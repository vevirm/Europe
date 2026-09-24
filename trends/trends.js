/* v21.7 — trend/counter-trend tug-of-war from the retained Radar corpus.
   Publication rule is intentionally simple:
   - a side needs at least three current records from at least two independent sources;
   - a pair therefore needs current evidence on both sides before it is published;
   - historical material older than the six-month boundary may add context,
     but it cannot make a current trend qualify.
   Weighting remains deliberately playful: stronger and more independent evidence
   pulls harder, repeated publication from the same source pulls less. */
(function(root,factory){
  if(typeof module==='object'&&module.exports)module.exports=factory(require('../reader_rank.js'));
  else root.RadarTrends=factory(root.RadarReaderRank);
})(typeof globalThis!=='undefined'?globalThis:this,function(ReaderRank){
  'use strict';
  const clean=v=>String(v||'').replace(/\s+/g,' ').trim();
  const low=v=>clean(v).toLowerCase();
  const rx=v=>v instanceof RegExp?v:new RegExp(String(v),'i');
  const dateValue=v=>{const n=Date.parse(v||'');return Number.isFinite(n)?n:0};
  const quality=x=>Math.max(0,Math.min(100,Number(ReaderRank?.scoreFor?.(x))||0));
  function rowText(x){return low([x.title,x.headline,x.what,x.reader_point,x.core_message,x.summary,x.relevance_note,x.why_it_matters,x.bridge_sentence,(x.geo_evidence||[]).join(' '),(x.ri_evidence||[]).join(' '),(x.topics||[]).join(' '),(x.topic_labels||[]).join(' '),x.source].join(' '))}
  function source(x){return clean(x?.source||x?.journal||x?.institution||x?.venue||'')}
  function historyText(x){return low([x.title,x.reader_title,x.reader_point,x.reader_what,x.reader_more,x.core_message,x.summary,x.relevance_note,x.source].join(' '))}
  const HISTORY_EU=/\b(?:eu|europe|european|horizon|eurohpc|erc|eic|jrc|commission|member states)\b/i;
  const ACTOR=/\b(?:European Commission|European Investment Bank|EEAS|European Central Bank|EuroHPC|Council of the European Union|European Parliament|Joint Research Centre|JRC Publications Repository|ERA Portal|Marie Skłodowska-Curie Actions|Research Council of|Ministry|Agency for|Government of|Fusion for Energy)\b/i;
  const EU_POLICY_ACTOR=/\b(?:European Commission|European Innovation Council|European Research Council|EuroHPC|Council of the European Union|Joint Research Centre|JRC Publications Repository|ERA Portal|Marie Skłodowska-Curie Actions)\b/i;
  function reportingRole(x){return ACTOR.test(source(x))?'actor':'observer'}

  function currentCorpus(data){
    const out=[],seen=new Set();
    for(const [key,prefix] of [['strand_a','A'],['strand_c','C'],['strategic_pathways','P']]){
      const xs=Array.isArray(data?.[key])?data[key]:[];
      xs.forEach((x,i)=>{if(!x||typeof x!=='object')return;const k=clean(x.link)||low(x.title||x.headline||x.what);if(k&&seen.has(k))return;if(k)seen.add(k);out.push({...x,_row:`${prefix}${String(i+1).padStart(3,'0')}`,_strand:prefix,_historical:false})});
    }
    return out;
  }
  function historicalCorpus(history){
    const xs=Array.isArray(history?.items)?history.items:[];
    const cutoff=Date.parse(history?.cutoff_exclusive||history?.date_to||'');
    const seen=new Set(),out=[];
    xs.forEach((x,i)=>{
      if(!x||typeof x!=='object')return;
      const d=dateValue(x.date);
      if(Number.isFinite(cutoff)&&cutoff>0&&d>=cutoff)return;
      const k=clean(x.url||x.link)||low(x.title||x.reader_point);
      if(k&&seen.has(k))return;if(k)seen.add(k);
      const rw=Number(x.historical_reasoning_weight);
      if(Number.isFinite(rw)&&rw<=0)return;
      out.push({...x,link:x.link||x.url||'',_row:`H${String(i+1).padStart(3,'0')}`,_strand:'H',_historical:true});
    });
    return out;
  }
  function matches(x,spec){
    const t=rowText(x);
    if(spec?.all&&spec.all.some(p=>!rx(p).test(t)))return false;
    if(spec?.any&&spec.any.length&&!spec.any.some(p=>rx(p).test(t)))return false;
    if(spec?.none&&spec.none.some(p=>rx(p).test(t)))return false;
    return true;
  }
  function hostileWitness(x,role){
    if(!role.hostileWitness)return false;
    if(role.hostileSource&&!rx(role.hostileSource).test(source(x)))return false;
    return EU_POLICY_ACTOR.test(source(x));
  }
  function candidateScore(x,role){
    let n=quality(x)*100;
    const t=rowText(x);
    for(const p of role.spec?.all||[])if(rx(p).test(t))n+=36;
    for(const p of role.spec?.any||[])if(rx(p).test(t))n+=14;
    if(role.spec?.preferSource&&rx(role.spec.preferSource).test(source(x)))n+=180;
    if(role.spec?.preferTitle&&rx(role.spec.preferTitle).test(clean(x.title||x.headline)))n+=220;
    if(hostileWitness(x,role))n+=300;
    if(x._strand==='C')n+=35; // a current observed change is useful in a trend tug-of-war
    n+=dateValue(x.date)/1e12;
    return n;
  }
  function pick(rows,role,usedRows){
    const candidates=rows.filter(x=>!usedRows.has(x._row)&&matches(x,role.spec||{})).sort((a,b)=>candidateScore(b,role)-candidateScore(a,role));
    const x=candidates[0]||null;if(x)usedRows.add(x._row);return x;
  }
  function claimWeight(x,role,sourceUse){
    const q=quality(x),rr=reportingRole(x),type=role.claimType||'diagnosis';
    let mult=1;
    if(type==='action')mult*=rr==='actor'?1.08:0.97;
    else if(type==='effect'||type==='outcome')mult*=rr==='actor'?0.72:1.08;
    else mult*=rr==='actor'?0.88:1.04;
    const hostile=hostileWitness(x,role);if(hostile)mult*=1.18;
    const src=source(x).toLowerCase(),count=sourceUse.get(src)||0;
    if(count===1)mult*=0.86;else if(count>=2)mult*=0.68;
    sourceUse.set(src,count+1);
    return {weight:q*mult,quality:q,reporting:rr,hostile};
  }
  function historyScore(x){
    const merit=Math.max(0,Math.min(100,Number(x?.source_merit_score)||0));
    const trust=Number.isFinite(Number(x?.historical_reasoning_weight))?Math.max(0,Math.min(1,Number(x.historical_reasoning_weight))):0.35;
    // Historical context never qualifies the current trend, but Deep-Scan-kept
    // context should be chosen ahead of provisional/review material when both match.
    return trust*100000+merit*10+dateValue(x.date)/1e12;
  }
  function pickHistory(rows,side,currentEvidence){
    const patterns=side.historyAny||[];
    if(!patterns.length)return [];
    const currentKeys=new Set(currentEvidence.map(e=>clean(e.row.link||e.row.url)||low(e.row.title)));
    const picked=[],seenSources=new Set();
    const candidates=rows.filter(x=>HISTORY_EU.test(historyText(x))&&patterns.some(p=>rx(p).test(historyText(x)))).sort((a,b)=>historyScore(b)-historyScore(a));
    for(const x of candidates){
      const k=clean(x.link||x.url)||low(x.title);if(k&&currentKeys.has(k))continue;
      const s=source(x).toLowerCase();if(s&&seenSources.has(s))continue;
      picked.push(x);if(s)seenSources.add(s);if(picked.length>=2)break;
    }
    return picked;
  }
  function sideEvidence(currentRows,historicalRows,side){
    const used=new Set(),sourceUse=new Map(),evidence=[];
    for(const role of side.roles){
      const row=pick(currentRows,role,used);if(!row)continue;
      const w=claimWeight(row,role,sourceUse);
      evidence.push({role:role.label,row,...w,claimType:role.claimType||'diagnosis'});
    }
    const sources=new Set(evidence.map(e=>source(e.row).toLowerCase()).filter(Boolean));
    const movements=evidence.filter(e=>e.claimType==='action'||e.claimType==='effect'||e.claimType==='outcome'||e.row._strand==='C').length;
    const avg=evidence.length?evidence.reduce((a,e)=>a+e.quality,0)/evidence.length:0;
    const observers=evidence.filter(e=>e.reporting==='observer').length;
    const hostile=evidence.filter(e=>e.hostile).length;
    const sum=evidence.reduce((a,e)=>a+e.weight,0);
    // Stronger evidence pulls harder; different sources add a small bonus; repetition is already discounted above.
    const diversityBonus=Math.min(18,sources.size*3)+Math.min(8,observers*2)+hostile*4;
    evidence.sort((a,b)=>(b.hostile?1:0)-(a.hostile?1:0)||b.quality-a.quality);
    const history=pickHistory(historicalRows,side,evidence);
    return {
      evidence,history,raw:sum+diversityBonus,averageQuality:Math.round(avg),
      bestQuality:evidence.length?Math.max(...evidence.map(e=>e.quality)):0,
      sourceCount:sources.size,movementCount:movements,observerCount:observers,hostileCount:hostile
    };
  }
  function sideQualifies(side){
    return side.evidence.length>=3&&side.sourceCount>=2&&side.bestQuality>=85&&side.averageQuality>=72;
  }

  const PAIRS=[
    {
      id:'protect_vs_open',
      left:{title:'Europe is protecting its economy more',plain:'The EU is using screening, export controls, trade defence and anti-coercion tools more often and more boldly.',why:'Stronger tools reduce exposure to pressure and unfair competition.',historyAny:[/economic security/,/screening/,/trade defen[cs]e/,/export control/,/anti-coercion/],roles:[
        {label:'Economic-security strategy',claimType:'action',spec:{any:[/economic security (?:strategy|package|doctrine)/,/strengthening eu economic security/,/civil society dialogue on economic security/]}},
        {label:'Investment screening',claimType:'action',spec:{any:[/fdi screening/,/investment screening/,/screening regulation/]}},
        {label:'Export controls',claimType:'action',spec:{any:[/export control/,/dual-use items/,/control list/]}},
        {label:'Trade defence',claimType:'action',spec:{any:[/anti-dumping/,/anti-subsidy/,/safeguard/,/foreign subsidies/]}}
      ]},
      right:{title:'Openness to trade and investment is under strain',plain:'Evidence points to the costs of protection: higher prices, retaliation, WTO friction and lost partners.',why:'If protection costs too much, support for it and for open trade can both erode.',historyAny:[/wto/,/protectionis/,/fragmentation/,/open trade/],roles:[
        {label:'Cost of fragmentation',claimType:'diagnosis',spec:{any:[/fragmentation/,/cost of de-?risking/,/welfare/]}},
        {label:'WTO friction',claimType:'effect',spec:{any:[/wto/,/erga omnes/,/multilateral/]}},
        {label:'Retaliation risk',claimType:'effect',spec:{any:[/retaliat/,/countermeasure/,/trade war/]}}
      ]},
      flip:'The balance changes if protective tools are shown to work at low cost, or if their costs clearly outweigh the risks they address.'
    },
    {
      id:'diversify_vs_concentrate',
      left:{title:'Europe is diversifying its supplies',plain:'New partnerships, strategic projects and stockpiles are widening Europe\u2019s sources of critical inputs.',why:'More suppliers mean less leverage for any one of them.',historyAny:[/diversif/,/critical raw materials act/,/repowereu/,/partnership/],roles:[
        {label:'Raw-material partnerships',claimType:'action',spec:{any:[/partnership on critical raw materials/,/critical minerals partnership/,/raw materials platform/,/strategic project/]}},
        {label:'Energy diversification',claimType:'action',spec:{any:[/diversification of gas supply/,/lng/,/security of (?:oil|gas) supply/]}},
        {label:'Supply-chain redesign',claimType:'action',spec:{any:[/redesigning supply chains/,/supply chain optimi[sz]ation/,/reshor|friendshor/]}}
      ]},
      right:{title:'Dependence on a few suppliers persists',plain:'Critical inputs, processing and some technologies still come from a small number of countries.',why:'Concentration keeps Europe exposed to cutoffs and coercion.',historyAny:[/dependenc/,/concentrat/,/rare earth/,/china/],roles:[
        {label:'Import concentration',claimType:'diagnosis',spec:{any:[/strategic dependenc/,/import dependence/,/concentrat/]}},
        {label:'Processing dominance',claimType:'diagnosis',spec:{any:[/rare earth/,/refining|processing capacity/,/critical raw material/]}},
        {label:'Export dependence',claimType:'diagnosis',spec:{any:[/export dependence/,/geoeconomic exposure/]}}
      ]},
      flip:'The balance changes if new sources carry real volumes, or if concentration deepens faster than diversification.'
    },
    {
      id:'partners_vs_rivalry',
      left:{title:'Europe is widening its circle of partners',plain:'Trade agreements, strategic partnerships and G7 coordination are expanding.',why:'Partners spread risk and make European tools more effective.',historyAny:[/trade agreement/,/partnership/,/g7/,/global gateway/],roles:[
        {label:'Trade agreements',claimType:'action',spec:{any:[/trade agreement/,/free trade/,/mercosur|india|asean/]}},
        {label:'Strategic partnerships',claimType:'action',spec:{any:[/strategic partnership/,/global gateway/,/greenland partnership/]}},
        {label:'Like-minded coordination',claimType:'action',spec:{any:[/like-minded/,/g7/,/japan/]}}
      ]},
      right:{title:'Great-power rivalry narrows Europe\u2019s room',plain:'US\u2013China rivalry, tariffs and techno-nationalism put pressure on Europe to take sides.',why:'Less room for manoeuvre makes Europe a rule-taker.',historyAny:[/us-china|us\u2013china/,/techno-?nationalis/,/tariff/,/rivalry/],roles:[
        {label:'US\u2013China rivalry',claimType:'diagnosis',spec:{any:[/us.china/,/techno.?nationalis/,/strategic competition/]}},
        {label:'Tariff pressure',claimType:'effect',spec:{any:[/tariff/,/section 232/]}},
        {label:'Sanctions reach',claimType:'effect',spec:{any:[/secondary sanctions/,/extraterritorial/]}}
      ]},
      flip:'The balance changes if partnerships deliver concrete coordination, or if rivalry forces Europe into bloc choices.'
    },
    {
      id:'industrial_build_vs_hollowing',
      left:{title:'Europe is rebuilding strategic industry',plain:'Industrial policy, defence spending and European-preference rules are adding capacity in strategic sectors.',why:'Domestic capacity reduces reliance on imports in a crisis.',historyAny:[/industrial policy/,/manufacturing capacity/,/defen[cs]e industr/],roles:[
        {label:'Industrial policy',claimType:'action',spec:{any:[/industrial accelerator act/,/industrial policy/,/made in europe|european preference/]}},
        {label:'Defence production',claimType:'action',spec:{any:[/defen[cs]e (?:industr|production)/,/arms production/,/security action for europe|safe/]}},
        {label:'Critical medicines',claimType:'action',spec:{any:[/critical medicines/,/manufacturing critical medicines/]}}
      ]},
      right:{title:'Industry is under competitive pressure',plain:'High energy costs and subsidised competition from abroad squeeze European producers.',why:'Lost capacity is hard to rebuild and turns into new dependence.',historyAny:[/overcapacity/,/energy cost/,/deindustriali/],roles:[
        {label:'Overcapacity',claimType:'effect',spec:{any:[/overcapacity/,/dumping/,/subsidi[sz]ed/]}},
        {label:'Energy costs',claimType:'diagnosis',spec:{any:[/energy (?:costs|prices)/,/energy-intensive/]}},
        {label:'Plant closures',claimType:'effect',spec:{any:[/plant closure|job losses|deindustriali/]}}
      ]},
      flip:'The balance changes if new capacity is actually built and runs, or if closures outpace it.'
    },
    {
      id:'unity_vs_fragmentation',
      left:{title:'The EU is acting more as one',plain:'More economic-security decisions are coordinated at EU level with shared risk assessments.',why:'A united response is harder to coerce and splits less easily.',historyAny:[/member states/,/coordination/,/common/],roles:[
        {label:'Common rules',claimType:'action',spec:{any:[/mandatory .*screening|all member states/,/harmoni[sz]/,/eu-level/]}},
        {label:'Joint instruments',claimType:'action',spec:{any:[/joint procurement|joint purchas/,/security action for europe/,/european competitiveness fund/]}}
      ]},
      right:{title:'Member states still pull apart',plain:'National screening regimes, bilateral deals and unanimity rules keep responses fragmented.',why:'Division gives outside powers a way to split Europe.',historyAny:[/fragment/,/unanimity/,/bilateral/],roles:[
        {label:'National divergence',claimType:'diagnosis',spec:{any:[/national (?:regimes|screening)/,/fragment/,/divergen/]}},
        {label:'Unanimity limits',claimType:'diagnosis',spec:{any:[/unanimity/,/veto/]}}
      ]},
      flip:'The balance changes if EU-level tools are used in a real case, or if a member state blocks a common response.'
    },
  ];

  function plainTrendTitle(value){
    const t=clean(value);
    const exact={
      'Green technology gains momentum':'Green technology is expanding',
      'Rules and costs rein green technology in':'Rules and costs are constraining green technology',
      'Build more European computing capacity':'Europe is expanding computing capacity',
      'Power, supply and access constrain the build-out':'Power, supply and access are constraining computing expansion',
      'Fresh commitments for strategic investment':'Strategic investment is increasing',
      'Friction grows around strategic investment':'Barriers to strategic investment are growing',
      'Scaling up research security':'Research-security measures are expanding',
      'Research security gets harder to do':'Research-security requirements are becoming harder to implement',
      'Europe bets bigger on AI':'Europe is increasing investment in AI',
      'The bill for AI keeps rising':'AI costs and requirements are increasing',
      'Europe pushes materials advanced forward':'Europe is expanding advanced-materials capacity',
      'Materials advanced runs into limits':'Advanced materials face growing constraints',
      'Horizon access: the build-out accelerates':'Horizon access is expanding',
      'Horizon access: the fine print tightens':'Conditions on Horizon access are tightening',
      'Europe doubles down on venture capital':'European venture capital is expanding',
      'Second thoughts slow venture capital':'Europe still has a venture-capital gap',
      'Build more strategic autonomy':'Europe is building more strategic autonomy',
      'Dependencies keep setting the terms':'Strategic dependencies are limiting autonomy',
      'Open more research partnerships':'Europe is opening more research partnerships',
      'Put more conditions around collaboration':'Research collaboration faces tighter conditions',
      'Critical infrastructure resilience is on the rise':'Europe is strengthening critical-infrastructure resilience',
      'Critical infrastructure resilience meets resistance':'Preparedness gaps are slowing resilience efforts',
      'Opening the throttle on energy supply':'Energy-supply capacity is expanding',
      'Pulling the handbrake on energy supply':'New constraints are emerging around energy supply',
      'Expand research-system capacity':'Europe is expanding research-system capacity',
      'Capacity is being stretched or made conditional':'Research-system capacity is being stretched or made conditional',
      'More money and moves behind the defence industry':'Funding and activity are increasing in the defence industry',
      'New conditions pile up around the defence industry':'Conditions around the defence industry are tightening',
      'Push harder on innovation performance':'Europe is strengthening innovation performance',
      'Structural bottlenecks keep holding performance back':'Structural bottlenecks are holding innovation performance back'
    };
    if(exact[t])return exact[t];
    const rules=[
      [/^Europe pushes (.+) forward$/i,(_,x)=>`Europe expands ${x}`],
      [/^(.+) runs into limits$/i,(_,x)=>`${x} faces growing constraints`],
      [/^More money and moves behind (.+)$/i,(_,x)=>`Investment and activity increase in ${x}`],
      [/^New conditions pile up around (.+)$/i,(_,x)=>`Conditions around ${x} are tightening`],
      [/^(.+) gains momentum$/i,(_,x)=>`${x} is expanding`],
      [/^Rules and costs rein (.+) in$/i,(_,x)=>`Rules and costs are constraining ${x}`],
      [/^Scaling up (.+)$/i,(_,x)=>`${x} is expanding`],
      [/^(.+) gets harder to do$/i,(_,x)=>`Barriers to ${x} are increasing`],
      [/^Europe doubles down on (.+)$/i,(_,x)=>`Europe is increasing support for ${x}`],
      [/^Second thoughts slow (.+)$/i,(_,x)=>`Constraints are slowing ${x}`],
      [/^(.+): the build-out accelerates$/i,(_,x)=>`${x} is expanding`],
      [/^(.+): the fine print tightens$/i,(_,x)=>`Conditions around ${x} are tightening`],
      [/^Fresh commitments for (.+)$/i,(_,x)=>`New commitments strengthen ${x}`],
      [/^Friction grows around (.+)$/i,(_,x)=>`Barriers around ${x} are growing`],
      [/^(.+) is on the rise$/i,(_,x)=>`${x} is expanding`],
      [/^(.+) meets resistance$/i,(_,x)=>`Resistance to ${x} is growing`],
      [/^Opening the throttle on (.+)$/i,(_,x)=>`Activity is increasing in ${x}`],
      [/^Pulling the handbrake on (.+)$/i,(_,x)=>`Constraints are slowing ${x}`],
      [/^(.+) finds new backers$/i,(_,x)=>`Support is growing for ${x}`],
      [/^(.+) faces new hurdles$/i,(_,x)=>`Barriers to ${x} are growing`],
      [/^Europe bets bigger on (.+)$/i,(_,x)=>`Europe is investing more in ${x}`],
      [/^The bill for (.+) keeps rising$/i,(_,x)=>`Costs of ${x} are rising`],
      [/^(.+) spreads$/i,(_,x)=>`Use of ${x} is expanding`],
      [/^(.+) gets fenced in$/i,(_,x)=>`Restrictions on ${x} are increasing`]
    ];
    for(const [re,fn] of rules){const m=t.match(re);if(m)return fn(...m);}
    return t;
  }


  function trendHeadlineFromPlain(title,plain){
    const t=plainTrendTitle(title),p=clean(plain),l=low(p);
    // Headline must be a compact statement actually supported by the sentence below it.
    // These rules describe the development in the sentence; they never broaden it back
    // to the controlled object merely because that object was used for candidate discovery.
    const rules=[
      [/environmental biotechnology offers routes to cleaner production/,()=> 'Environmental biotechnology is opening cleaner production routes'],
      [/persistent gaps in batteries and solar supply chains/,()=> 'Europe still has gaps in batteries and solar supply chains'],
      [/eurohpc opened a competitive call.*ai gigafactor/,()=> 'Europe is moving to build AI Gigafactories'],
      [/data-centre geography changing in response to power and land constraints/,()=> 'Power and land constraints are reshaping AI data-centre locations'],
      [/subsidies helped compensate for germany.s cost disadvantages/,()=> 'Subsidies are supporting strategic investment despite Germany’s cost disadvantages'],
      [/selective conditionality is narrowly targeted.*limited leverage over foreign investors/,()=> 'EU investment conditionality remains limited'],
      [/belgian authorities opened a concrete semiconductor-espionage case/,()=> 'Belgium has opened a semiconductor-espionage case'],
      [/research security self-assessment appendix is a mandatory/,()=> 'Finland has made research-security self-assessment mandatory'],
      [/commission proposes a regulation.*cloud and ai ecosystem/,()=> 'The EU is proposing new rules for its cloud and AI ecosystem'],
      [/legal clarity is associated with deeper, not necessarily broader.*ai adoption/,()=> 'AI legal clarity may deepen adoption without broadening it'],
      [/advanced-materials effort must be less fragmented/,()=> 'Europe’s advanced-materials effort remains fragmented'],
      [/mature substitutes can cut gallium.*germanium.*palladium/,()=> 'Mature substitutes can reduce some critical-material dependencies'],
      [/horizon europe initiatives launched to improve access, financing and industry collaboration/,()=> 'EU initiatives are widening access to research infrastructure'],
      [/hungary.s continued exclusion from horizon europe grants/,()=> 'Hungary’s Horizon exclusion is constraining research capacity'],
      [/mistral closed a eur 3 billion round/,()=> 'Mistral’s €3 billion round is boosting European venture capital'],
      [/eu leads globally in scientific output but underperforms markedly in patenting, venture capital and scale-up/,()=> 'Europe still lags in venture capital and scale-up'],
      [/pursuing greater sovereign space capability/,()=> 'Europe is pursuing more sovereign space capability'],
      [/reducing strategic dependencies and adapting to those that persist/,()=> 'Strategic dependencies continue to limit European resilience'],
      [/council adopted the first eu framework for science diplomacy/,()=> 'The EU has adopted a framework for science diplomacy'],
      [/security and sovereignty measures do not collapse the openness needed for science/,()=> 'Security measures can constrain research openness'],
      [/spain proposed a stronger eu climate-resilience framework/,()=> 'Spain is pushing for stronger EU climate-resilience rules'],
      [/preparedness and integration into corporate strategy remain uneven/,()=> 'European firms remain unevenly prepared for geopolitical risks'],
      [/google announced a major new ai-compute investment and energy arrangement in finland/,()=> 'Google is expanding AI compute and energy investment in Finland'],
      [/finnish opposition parties proposed a national permitting framework for data centres/,()=> 'Finland is considering a national permitting framework for data centres'],
      [/international coalition for science, research and innovation in ukraine.*gdansk declaration/,()=> 'International partners are coordinating support for Ukraine’s research system'],
      [/irish preparedness confidence fell.*vulnerability profiles/,()=> 'Preparedness remains uneven across countries'],
      [/agile.*€?115 million programme.*development, testing and uptake/,()=> 'EU institutions are funding faster defence-technology development'],
      [/defence readiness by 2030 depends on collaborative procurement, shared training/,()=> 'European defence readiness still depends on coordinated procurement and training'],
      [/commission proposed new eu legislation aimed at strengthening the single market for innovation/,()=> 'The Commission is proposing new EU innovation legislation'],
      [/eu27 improves but remains behind the us, south korea and japan/,()=> 'EU innovation performance still trails major global peers']
    ];
    for(const [re,fn] of rules){if(re.test(l))return fn();}
    // Fail conservative: if a generic generated title appears to speak more broadly
    // than the displayed evidence sentence, use a compact first-clause headline instead.
    const generic=/\b(expand|expanding|constraint|constrain|slow|strengthen|tighten|support|barrier|capacity|investment|autonomy|performance|resilience|energy supply)\b/i;
    if(generic.test(t)){
      let h=p.replace(/^(new market data show|the evidence shows|sources show|analysis shows)\s+/i,'')
             .split(/[.;]/)[0].trim();
      const words=h.split(/\s+/);
      if(words.length>16)h=words.slice(0,16).join(' ')+'…';
      if(h)return h.charAt(0).toUpperCase()+h.slice(1).replace(/[.!?]+$/,'');
    }
    return t;
  }

  function highOrderPairs(data){
    const state=data?.high_order_inference&&typeof data.high_order_inference==='object'?data.high_order_inference:{};
    const ids=Array.isArray(state?.publications?.trend)?state.publications.trend:[];
    const map=new Map((Array.isArray(state?.candidates)?state.candidates:[]).filter(x=>x&&typeof x==='object').map(x=>[clean(x.id),x]));
    return ids.map(id=>map.get(clean(id))).filter(Boolean).map(c=>{
      const b=c.trend_balance||{},lp=Number(b.left_pull),rp=Number(b.right_pull);
      if(!Number.isFinite(lp)||!Number.isFinite(rp)||Math.round(lp+rp)!==100)return null;
      const support=Array.isArray(c.support)?c.support:[];
      const leftRole=clean(b.left_role||'Concentrating action');
      const rightRole=clean(b.right_role||'Spreading action');
      const leftEvidence=support.filter(x=>clean(x?.role).startsWith(leftRole)).map(x=>({row:x}));
      const rightEvidence=support.filter(x=>clean(x?.role).startsWith(rightRole)).map(x=>({row:x}));
      if(leftEvidence.length<1||rightEvidence.length<1)return null;
      return {id:c.id,emergent:true,family:clean(b.family),objectKey:clean(b.object_key),support:Number(c.score)||0,
        left:{title:trendHeadlineFromPlain(b.left_title||'Pull A',b.left_plain||c.reader_summary||''),plain:clean(b.left_plain||c.reader_summary||''),why:'',pull:Math.round(lp),evidence:leftEvidence,history:[],sourceCount:Number(b.left_sources)||0},
        right:{title:trendHeadlineFromPlain(b.right_title||'Pull B',b.right_plain||c.reader_summary||''),plain:clean(b.right_plain||c.reader_summary||''),why:'',pull:Math.round(rp),evidence:rightEvidence,history:[],sourceCount:Number(b.right_sources)||0},
        pullRange:{left:b.left_range||[],right:b.right_range||[]},
        composition:clean(b.composition||''),flip:clean(b.flip_line||''),label:clean(b.label||''),
        actionStats:{leftActions:Number(b.left_actions)||0,rightActions:Number(b.right_actions)||0,leftSources:Number(b.left_sources)||0,rightSources:Number(b.right_sources)||0,rawLeft:Number(b.raw_left_pull),rawRight:Number(b.raw_right_pull)},
        currentEvidenceCount:Number(c.primary_records)||0,historicalContextCount:0};
    }).filter(Boolean);
  }

  function build(data,history){
    const state=data?.high_order_inference&&typeof data.high_order_inference==='object'?data.high_order_inference:{};
    if(state?.detector_backend==='claim_native'&&Number(state?.selection_stage||0)>=7){
      // Stage 7 already publishes the deliberate wow-cycle order (5,4,3,2,1 x3).
      // Do not re-sort the shelf in the browser.
      return highOrderPairs(data);
    }
    const currentRows=currentCorpus(data),historicalRows=historicalCorpus(history),out=[];
    for(const pair of PAIRS){
      const left=sideEvidence(currentRows,historicalRows,pair.left),right=sideEvidence(currentRows,historicalRows,pair.right);
      if(!sideQualifies(left)||!sideQualifies(right))continue;
      if(left.evidence.length+right.evidence.length<6)continue;
      const total=left.raw+right.raw;if(total<=0)continue;
      let leftPull=Math.round(100*left.raw/total);leftPull=Math.max(18,Math.min(82,leftPull));
      const rightPull=100-leftPull;
      // The score is deliberately a playful balance meter, not a probability estimate.
      const support=Math.round((left.averageQuality+right.averageQuality)/2+Math.min(10,left.sourceCount+right.sourceCount)+Math.min(4,left.history.length+right.history.length));
      out.push({...pair,left:{...pair.left,...left,pull:leftPull},right:{...pair.right,...right,pull:rightPull},support,currentEvidenceCount:left.evidence.length+right.evidence.length,historicalContextCount:left.history.length+right.history.length});
    }
    const semanticDuplicate=(x)=>{
      if(x.family==='open_protect'&&x.objectKey==='openness')return out.some(y=>y.id==='open_vs_secure');
      if(x.family==='attract_friction'&&x.objectKey==='talent')return out.some(y=>y.id==='talent_pull_vs_talent_friction');
      if(x.family==='capacity_access'&&x.objectKey==='infrastructure')return out.some(y=>y.id==='infrastructure_vs_bottlenecks');
      return false;
    };
    for(const x of highOrderPairs(data))if(!out.some(y=>y.id===x.id)&&!semanticDuplicate(x))out.push(x);
    return out.sort((a,b)=>b.support-a.support||Math.abs(50-a.left.pull)-Math.abs(50-b.left.pull)||a.id.localeCompare(b.id));
  }
  function stats(data,history){
    const hs=historicalCorpus(history);
    return {
      current:currentCorpus(data).length,historical:hs.length,
      historicalAuthoritative:hs.filter(x=>x?.historical_reasoning_status==='authoritative').length,
      historicalCautious:hs.filter(x=>x?.historical_reasoning_status&&x.historical_reasoning_status!=='authoritative').length,
      historicalExcluded:Number(history?.reasoning_stats?.not_retained)||0
    };
  }
  return {build,stats,pairs:PAIRS,reportingRole,quality,rowText,sideQualifies};
});
