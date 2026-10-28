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
    from artifact_tool import Workbook, SpreadsheetFile
    workbook = Workbook.create()
    intro = workbook.worksheets.add('START HERE')
    intro.get_range('A1:B7').values = [
        ['2026 — ALL ITEMS FOUND BY THE RADAR', ''],
        ['Period', '1 January–31 December 2026 (records available at generation)'],
        ['Total unique source URLs', len(records)],
        ['Research / reports', sum(r['strand'] != 'C' for r in records)],
        ['Signals / news', sum(r['strand'] == 'C' for r in records)],
        ['Date rule', 'Publication date; available Deep Scan corrections applied'],
        ['Scope', 'Discovered sources, not a census of all publications or independently verified conclusions'],
    ]
    intro.get_range('A1:B1').format.fill = '#102344'
    intro.get_range('A1:B1').format.font.color = '#FFFFFF'
    intro.get_range('A1:B1').format.font.bold = True
    intro.get_range('A:A').format.column_width = 37
    intro.get_range('B:B').format.column_width = 85
    headers = ['Publication date','Title / headline','Source','Authors','Strand','Record class','Original collection','Active Radar','Date corrected','Topics','Summary / finding excerpt','Source URL']
    def xmlsafe(value):
        return re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f]', '', str(value))
    def row(r):
        return [r['date'],r['title'],r['source'],r['authors'],r['strand'],r['record_type'],r['original_collection'],
                'Yes' if r['in_active_radar'] else 'No','Yes' if r['date_corrected'] else 'No',
                ', '.join(map(str,r['topics'])),r['summary'],r['url']]
    for name, subset in [('All 2026 items', records), ('Research and reports', [r for r in records if r['strand']!='C']),
                         ('Signals and news', [r for r in records if r['strand']=='C'])]:
        sheet = workbook.worksheets.add(name)
        sheet.get_range_by_indexes(0,0,len(subset)+1,len(headers)).values = [headers]+[[xmlsafe(v) for v in row(r)] for r in subset]
        head = sheet.get_range('A1:L1')
        head.format.fill = '#102344'
        head.format.font.color = '#FFFFFF'
        head.format.font.bold = True
        sheet.freeze_panes.freeze_rows(1)
        for col, width in [('A',18),('B',60),('C',30),('D',26),('E',12),('F',21),('G',26),('H',16),('I',18),('J',44),('K',90),('L',65)]:
            sheet.get_range(f'{col}:{col}').format.column_width = width
        sheet.tables.add(f'A1:L{len(subset)+1}', True, 'T'+name.replace(' ','').replace('2026','Y2026'))
    months=collections.defaultdict(lambda:[0,0])
    for rec in records:
        bucket=months[rec['date'][:7]]
        bucket[1 if rec['strand']=='C' else 0]+=1
    monthly=workbook.worksheets.add('Months')
    matrix=[['Month','Research / reports','Signals / news','Total']]
    for month in sorted(months):
        a,b=months[month]
        matrix.append([month,a,b,a+b])
    monthly.get_range_by_indexes(0,0,len(matrix),4).values=matrix
    monthly.get_range('A1:D1').format.fill='#102344'
    monthly.get_range('A1:D1').format.font.color='#FFFFFF'
    monthly.get_range('A1:D1').format.font.bold=True
    monthly.get_range('A:D').format.column_width=24
    SpreadsheetFile.export_xlsx(workbook).save(str(target))

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
