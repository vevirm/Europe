(function(g){
  'use strict';

  /* Eight reader maps cover different parts of Europe’s economic security.
     The labels are a hierarchy; the live corpus decides which maps are strongest now. */
  const HIERARCHIES=[
    {id:"raw_materials_energy",label:"Raw materials & energy",subs:[{label:"Supply exposure",leaves:[{label:"Critical raw materials & processing",terms:["critical raw material", "rare earth", "gallium", "germanium", "graphite", "refining", "processing"]},{label:"Energy supply & routes",terms:["lng", "gas supply", "energy security", "pipeline", "energy imports"]}]},{label:"European response",leaves:[{label:"Stockpiles, projects & partnerships",terms:["stockpil", "strategic project", "resourceeu", "critical raw materials act", "critical minerals partnership", "diversif"]}]}]},
    {id:"technology",label:"Technology security",subs:[{label:"Protect technology",leaves:[{label:"Export controls & dual use",terms:["export control", "dual-use", "dual use", "entity list"]},{label:"Leakage & outbound investment",terms:["technology leakage", "outbound investment", "technology transfer", "know-how"]}]},{label:"Build capacity",leaves:[{label:"Chips & critical technologies",terms:["semiconductor", "chips act", "quantum", "artificial intelligence", "critical technolog"]}]}]},
    {id:"investment",label:"Investment & ownership",subs:[{label:"Inbound",leaves:[{label:"FDI screening & takeovers",terms:["fdi screening", "investment screening", "takeover", "acquisition", "golden power"]},{label:"Foreign subsidies",terms:["foreign subsidies", "state-owned", "subsidised"]}]},{label:"Capital",leaves:[{label:"European capital for strategic firms",terms:["capital markets", "savings and investments union", "scale-up", "european competitiveness fund", "eib"]}]}]},
    {id:"trade",label:"Trade policy",subs:[{label:"Defend",leaves:[{label:"Trade defence & overcapacity",terms:["anti-dumping", "anti-subsidy", "safeguard", "overcapacity", "trade defence"]},{label:"Tariffs & market access",terms:["tariff", "market access", "customs"]}]},{label:"Rules",leaves:[{label:"WTO & the open trading system",terms:["wto", "multilateral", "rules-based", "fragmentation"]}]}]},
    {id:"coercion",label:"Coercion & sanctions",subs:[{label:"Pressure on Europe",leaves:[{label:"Economic coercion",terms:["economic coercion", "coercion", "weaponis", "weaponiz", "retaliat"]},{label:"Secondary sanctions & legal reach",terms:["secondary sanctions", "extraterritorial", "entity list"]}]},{label:"Europe’s tools",leaves:[{label:"Sanctions & anti-coercion",terms:["sanctions package", "restrictive measures", "anti-coercion", "circumvention"]}]}]},
    {id:"industry",label:"Industry & competitiveness",subs:[{label:"Capacity",leaves:[{label:"Strategic manufacturing",terms:["manufacturing", "production capacity", "industrial accelerator act", "made in europe", "european preference"]},{label:"Defence industry",terms:["defence industry", "defense industry", "ammunition", "rearm europe", "edip"]}]},{label:"Costs",leaves:[{label:"Energy costs & deindustrialisation",terms:["energy prices", "energy costs", "deindustriali", "plant closure"]}]}]},
    {id:"infrastructure",label:"Critical infrastructure",subs:[{label:"Physical links",leaves:[{label:"Cables, grids, pipelines & ports",terms:["subsea cable", "undersea cable", "grid", "pipeline", "port"]}]},{label:"Control",leaves:[{label:"Vendors, ownership & sabotage",terms:["high-risk vendor", "5g", "foreign ownership", "sabotage", "hybrid"]}]}]},
    {id:"partners",label:"Partners & agreements",subs:[{label:"Agreements",leaves:[{label:"Trade agreements",terms:["trade agreement", "free trade agreement", "mercosur", "india", "partnership agreement"]},{label:"G7 & like-minded coordination",terms:["g7", "like-minded", "trade and technology council", "japan"]}]},{label:"Great powers",leaves:[{label:"China & the US",terms:["china", "united states", "transatlantic", "us-china", "de-risk"]}]}]}
  ];

  const NODE_COPY={};

  const clean=s=>String(s||'').replace(/\s+/g,' ').trim();
  const escRx=s=>String(s).replace(/[.*+?^${}()|[\]\\]/g,'\\$&');
  const rowText=x=>[x?.title,x?.headline,x?.what,x?.core_message,x?.summary,x?.relevance_note,x?.why_it_matters,x?.source,...(x?.ri_evidence||[]),...(x?.geo_evidence||[])].map(v=>clean(v)).join(' ').toLowerCase();
  function hasTerm(h,t){const q=clean(t).toLowerCase();if(!q)return false;const p=escRx(q).replace(/\\ /g,'\\s+');return new RegExp('(^|[^a-z0-9])'+p+'([^a-z0-9]|$)','i').test(h)}
  function termHits(x,leaf){const h=rowText(x);let n=0;for(const t of leaf.terms||[])if(hasTerm(h,t))n++;return n}
  function stamp(x){const n=Date.parse(x?.date||0);return Number.isFinite(n)?n:0}

  function evaluate(items){
    const live=(items||[]).filter(x=>x&&typeof x==='object');
    return HIERARCHIES.map(h=>{
      const leaves=h.subs.flatMap(s=>s.leaves.map(l=>({...l,sub:s.label})));
      const matches=[];let supported=0,newRows=0,recency=0;
      const leafSupport=leaves.map(leaf=>{
        const ms=[];
        live.forEach((x,i)=>{const hits=termHits(x,leaf);if(hits){const m={x,i,hits,leaf};ms.push(m);matches.push(m);if(x.new_this_scan)newRows++}});
        if(ms.length)supported++;
        const newest=ms.reduce((n,m)=>Math.max(n,stamp(m.x)),0);recency=Math.max(recency,newest);
        return {leaf,matches:ms};
      });
      const score=matches.reduce((s,m)=>s+1+Math.min(3,m.hits-1)*.22+(m.x?.new_this_scan ? .12 : 0),0)+supported*6+(newRows?Math.min(3,newRows)*1.5:0)+(recency?recency/1e15:0);
      return {...h,matches,leafSupport,supported,score};
    }).filter(x=>x.supported>=2).sort((a,b)=>b.supported-a.supported||b.score-a.score||a.label.localeCompare(b.label));
  }

  function chooseMain(evals,count){
    const n=Math.max(1,Math.min(8,Number(count)||8));
    const pinned=['raw_materials_energy','technology','investment','trade','coercion','industry','infrastructure','partners'];
    const out=[];
    for(const id of pinned){const e=evals.find(x=>x.id===id);if(e&&!out.includes(e)&&out.length<n)out.push(e)}
    for(const e of evals){if(out.length>=n)break;if(!out.includes(e))out.push(e)}
    return out.slice(0,n);
  }

  function bestMatch(ms){
    return [...(ms||[])].sort((a,b)=>(b.hits-a.hits)||((b.x?.new_this_scan?1:0)-(a.x?.new_this_scan?1:0))||(stamp(b.x)-stamp(a.x)))[0]||null;
  }
  function nodeMeta(ms,query,label){
    const unique=new Map();for(const m of ms||[]){const key=clean(m.x?.link)||clean(m.x?.title)||String(m.i);if(!unique.has(key))unique.set(key,m)}
    const matches=[...unique.values()],best=bestMatch(matches),x=best?.x||{};
    const copy=NODE_COPY[label]||{};
    const whatRaw=copy.what||globalThis.RadarReaderStyle?.whatFor?.(x)||clean(x.core_message||x.what||x.title||'');
    const whyRaw=copy.why||globalThis.RadarReaderStyle?.whyFor?.(x)||clean(x.why_it_matters||x.relevance_note||'');
    const what=globalThis.RadarReaderStyle?.limit?.(whatRaw||`${label} is active in the current material.`,18)||whatRaw;
    const why=globalThis.RadarReaderStyle?.limit?.(whyRaw||'It changes a specific European research capability, dependency, rule or partnership.',15)||whyRaw;
    return {query:clean(query),evidenceCount:matches.length,sourceLink:clean(x.link),sourceTitle:clean(x.title||x.headline),sourceName:clean(x.source),what,why};
  }
  function build(items,opt={}){
    const evals=evaluate(items),count=Math.max(1,Math.min(8,Number(opt.count)||8));
    const mains=chooseMain(evals,count);
    return mains.map((h,index)=>{
      const support=new Map(h.leafSupport.map(v=>[v.leaf.label,v.matches]));
      const subs=h.subs.map((sub,si)=>{
        const subMatches=sub.leaves.flatMap(l=>support.get(l.label)||[]);
        const query=sub.leaves[0]?.terms?.[0]||sub.label;
        return {id:`${h.id}-s${si+1}`,label:sub.label,...nodeMeta(subMatches,query,sub.label)};
      });
      const leaves=h.subs.flatMap((sub,si)=>sub.leaves.map((leaf,li)=>({
        id:`${h.id}-s${si+1}-l${li+1}`,label:leaf.label,...nodeMeta(support.get(leaf.label)||[],leaf.terms?.[0]||leaf.label,leaf.label)
      }))).slice(0,3);
      const mainQuery=h.subs[0]?.leaves?.[0]?.terms?.[0]||h.label;
      return {id:h.id,rank:index+1,main:{id:h.id,label:h.label,...nodeMeta(h.matches,mainQuery,h.label)},subs,leaves};
    });
  }

  g.RadarIssues={build,buildTrees:build,evaluate,chooseMain,hierarchies:HIERARCHIES};
})(globalThis);
