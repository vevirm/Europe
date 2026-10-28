#!/usr/bin/env python3
"""Regenerate annual 2026 publication inventory from the repository's current JSON files.
No Deep Scan invocation; no scanner archives or reasoning outputs are modified.
"""
import json, re, hashlib, argparse
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit

ROOT=Path(__file__).resolve().parents[1]
START='2026-01-01'; END='2026-12-31'

def load(name, default):
    p=ROOT/name
    return json.loads(p.read_text(encoding='utf-8')) if p.exists() else default

def clean_date(v):
    v=str(v or '').strip()
    return v[:10] if re.fullmatch(r'\d{4}-\d{2}-\d{2}',v[:10]) else ''

def url(item):return str(item.get('link') or item.get('url') or item.get('landing_page_url') or '').strip()

def canonical(s):
    try:
        p=urlsplit(s.lower().strip());return urlunsplit((p.scheme,p.netloc,p.path.rstrip('/'),'', ''))
    except ValueError:return s.lower().strip()

def corrected(item, corrections):
    keys=['link:'+url(item),'url:'+url(item),'historical:id:'+str(item.get('id') or ''), 'id:'+str(item.get('id') or '')]
    for k in keys:
        c=corrections.get(k,{})
        d=clean_date((c.get('fields') or {}).get('date'))
        if d:return d,True
    return clean_date(item.get('date')),False

def make():
    raw=load('radar.json',{});active=load('radar_active.json',{});historical=load('historical/historical.json',{});corr=load('record_corrections.json',{}).get('records',{})
    records={}
    groups=[('Main Radar archive',raw.get('strand_a',[])+raw.get('strand_b',[])+raw.get('strand_c',[])),('Main Radar active',active.get('strand_a',[])+active.get('strand_b',[])+active.get('strand_c',[])),('Earlier Findings archive',historical.get('items',[]))]
    for group,items in groups:
        for item in items:
            if not isinstance(item,dict):continue
            strand=(item.get('strand') or ('C' if item.get('headline') else 'A')).upper()
            if strand not in ('A','B','C'):continue
            date,was_corrected=corrected(item,corr)
            if not START<=date<=END:continue
            title=str(item.get('title') or item.get('headline') or '').strip();link=url(item)
            if not title or not link:continue
            key=canonical(link) or hashlib.sha256((title.lower()+date).encode()).hexdigest()
            rec=records.get(key)
            candidate={'date':date,'title':title,'source':str(item.get('source') or item.get('venue') or ''),'authors':str(item.get('authors') or ''),'strand':strand,'url':link,'summary':str(item.get('core_message') or item.get('reader_point') or item.get('summary') or '')[:850].strip(),'topics':item.get('topic_labels') or item.get('topics') or [],'in_active_radar':group=='Main Radar active','original_collection':group,'date_corrected':was_corrected,'year':2026,'record_type':'Signal / news' if strand=='C' else 'Research / report'}
            if not isinstance(candidate['topics'],list):candidate['topics']=[]
            if rec:
                rec['in_active_radar'] |= candidate['in_active_radar'];rec['date_corrected'] |= candidate['date_corrected']
                if group=='Main Radar active' or (not rec['summary'] and candidate['summary']):
                    candidate['in_active_radar']=rec['in_active_radar'];candidate['date_corrected']=rec['date_corrected'];records[key]=candidate
            else:records[key]=candidate
    out=sorted(records.values(),key=lambda x:(x['date'],x['title']),reverse=True)
    p=ROOT/'2026-stuff/publications.json';p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps({'period_start':START,'period_end':END,'source_note':'Snapshot generated from repository JSON with available Deep Scan date corrections. Includes A/B research and reports and separately labeled Strand C signals. Archive membership may be historical; inclusion follows corrected publication date.','count':len(out),'publications':out},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(f'Created {p.relative_to(ROOT)} with {len(out)} unique publications')
    return out
if __name__=='__main__': make()
