#!/usr/bin/env python3
"""Regenerate 2026 Stuff JSON and XLSX from current repository scanner archives.
Does not run scanners, alter source archives, or modify analytical outputs.
"""
import argparse
import collections
import hashlib
import json
import re
from datetime import date
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit

ROOT = Path(__file__).resolve().parents[1]
START, END = '2026-01-01', '2026-12-31'
OUTPUT = ROOT / '2026-stuff'

def read(relative):
    path = ROOT / relative
    if not path.is_file():
        raise FileNotFoundError(f'Required input missing: {relative}; refusing to overwrite 2026 Stuff')
    return json.loads(path.read_text(encoding='utf-8'))

def clean_date(value):
    v = str(value or '').strip()[:10]
    if not re.fullmatch(r'\d{4}-\d{2}-\d{2}', v):
        return ''
    try:
        date.fromisoformat(v)
        return v
    except ValueError:
        return ''

def source_url(item):
    return str(item.get('link') or item.get('url') or item.get('landing_page_url') or '').strip()

def canonical(value):
    try:
        p = urlsplit(value.strip())
        return urlunsplit((p.scheme.lower(), p.netloc.lower(), p.path.rstrip('/'), '', ''))
    except ValueError:
        return value.strip().lower()

def corrected_date(item, corrections):
    link = source_url(item)
    ident = str(item.get('id') or '')
    keys = ['link:' + link, 'url:' + link]
    if ident:
        keys += ['historical:id:' + ident, 'id:' + ident]
    for key in keys:
        correction = corrections.get(key, {})
        if isinstance(correction, dict):
            d = clean_date((correction.get('fields') or {}).get('date'))
            if d:
                return d, True
    return clean_date(item.get('date')), False

def collect():
    raw = read('radar.json')
    active = read('radar_active.json')
    earlier = read('historical/historical.json')
    corrections = read('record_corrections.json').get('records', {})
    groups = [
        ('Main Radar archive', sum([raw.get('strand_'+k, []) for k in 'abc'], [])),
        ('Main Radar active', sum([active.get('strand_'+k, []) for k in 'abc'], [])),
        ('Earlier Findings archive', earlier.get('items', [])),
    ]
    records = {}
    for group, items in groups:
        for item in items:
            if not isinstance(item, dict):
                continue
            strand = str(item.get('strand') or ('C' if item.get('headline') else 'A')).upper()
            if strand not in ('A', 'B', 'C'):
                continue
            published, corrected = corrected_date(item, corrections)
            if not START <= published <= END:
                continue
            title = str(item.get('title') or item.get('headline') or '').strip()
            link = source_url(item)
            if not title or not link:
                continue
            key = canonical(link) or hashlib.sha256((title.lower()+published).encode()).hexdigest()
            previous = records.get(key)
            topics = item.get('topic_labels') or item.get('topics') or []
            if not isinstance(topics, list):
                topics = []
            candidate = {
                'date': published, 'title': title,
                'source': str(item.get('source') or item.get('venue') or ''),
                'authors': str(item.get('authors') or ''), 'strand': strand, 'url': link,
                'summary': str(item.get('core_message') or item.get('reader_point') or item.get('summary') or '')[:850].strip(),
                'topics': topics, 'in_active_radar': group == 'Main Radar active',
                'original_collection': group, 'date_corrected': corrected,
                'year': 2026, 'record_type': 'Signal / news' if strand == 'C' else 'Research / report',
            }
            if previous:
                candidate['in_active_radar'] |= previous['in_active_radar']
                candidate['date_corrected'] |= previous['date_corrected']
                if group == 'Main Radar active' or (not previous['summary'] and candidate['summary']):
                    records[key] = candidate
                else:
                    previous['in_active_radar'] = candidate['in_active_radar']
                    previous['date_corrected'] = candidate['date_corrected']
            else:
                records[key] = candidate
    return sorted(records.values(), key=lambda r: (r['date'], r['title']), reverse=True)

def excel(records, target):
    """Write a readable XLSX using Python's standard-library OOXML ZIP support.

    No PyPI-only spreadsheet package is needed on GitHub Actions runners.
    """
    from zipfile import ZipFile, ZIP_DEFLATED
    from xml.sax.saxutils import escape

    headers = ['Publication date', 'Title / headline', 'Source', 'Authors', 'Strand',
               'Record class', 'Original collection', 'Active Radar', 'Date corrected',
               'Topics', 'Summary / finding excerpt', 'Source URL']
    def row(r):
        return [r['date'], r['title'], r['source'], r['authors'], r['strand'],
                r['record_type'], r['original_collection'],
                'Yes' if r['in_active_radar'] else 'No',
                'Yes' if r['date_corrected'] else 'No',
                ', '.join(map(str, r['topics'])), r['summary'], r['url']]
    months = collections.defaultdict(lambda: [0, 0])
    for rec in records:
        months[rec['date'][:7]][1 if rec['strand'] == 'C' else 0] += 1
    sheets = [
        ('START HERE', [
            ['2026 — ALL ITEMS FOUND BY THE RADAR', ''],
            ['Period', '1 January–31 December 2026 (records available at generation)'],
            ['Total unique source URLs', len(records)],
            ['Research / reports', sum(r['strand'] != 'C' for r in records)],
            ['Signals / news', sum(r['strand'] == 'C' for r in records)],
            ['Date rule', 'Publication date; available Deep Scan corrections applied'],
            ['Scope', 'Discovered sources, not a census of all publications or independently verified conclusions'],
        ]),
        ('All 2026 items', [headers] + [row(r) for r in records]),
        ('Research and reports', [headers] + [row(r) for r in records if r['strand'] != 'C']),
        ('Signals and news', [headers] + [row(r) for r in records if r['strand'] == 'C']),
        ('Months', [['Month', 'Research / reports', 'Signals / news', 'Total']] + [
            [month, a, b, a+b] for month, (a, b) in sorted(months.items())]),
    ]

    def colname(index):
        result = ''
        while index:
            index, mod = divmod(index - 1, 26)
            result = chr(65 + mod) + result
        return result

    def xmltext(value):
        clean = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f]', '', str(value))
        return escape(clean, {'"': '&quot;', "'": '&apos;'})

    def sheet_xml(rows, widths):
        import numbers
        out = ['<?xml version="1.0" encoding="UTF-8" standalone="yes"?>',
               '<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">',
               '<sheetViews><sheetView workbookViewId="0"><pane ySplit="1" topLeftCell="A2" activePane="bottomLeft" state="frozen"/></sheetView></sheetViews>',
               '<cols>']
        for index, width in enumerate(widths, 1):
            out.append(f'<col min="{index}" max="{index}" width="{width}" customWidth="1"/>')
        out += ['</cols>', '<sheetData>']
        for ri, values in enumerate(rows, 1):
            out.append(f'<row r="{ri}">')
            for ci, value in enumerate(values, 1):
                address = f'{colname(ci)}{ri}'
                style = ' s="1"' if ri == 1 else ''
                if isinstance(value, numbers.Number) and not isinstance(value, bool):
                    out.append(f'<c r="{address}"{style}><v>{value}</v></c>')
                else:
                    out.append(f'<c r="{address}"{style} t="inlineStr"><is><t xml:space="preserve">{xmltext(value)}</t></is></c>')
            out.append('</row>')
        out.append('</sheetData>')
        if len(rows) > 1:
            out.append(f'<autoFilter ref="A1:{colname(len(rows[0]))}{len(rows)}"/>')
        out.append('</worksheet>')
        return ''.join(out).encode('utf-8')

    ns = 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'
    relns = 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'
    with ZipFile(target, 'w', ZIP_DEFLATED, compresslevel=6) as z:
        types = ['<?xml version="1.0" encoding="UTF-8" standalone="yes"?>',
                 '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">',
                 '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>',
                 '<Default Extension="xml" ContentType="application/xml"/>',
                 '<Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/>',
                 '<Override PartName="/xl/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.styles+xml"/>']
        for i in range(1, len(sheets)+1):
            types.append(f'<Override PartName="/xl/worksheets/sheet{i}.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>')
        z.writestr('[Content_Types].xml', ''.join(types) + '</Types>')
        z.writestr('_rels/.rels', '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
                   '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
                   '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="xl/workbook.xml"/>'
                   '</Relationships>')
        wb = [f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?><workbook xmlns="{ns}" xmlns:r="{relns}"><sheets>']
        rels = ['<?xml version="1.0" encoding="UTF-8" standalone="yes"?>',
                '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">']
        for i, (name, rows) in enumerate(sheets, 1):
            wb.append(f'<sheet name="{xmltext(name)}" sheetId="{i}" r:id="rId{i}"/>')
            rels.append(f'<Relationship Id="rId{i}" Type="{relns}/worksheet" Target="worksheets/sheet{i}.xml"/>')
            widths = ([36, 85] if i == 1 else
                      [18, 60, 30, 26, 12, 21, 26, 16, 18, 44, 90, 65] if i in (2, 3, 4)
                      else [24, 24, 24, 24])
            z.writestr(f'xl/worksheets/sheet{i}.xml', sheet_xml(rows, widths))
        wb.append('</sheets></workbook>')
        rels.append(f'<Relationship Id="rId{len(sheets)+1}" Type="{relns}/styles" Target="styles.xml"/>')
        z.writestr('xl/workbook.xml', ''.join(wb))
        z.writestr('xl/_rels/workbook.xml.rels', ''.join(rels) + '</Relationships>')
        z.writestr('xl/styles.xml', f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
                  f'<styleSheet xmlns="{ns}"><fonts count="2"><font><sz val="11"/><name val="Aptos"/></font>'
                  '<font><b/><color rgb="FFFFFFFF"/><sz val="11"/><name val="Aptos"/></font></fonts>'
                  '<fills count="3"><fill><patternFill patternType="none"/></fill>'
                  '<fill><patternFill patternType="gray125"/></fill>'
                  '<fill><patternFill patternType="solid"><fgColor rgb="FF102344"/><bgColor indexed="64"/></patternFill></fill></fills>'
                  '<borders count="1"><border><left/><right/><top/><bottom/><diagonal/></border></borders>'
                  '<cellStyleXfs count="1"><xf numFmtId="0" fontId="0" fillId="0" borderId="0"/></cellStyleXfs>'
                  '<cellXfs count="2"><xf numFmtId="0" fontId="0" fillId="0" borderId="0" xfId="0"/>'
                  '<xf numFmtId="0" fontId="1" fillId="2" borderId="0" xfId="0" applyFont="1" applyFill="1"/></cellXfs>'
                  '</styleSheet>')

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--allow-large-drop',action='store_true',help='Explicit override of shrinkage protection')
    args=parser.parse_args()
    records=collect()
    if not records:
        raise SystemExit('Refusing to publish an empty 2026 inventory')
    target=OUTPUT/'publications.json'
    if target.exists() and not args.allow_large_drop:
        previous=json.loads(target.read_text(encoding='utf-8')).get('count', 0)
        if previous and len(records) < previous * 0.9:
            raise SystemExit(f'Safety stop: count fell from {previous} to {len(records)} (>10%). Inspect inputs first.')
    OUTPUT.mkdir(parents=True,exist_ok=True)
    document={
        'period_start':START,'period_end':END,
        'source_note':'Generated from current repository scanner archives with available Deep Scan date corrections. Research and reports are separated from Strand C signals. Counts represent deduplicated discovered sources.',
        'count':len(records),'publications':records,
    }
    new_json=target.with_suffix('.json.tmp')
    new_excel=OUTPUT/'2026_publications.xlsx.tmp'
    excel(records,new_excel)
    new_json.write_text(json.dumps(document,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    new_json.replace(target)
    new_excel.replace(OUTPUT/'2026_publications.xlsx')
    print(f'Updated JSON and XLSX: {len(records)} unique source records')

if __name__=='__main__':
    main()
