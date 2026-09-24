(function(root){
'use strict';
const TERMS=[
[
"Anti-Coercion Instrument",
"EU tools",
"The EU regulation (in force since December 2023) that lets the Union respond collectively when a third country uses economic pressure to force a policy change.",
"It is Europe’s main deterrent against coercion; its value depends on how fast and united its use would be."
],
[
"Chokepoint",
"Dependencies",
"A concentrated supplier, route, technology or infrastructure that many depend on and that is hard to replace quickly.",
"Whoever controls a chokepoint can gain leverage over European industry."
],
[
"Critical infrastructure",
"Security",
"Infrastructure whose disruption would seriously affect essential services or the economy: grids, pipelines, ports, cables, telecoms.",
"Ownership, vendors and physical security of these links are economic-security questions."
],
[
"Critical raw materials",
"Supply chains",
"Materials that are economically important and exposed to significant supply risk, such as rare earths, gallium or graphite.",
"Much of their mining and especially processing is concentrated in a few countries."
],
[
"De-risking",
"Strategy",
"Reducing risky dependencies and exposures without cutting economic ties altogether.",
"It is the EU’s chosen middle way between openness and decoupling."
],
[
"Decoupling",
"Strategy",
"Deliberately separating economies, supply chains or technology ecosystems.",
"Most European policy rejects full decoupling as too costly, but it can happen sector by sector."
],
[
"Dual-use",
"Technology security",
"Goods, software or technology that can serve civilian as well as military purposes.",
"Dual-use items are subject to EU export controls."
],
[
"Economic coercion",
"Coercion",
"Using trade, investment or other economic measures to pressure a country into changing its policy.",
"Europe has faced it directly and built the anti-coercion instrument in response."
],
[
"Economic security",
"Strategy",
"Protecting an economy’s resilience, supply, technology and infrastructure against risks from geopolitical rivalry, while keeping it open.",
"The EU set out its approach in a 2023 strategy and strengthened it in a December 2025 communication."
],
[
"Export controls",
"Technology security",
"Rules that require permission to export certain goods or technologies, especially dual-use items.",
"They can protect technology but also cost sales and partners if applied unilaterally."
],
[
"FDI screening",
"Investment",
"Review of foreign direct investment on security or public-order grounds, with the power to set conditions or block deals.",
"A revised EU regulation adopted in June 2026 makes screening mandatory in every member state."
],
[
"Foreign Subsidies Regulation",
"EU tools",
"EU rules that let the Commission investigate subsidies from non-EU governments that distort the single market.",
"It targets subsidised takeovers and public-procurement bids."
],
[
"Friendshoring",
"Supply chains",
"Moving supply chains towards countries seen as reliable partners.",
"It reduces some risks but can raise costs and create new concentrations."
],
[
"Geoeconomic fragmentation",
"Trade",
"The splitting of trade and investment into rival blocs.",
"It raises costs and narrows options for an open economy like Europe’s."
],
[
"Like-minded partners",
"Partnerships",
"Countries that share key interests and rules and can coordinate on economic security.",
"Partnerships are one of the three pillars of the EU approach: promote, protect, partner."
],
[
"Open strategic autonomy",
"Strategy",
"The EU’s aim to act on its own interests while remaining open to trade and cooperation.",
"It frames the dilemma between protection and openness."
],
[
"Outbound investment",
"Investment",
"European investment in other countries, especially in sensitive technologies.",
"The EU is examining whether to monitor or restrict it in areas such as chips, AI and quantum."
],
[
"Overcapacity",
"Trade",
"Production far beyond domestic demand, often supported by subsidies, that spills into export markets.",
"It can undercut European producers faster than trade defence can respond."
],
[
"Secondary sanctions",
"Sanctions",
"Sanctions that penalise third-country firms for dealing with a sanctioned target.",
"They can reach European firms through finance and supply chains regardless of EU policy."
],
[
"Strategic dependency",
"Dependencies",
"Reliance on a few external suppliers for something important and hard to substitute.",
"The EU tracks strategic dependencies to decide where diversification is needed."
],
[
"Trade defence",
"Trade",
"Anti-dumping, anti-subsidy and safeguard measures against unfair or damaging imports.",
"They protect industry but can raise prices and invite retaliation."
],
[
"Weaponised interdependence",
"Coercion",
"Using control over networks or chokepoints that others depend on as leverage.",
"It explains why ordinary economic ties can become security risks."
]
];
const byTerm=new Map(TERMS.map(x=>[x.term.toLowerCase(),x]));
const aliasRows=ALIASES.map(([alias,term])=>({alias,term:byTerm.get(term.toLowerCase())})).filter(x=>x.term).sort((a,b)=>b.alias.length-a.alias.length);
const esc=s=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
function slug(s){return String(s||'').toLowerCase().replace(/&/g,'and').replace(/[^a-z0-9]+/g,'-').replace(/^-|-$/g,'')}
function lookup(name){return byTerm.get(String(name||'').toLowerCase())||null}
function find(text,max=4){
  const s=String(text||''), lower=s.toLowerCase(), hits=[], seen=new Set();
  for(const row of aliasRows){
    if(seen.has(row.term.term))continue;
    let from=0;
    while(true){
      const i=lower.indexOf(row.alias,from); if(i<0)break;
      const before=i?lower[i-1]:'', after=lower[i+row.alias.length]||'';
      const okBefore=!before||!/[_a-z0-9]/.test(before), okAfter=!after||!/[_a-z0-9]/.test(after);
      if(okBefore&&okAfter){hits.push({index:i,length:row.alias.length,term:row.term});seen.add(row.term.term);break}
      from=i+row.alias.length;
    }
  }
  return hits.sort((a,b)=>a.index-b.index).slice(0,Math.max(0,max));
}
function annotate(text,max=4){
  const s=String(text||''), hits=find(s,max); if(!hits.length)return esc(s);
  let out='',pos=0;
  for(const h of hits){
    if(h.index<pos)continue;
    out+=esc(s.slice(pos,h.index));
    const shown=s.slice(h.index,h.index+h.length);
    out+=`<span class="glossary-inline" title="${esc(h.term.meaning)}" data-glossary="${esc(h.term.term)}">${esc(shown)}</span>`;
    pos=h.index+h.length;
  }
  return out+esc(s.slice(pos));
}
function simpleDefinitions(text,max=3){return find(text,max).map(h=>h.term)}
root.RadarGlossary={terms:TERMS,lookup,slug,find,simpleDefinitions,annotate};
})(typeof globalThis!=='undefined'?globalThis:this);
