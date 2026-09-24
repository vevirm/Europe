(function(root,factory){
  if(typeof module==='object'&&module.exports)module.exports=factory(require('./scenarios.js'),require('../reader_rank.js'));
  else root.RadarShockVariants=factory(root.RadarShockScenarios,root.RadarReaderRank);
})(typeof globalThis!=='undefined'?globalThis:this,function(Scenarios,ReaderRank){
  'use strict';
  const clean=v=>String(v||'').replace(/\s+/g,' ').trim();
  const low=v=>clean(v).toLowerCase();
  const dateValue=v=>{const n=Date.parse(v||'');return Number.isFinite(n)?n:0};
  const qualityScore=x=>Math.max(0,Math.min(100,Number(x?._storedQuality??ReaderRank?.scoreFor?.(x))||0));
  const rx=v=>v instanceof RegExp?v:new RegExp(String(v),'i');
  function rowText(x){return low([x.title,x.headline,x.what,x.core_message,x.summary,x.relevance_note,x.why_it_matters,x.source].join(' '))}
  function matches(x,spec){
    const t=rowText(x);
    if(spec.all&&spec.all.some(p=>!rx(p).test(t)))return false;
    if(spec.any&&spec.any.length&&!spec.any.some(p=>rx(p).test(t)))return false;
    if(spec.none&&spec.none.some(p=>rx(p).test(t)))return false;
    return true;
  }
  function score(x,spec){
    const t=rowText(x);let n=qualityScore(x)*100;
    for(const p of spec.all||[])if(rx(p).test(t))n+=35;
    for(const p of spec.any||[])if(rx(p).test(t))n+=18;
    if(spec.preferSource&&rx(spec.preferSource).test(clean(x.source)))n+=220;
    if(spec.preferTitle&&rx(spec.preferTitle).test(clean(x.title||x.headline)))n+=260;
    if(x.new_this_scan)n+=12;
    n+=dateValue(x.date)/1e12;
    return n;
  }
  function corpus(data){
    const out=[],seen=new Set();
    for(const [key,prefix] of [['strand_a','A'],['strand_c','C'],['strategic_pathways','P']]){
      const xs=Array.isArray(data?.[key])?data[key]:[];
      xs.forEach((x,i)=>{if(!x||typeof x!=='object')return;const k=clean(x.link)||clean(x.title||x.headline).toLowerCase();if(k&&seen.has(k))return;if(k)seen.add(k);out.push({...x,_row:`${prefix}${String(i+1).padStart(3,'0')}`,_strand:prefix})});
    }
    return out;
  }
  function pick(rows,spec,used){
    const candidates=rows.filter(x=>!used.has(x._row)&&matches(x,spec)).sort((a,b)=>score(b,spec)-score(a,spec));
    const chosen=candidates[0];if(chosen)used.add(chosen._row);return chosen||null;
  }

  const PROFILES={};


  function findScenario(data,id){
    const all=[...(Scenarios?.buildDirect?.(data)||[]),...(Scenarios?.build?.(data)||[]),...(Scenarios?.buildDynamic?.(data)||[])];
    return all.find(s=>s.id===id)||null;
  }
  function counterEvidence(data,scenario,profile){
    if(Array.isArray(scenario?.againstEvidence)&&scenario.againstEvidence.length)return scenario.againstEvidence.slice().sort((a,b)=>(b.quality||0)-(a.quality||0)).slice(0,5);
    const rows=corpus(data),used=new Set((scenario.evidence||[]).map(e=>e.row._row)),out=[];
    for(const [role,spec] of profile.counterRoles||[]){const row=pick(rows,spec,used);if(row)out.push({role,row,quality:qualityScore(row)})}
    // If a genuinely double-edged row is already part of the shock case, allow it
    // back only when the independent counter search found too little evidence.
    if(out.length<2){
      const used2=new Set();
      for(const [role,spec] of profile.counterRoles||[]){const row=pick(rows,spec,used2);if(row&&!out.some(e=>e.row._row===row._row))out.push({role,row,quality:qualityScore(row)})}
    }
    return out.sort((a,b)=>b.quality-a.quality).slice(0,5);
  }
  const GENERIC_COUNTER_ROLES=[
    ['European substitution / diversification',{any:[/diversif/,/substitut/,/alternative supplier/,/strategic autonomy/,/resilien/]}],
    ['Shared or federated European capacity',{any:[/federat/,/shared infrastructure/,/research infrastructure/,/eurohpc/,/open access/]}],
    ['European policy capacity',{any:[/european commission/,/framework programme/,/horizon europe/,/funding/,/procurement/,/regulatory sandbox/]}],
    ['Open or international cooperation channel',{any:[/science diplomacy/,/international cooperation/,/association/,/open science/,/research collaboration/]}],
    ['Talent / capability reinforcement',{any:[/attract and retain/,/research talent/,/skills/,/training/,/capacity building/]}]
  ];
  function genericProfile(scenario){
    return {
      variants:[
        {id:'contained',label:'Contained',title:`Contained: ${scenario.title}`,text:'The mechanism appears, but redundancy, substitution, workarounds or policy response keep it local and temporary.'},
        {id:'core',label:'Core shock',title:scenario.title,text:scenario.plainly||'The disruption reaches the capability described in the scenario.'},
        {id:'compound',label:'Compound',title:`Compound: ${scenario.title}`,text:`The same mechanism lands together with an adjacent dependency or policy failure. ${scenario.secondOrder||''}`.trim()}
      ],
      counterRoles:GENERIC_COUNTER_ROLES
    };
  }
  function build(data,id){
    const scenario=findScenario(data,id);
    if(!scenario)return null;
    const profile=PROFILES[id]||genericProfile(scenario);
    return {
      scenario,
      variants:profile.variants,
      forEvidence:(scenario.evidence||[]).slice(0,7),
      againstEvidence:counterEvidence(data,scenario,profile)
    };
  }
  function scenarioIdForRealised(x){
    const t=low([x?.title,x?.headline,x?.what,x?.core_message,x?.summary,x?.lens?.shock_family].join(' '));
    if(/cyber|software vulnerab|digital outage/.test(t))return 'direct_cyber_infrastructure';
    if(/armed conflict|war |war-|invasion|refugee|displac/.test(t))return 'direct_conflict_research_corridor';
    if(/research collaboration|grant restriction|participation ban|data exchange/.test(t))return 'direct_collaboration_restriction';
    if(/export|trade disruption|critical raw material|chip|semiconductor|dual-use/.test(t))return 'direct_materials_cutoff';
    return null;
  }
  return {build,profiles:PROFILES,scenarioIdForRealised};
});
