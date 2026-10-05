/* Reader clarity layer for the derived analytical pages only.
   Presentation-only: it never mutates radar.json, findings, scores, evidence,
   inference objects, selection, updating, or any reasoning state.

   The job here is narrower than Reader Language: when a derived card is technically
   correct but assumes the reader knows an unnamed agreement, a machine object label,
   or a research-paper construction, use the evidence already attached to that card to
   make the displayed point self-contained.
*/
(function(g){
'use strict';

const clean=v=>String(v??'').replace(/\s+/g,' ').trim();
const low=v=>clean(v).toLowerCase();
const sentence=v=>{const s=clean(v);return s&&!/[.!?]$/.test(s)?`${s}.`:s};
const cap=v=>clean(v).replace(/^([^A-Za-zÀ-ÖØ-öø-ÿ]*)([a-zà-öø-ÿ])/,(_,a,b)=>a+b.toUpperCase());

function evidenceRows(v){
  const rows=[];
  const add=x=>{if(!x)return;const r=x.row||x;if(r&&typeof r==='object')rows.push(r)};
  if(Array.isArray(v))v.forEach(add);
  else if(v&&typeof v==='object'){
    for(const key of ['evidence','support','history','currentEvidence','historicalEvidence','against']){
      if(Array.isArray(v[key]))v[key].forEach(add);
    }
  }
  return rows;
}
function evidenceText(v){
  return evidenceRows(v).map(r=>clean([r.title,r.headline,r.source_statement,r.sourceStatement,r.core_message,r.summary,r.evidence_contribution,r.contribution].filter(Boolean).join(' '))).join(' ');
}

const OBJECTS={
  'wto compatibility':'WTO compatibility',
  'european preference':'Buy-European preferences',
  'export controls':'export controls',
  'supply chains':'supply chains',
  'energy supply':'energy supply',
  'critical infrastructure resilience':'critical-infrastructure resilience',
  'foreign ownership':'foreign ownership',
  'strategic investment':'strategic investment',
  'coercion and sanctions':'sanctions and economic coercion',
  'payment infrastructure':'European payment infrastructure',
  'like minded coordination':'coordination with like-minded partners',
  'critical raw materials':'critical raw materials',
  'trade market access':'EU market access',
  'trade eu countermeasures':'EU trade countermeasures',
  'export control dual use list':'the EU dual-use export-control list',
  'trade agreement':'trade agreements',
  'energy grid':'European energy grids',
  'materials processing capacity':'European materials-processing capacity',
  'european drone capability':'European drone capability',
  'strategic investment finance':'strategic investment finance',
  'critical raw material supply':'critical-raw-material supply',
  'critical materials as a whole':'critical materials',
  'trade as a whole':'trade policy',
  'energy supply as a whole':'energy supply',
  'finance and payments as a whole':'finance and payments',
  'the defence industry as a whole':'the defence industry',
  'strategic dependencies as a whole':'strategic dependencies',
  'econsec strategy':'economic-security strategy',
  'econsec toolbox coordination':'coordination of economic-security tools',
  'trade eu countermeasures':'EU trade countermeasures',
  'energy gas supply':'gas supply',
  'sanctions package':'sanctions',
  'trade agreement':'trade agreements'
};
function lowerFirst(v){const s=clean(v);if(/^[A-Z]{2,}\b/.test(s))return s;return s?s.charAt(0).toLowerCase()+s.slice(1):s;}
function friendlyObject(v){
  let s=low(v).replace(/^the\s+/,'').replace(/\s+as a whole$/,'').trim();
  if(OBJECTS[s])return OBJECTS[s];
  s=s.replace(/\beconsec\b/g,'economic security')
     .replace(/\beu\b/g,'EU')
     .replace(/\bwto\b/g,'WTO')
     .replace(/\bai\b/g,'AI')
     .replace(/\bdual use\b/g,'dual-use')
     .replace(/\bexport control\b/g,'export-control');
  return s;
}

function sourceContextForAgreement(side){
  const t=evidenceText(side);
  if(/wto waiver permitting autonomous trade preferences to the western balkans/i.test(t)){
    return {
      title:'The EU is seeking to keep preferential trade treatment for the Western Balkans compatible with WTO rules',
      what:'The underlying EU proposal asks the WTO to extend the waiver that permits autonomous EU trade preferences for the Western Balkans.',
      why:'Without that waiver, the same preferential treatment could have to be extended to other WTO members.'
    };
  }
  return null;
}

function trendSide(side){
  const rawTitle=clean(side?.title),rawWhat=clean(side?.plain||side?.what),rawWhy=clean(side?.why);
  const all=low([rawTitle,rawWhat,evidenceText(side)].join(' '));
  let title=rawTitle,what=rawWhat,why=rawWhy;

  if(/the eu is a party to the agreement/.test(all)){
    const c=sourceContextForAgreement(side);if(c)return c;
  }
  if(/weather variability changes the modelled cost balance between domestic european hydrogen production and imports/.test(all)){
    title='Weather can shift the cost advantage between European and imported hydrogen';
    what='Weather conditions can change whether producing hydrogen in Europe or importing it is the cheaper option.';
    why='The preferred supply mix therefore depends partly on weather assumptions, not only on average production costs.';
    return {title,what,why};
  }
  if(/the article (?:assesses|examines) how cbam verification and mutual recognition can reduce trade frictions/.test(all)){
    title='CBAM compliance could become easier where verification systems are mutually recognised';
    what='Mutual recognition of carbon-verification systems can reduce trade friction while preserving the credibility of the EU carbon-border system.';
    return {title,what,why};
  }
  if(/2026 update of the eu control list of dual-use items/.test(all)){
    title='The EU is updating the list of dual-use items subject to export controls';
    what='The 2026 control-list update changes which civilian and defence-related goods and technologies fall under EU export controls.';
    return {title,what,why};
  }
  if(/^the article (?:assesses|examines|finds|shows) how /i.test(rawWhat)){
    what=cap(rawWhat.replace(/^the article (?:assesses|examines|finds|shows) how /i,''));
  }
  if(/^the (?:study|paper|report|analysis) (?:finds|shows|argues|examines|assesses) /i.test(rawWhat)){
    what=cap(rawWhat.replace(/^the (?:study|paper|report|analysis) (?:finds|shows|argues|examines|assesses) /i,''));
  }
  // Machine object labels are useful internally but poor standalone headings.
  if(/^Supply chains is expanding$/i.test(rawTitle)&&/multinationals report using diversification/i.test(rawWhat))
    title='European firms are diversifying supply chains to manage geopolitical risk';
  let m=rawTitle.match(/^Europe expands (.+)$/i);
  if(m)title=`Europe is expanding ${friendlyObject(m[1])}`;
  m=rawTitle.match(/^Constraints on (.+) are growing$/i);
  if(m)title=`Constraints on ${friendlyObject(m[1])} are growing`;
  m=rawTitle.match(/^Investment and activity increase in (.+)$/i);
  if(m)title=`Activity supporting ${friendlyObject(m[1])} is increasing`;
  m=rawTitle.match(/^Conditions around (.+) are tightening$/i);
  if(m)title=`Conditions around ${friendlyObject(m[1])} are tightening`;
  m=rawTitle.match(/^(.+) is gaining support$/i);
  if(m)title=`Support for ${friendlyObject(m[1])} is growing`;
  m=rawTitle.match(/^Costs and constraints are limiting (.+)$/i);
  if(m)title=`Costs and constraints are limiting ${friendlyObject(m[1])}`;
  return {title:sentence(title).replace(/[.]$/,''),what:sentence(what),why:sentence(why)};
}

function phenomenon(item,text,explanation){
  let title=clean(text),why=clean(explanation);
  let m=title.match(/^(.+?) as a whole keeps returning across the research-policy cycle\.?$/i);
  if(m){const obj=cap(friendlyObject(m[1]));const plural=/s$|materials|payments|sanctions|dependencies|countermeasures/i.test(obj);title=`${obj} ${plural?'keep':'keeps'} reappearing in European economic-security policy.`;}
  m=title.match(/^(.+?) keeps returning across the research-policy cycle\.?$/i);
  if(m){const obj=cap(friendlyObject(m[1]));const plural=/s$|materials|payments|sanctions|dependencies|countermeasures/i.test(obj);title=`${obj} ${plural?'keep':'keeps'} reappearing in European economic-security policy.`;}
  if(/^Strategic autonomy keeps spreading through research and technology policy\.?$/i.test(title))
    title='Strategic autonomy is becoming a recurring concern in research and technology policy.';
  if(!why){
    const t=low(title);
    if(/trade policy|trade agreement/.test(t))why='Trade policy keeps linking market access, supply security and Europe’s room to act internationally.';
    else if(/critical material/.test(t))why='European technology and industry remain exposed when essential materials have few fast substitutes.';
    else if(/energy supply|gas supply/.test(t))why='Supply diversification matters because energy disruptions can quickly spill into industrial costs and strategic capacity.';
    else if(/payment/.test(t))why='Payment infrastructure affects how dependent European transactions are on providers and rules outside Europe.';
  }
  return {title:sentence(title),explanation:sentence(why)};
}

function priority(item,kind,title,explanation){
  let t=clean(title),e=clean(explanation);
  const topic=friendlyObject(item?.topicLabel||'');
  let m;
  if((m=t.match(/^(.+?) is moving into practice before the rulebook catches up\.?$/i))){
    const obj=cap(friendlyObject(m[1]));
    t=`Europe is acting on ${lowerFirst(obj)} before the rules are settled.`;
    e='If practice becomes established first, later rules may have to adapt to what is already being done rather than shape it from the start.';
  }
  if((m=t.match(/^(.+?) could become more conditional\.?$/i))){
    const obj=friendlyObject(m[1]);
    t=obj==='EU market access'?'Access to the EU market could come with more conditions.':`Access to ${obj} could come with more conditions.`;
    e='The current evidence points to additional conditions on access or participation, which could make the route harder to use.';
  }
  if(/^New instruments could move European drone capability further into operation\.?$/i.test(t)){
    t='Existing European programmes could turn drone plans into deployed capability.';
    e='Funding and cooperation routes already exist; continued implementation could convert them into more usable European capability.';
  }
  if(/^New funding could expand strategic investment finance\.?$/i.test(t)){
    t='New funding could widen Europe’s strategic-investment capacity.';
    e='A live funding route could give more strategic projects a European source of finance if implementation continues.';
  }
  if(/^Trade agreement could become the missing route into critical raw-material supply\.?$/i.test(t)){
    t='A trade agreement could help secure critical-raw-material supplies through structures Europe already has.';
    e='The opportunity is to connect an existing trade route to a known supply need instead of building a new mechanism from scratch.';
  }
  if(/^New investment could expand energy grid\.?$/i.test(t)){
    t='New investment could expand European grid capacity.';
    e='More grid capacity can make additional energy supply usable and reduce infrastructure bottlenecks if projects are delivered.';
  }
  if(topic&&/^(?:Evidence-backed finding|A live European instrument)/i.test(t))t=cap(topic)+'.';
  return {title:sentence(t),explanation:sentence(e)};
}

function shock(item,title,explanation){
  let t=clean(title),e=clean(explanation);
  // For rhetorical or metaphorical shock titles, the consequence underneath is usually
  // the clearest statement of the actual shock. Promote that consequence to the surface.
  if(/^What if /i.test(t)&&e)t=cap(e);
  if(/licence stamped abroad/i.test(t))t='Foreign export controls could block equipment or components needed for European materials processing.';
  if(/one new export list could leave european drone capability without its parts/i.test(t))t='A foreign export-control change could cut European drone programmes off from critical parts.';
  if(/payments blocked, partners gone/i.test(t))t='Sanctions could freeze funding and partnerships for European materials-processing projects.';
  if(/wider conflict could pull people and money away/i.test(t))t='A wider conflict could divert people, funding and supply routes away from European drone programmes.';
  if(/heatwave or outbreak could close the doors/i.test(t))t='Extreme weather or a public-health emergency could halt European materials-processing work.';
  if(/if fighting spreads, the routes/i.test(t))t='A wider conflict could close routes European materials processing depends on.';
  if(e&&low(t)===low(e))e='';
  return {title:sentence(t),explanation:sentence(e)};
}

function scenarioCopy(){
  return {
    kicker:'Possible Europes in 2035',
    title:'Four ways Europe’s economic position could develop by 2035',
    lede:'The four main scenarios differ on two big uncertainties: how connected the world economy remains, and how much strategic capacity Europe can build for itself. Open a scenario to see what current Radar evidence could mean inside that world.',
    note:'The two main uncertainties stay fixed so the four worlds remain comparable over time. Inside each world, the second set of uncertainties changes with the current Radar.'
  };
}

function subScenarioIntro(frame){
  const x=clean(frame?.x_axis?.title),y=clean(frame?.y_axis?.title);
  return `Inside this 2035 world, the current Radar points to two further uncertainties: ${x} and ${y}. These can change as the evidence changes.`;
}

function tradeoffLabel(v){return clean(v)?`The central tension in this world: ${clean(v)}`:''}

function branchesIntro(){
  return 'Each sub-scenario is then tested against four different developments drawn from current Radar evidence: a shock, an opportunity, a trend or a risk. The branches do not change the scenario; they show how the same world could play out differently.';
}

g.RadarReaderClarity={trendSide,phenomenon,priority,shock,scenarioCopy,subScenarioIntro,tradeoffLabel,branchesIntro,friendlyObject,evidenceText};
})(globalThis);
