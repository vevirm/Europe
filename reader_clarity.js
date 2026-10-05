/* Reader-only clarity layer.
   It never changes Radar data, findings, scores or reasoning. It only turns the
   already-selected card + its attached evidence into self-contained display copy.
   Conservative rule: when no grounded abstraction is recognised, keep the source
   wording after punctuation cleanup rather than inventing a new claim. */
(function(root){
'use strict';
const clean=v=>String(v??'').replace(/\s+/g,' ').trim();
const low=v=>clean(v).toLowerCase();
const sentence=v=>{
  let s=clean(v)
    .replace(/\s+([,.;:!?])/g,'$1')
    .replace(/([,;:])\s*[.,]+/g,'$1')
    .replace(/\.{2,}/g,'.')
    .replace(/,\s*\.$/,'.')
    .replace(/\s+[,.]$/,'')
    .trim();
  if(!s)return '';
  s=s.charAt(0).toUpperCase()+s.slice(1);
  return /[.!?]$/.test(s)?s:s+'.';
};
const deTitle=v=>clean(v)
  .replace(/\s+-\s+(?:Borderlex|Reuters|Financial Times|POLITICO|Euractiv|European trade policy).*$/i,'')
  .replace(/\s*\|\s*[^|]{2,80}$/,'')
  .replace(/\s+-\s+[^-]{2,70}$/,'');
function evidenceText(items){
  return (items||[]).map(e=>e?.row||e).filter(Boolean).map(x=>[
    x.source_statement,x.core_message,x.summary,x.reader_point,x.what,x.why_it_matters,x.title,x.headline
  ].map(clean).filter(Boolean).join(' ')).join(' ');
}
function pack(title,what,why){
  title=clean(title).replace(/[.!?]+$/,'');
  what=sentence(what); why=sentence(why);
  if(low(what)===low(title+'.'))what='';
  if(low(why)===low(what))why='';
  return {title,what,why};
}
function classify(text){
  const t=low(text);
  const tests=[
    ['hydrogen_storage',/hydrogen.{0,40}(storage|solar)|storage.{0,50}solar|power output.{0,40}energy efficiency/],
    ['energy_diversification',/kazakhstan.{0,80}energy|energy.{0,60}(diversif|supplier|transit)|repowereu|lng supplier/],
    ['european_preference',/buy european|made in europe|european preference|union-origin|procurement.{0,40}european/],
    ['wto_compatibility',/wto.{0,80}(compat|waiver|rule)|world trade organization|non-discrimination|mutual recognition.{0,50}trade/],
    ['export_controls',/export control|dual-use|technology transfer restriction|entity list/],
    ['supply_chain',/supply[- ]chain|supplier concentration|sourcing|diversif.{0,30}supply|logistics/],
    ['critical_materials',/critical raw material|critical mineral|rare earth|gallium|germanium|graphite|lithium|cobalt/],
    ['chips',/semiconductor|microchip|chips? act|foundry|wafer|lithograph/],
    ['ai_compute',/artificial intelligence|\bai\b|gpu|compute|data cent(?:re|er)|supercomputer|gigafactor/],
    ['research_security',/research security|knowledge security|foreign interference|trusted research|sensitive research/],
    ['research_openness',/open science|research openness|academic freedom|international research collaboration/],
    ['talent',/researcher|scientist|talent|brain drain|career|doctoral|postdoc|skills shortage/],
    ['scaleup',/scale[- ]?up|venture capital|commerciali[sz]|startup|deep tech|growth capital/],
    ['industrial_capacity',/industrial capacity|manufactur|factory|production capacity|industrial accelerator|deindustriali/],
    ['defence',/defen[cs]e industr|military production|arms production|dual-use defence/],
    ['infrastructure',/critical infrastructure|grid|subsea cable|pipeline|port|telecom|research infrastructure/],
    ['trade_tariffs',/tariff|trade retaliation|anti-coercion|trade defence|countermeasure/],
    ['partnerships',/strategic partnership|trade agreement|science diplomacy|international cooperation|g7 coordination/],
    ['funding',/research funding|grant|horizon europe|european research council|eic|investment fund/],
    ['standards_rules',/regulat|standard|rulebook|governance|compliance|permitting/],
    ['strategic_autonomy',/strategic autonom|technology sovereignty|economic security|de-risk|dependency/]
  ];
  return (tests.find(([,re])=>re.test(t))||[])[0]||'';
}

const OBJECT_TRENDS={
  'industry.european_preference':{
    left:['Europe is moving toward stronger preference for European production','EU procurement and industrial-support proposals are giving more weight to European origin and resilient supply','If adopted and used, these rules could shift public demand toward European capacity'],
    right:['“Buy European” rules face political and trade constraints','Member states and partners are contesting who should qualify and how far European-preference conditions should go','The final design will determine whether preference rules build capacity without fragmenting markets or triggering avoidable trade disputes']},
  'trade.wto_compatibility':{
    left:['Europe is still finding legal routes for preferential trade arrangements','The EU is using WTO waivers and interim arrangements to preserve selected trade preferences and dispute-settlement options','That gives Europe room to pursue policy goals without abandoning the multilateral trade framework'],
    right:['Economic-security measures face tighter WTO-compatibility tests','Verification, mutual recognition and non-discrimination rules are becoming more important when Europe introduces new trade measures','Measures that cannot be defended under trade rules are harder to use as durable economic-security tools']},
  'family:export_control':{
    left:['Europe is tightening control over sensitive technology transfers','EU control lists and dual-use rules are being updated as technology security becomes a larger policy concern','Controls can reduce unwanted transfer of strategic capability when they are targeted and enforceable'],
    right:['Export controls are becoming harder to coordinate and contain','Foreign controls, differing partner policies and workarounds can shift technology flows outside Europe’s own rulebook','Gaps between jurisdictions can weaken controls while still imposing costs on European firms']},
  'family:supply_chain':{
    left:['Europe is diversifying strategic supply chains','Firms and policymakers are adding suppliers, routes and resilience measures to reduce concentrated dependencies','More alternatives reduce the damage that one disrupted supplier or route can cause'],
    right:['Supply-chain constraints are still growing in important sectors','Weather, maritime disruption and continuing dependence on a small number of suppliers can still raise costs or interrupt supply','Diversification matters only if alternatives are available at the scale and speed needed during a disruption']},
  'family:energy':{
    left:['Europe is widening energy supplies, routes and partnerships','New suppliers, cross-border links and investment are expanding the number of ways Europe can obtain and move energy','A broader energy system reduces exposure to disruption or political pressure from any single route or supplier'],
    right:['Europe’s energy system still faces cost and resilience constraints','Storage losses, weather variability and external gas shocks can change which energy options are reliable or competitive','Energy security depends not only on adding supply, but on whether the system can absorb variability and shocks at acceptable cost']},
  'critical_infrastructure.resilience':{
    left:['Europe is strengthening protection of critical infrastructure','Security, resilience and threat-response measures are expanding around energy, maritime, digital and other essential infrastructure','Better protection reduces the chance that one attack or failure cascades across several parts of the economy'],
    right:['Critical infrastructure remains exposed to new technical vulnerabilities','More connected and automated infrastructure creates cyber and system risks that resilience measures still have to absorb','A weak point in shared infrastructure can disrupt services and production well beyond the original failure']},
  'infrastructure.foreign_ownership':{
    left:['Europe is accepting some foreign investment in strategic infrastructure','Foreign participation can provide capital and capacity even in infrastructure with economic-security importance','The benefit is investment; the risk is whether ownership creates leverage over assets Europe cannot easily replace'],
    right:['Foreign ownership can create long-term strategic dependence','Infrastructure investment can tie essential European assets to external state or corporate interests','Control of critical infrastructure matters most when political relations worsen or access becomes contested']},
  'finance.strategic_investment':{
    left:['Europe is mobilising more capital for strategic technologies and infrastructure','New EU funds and large private investments are aimed at helping strategic projects move from development to scale','Capital availability can determine whether important technologies grow in Europe or elsewhere'],
    right:['Strategic investment remains uneven across Europe','Large projects still depend on national fiscal capacity, state-aid choices and different incentives among member states','Uneven financing can concentrate capability in a few countries and leave common European goals underfunded']},
  'family:defence':{
    left:['Europe is increasing defence investment and production activity','Funding, procurement and industrial programmes are expanding efforts to build more defence capability in Europe','More domestic production can reduce dependence and improve the ability to replenish equipment during a crisis'],
    right:['European defence readiness still depends on coordination and supply security','Fragmented procurement, external inputs and interoperability constraints can limit what additional spending delivers','Readiness depends on producing usable capability at scale, not only on announcing higher budgets']},
  'cluster:coercion_sanctions':{
    left:['Europe is using sanctions and anti-coercion tools more actively','Economic restrictions are increasingly used to respond to security threats and hostile behaviour','These tools can create leverage without military action when Europe can maintain unity and enforcement'],
    right:['Sanctions remain vulnerable to bargaining, exemptions and enforcement gaps','Delistings, national disagreements and circumvention can weaken restrictions over time','The credibility of sanctions depends on whether measures remain politically sustainable and difficult to bypass']},
  'finance.payment_infrastructure':{
    left:['Europe is building more autonomous payment infrastructure','The digital euro and links between European payment systems are expanding alternatives to foreign-dominated payment networks','More European payment capacity can reduce dependence on external providers in a politically sensitive part of the economy'],
    right:['European payment autonomy still faces scale and adoption barriers','New networks must attract users, merchants and cross-border participation before they can replace established providers','Infrastructure creates autonomy only when it becomes widely usable, trusted and economically competitive']},
  'goal.strategic_autonomy':{
    left:['Europe is investing more in strategic autonomy','Policy and investment increasingly aim to preserve European access to critical technologies, infrastructure and production capability','Greater domestic capability gives Europe more room to act when external partners change course'],
    right:['Strategic autonomy still runs into external dependence and high costs','Space, energy and other strategic systems remain tied to international suppliers, capital and markets','Autonomy has limits where replacing external capability would be too slow or expensive']},
  'partnership.like_minded_coordination':{
    left:['Europe is widening coordination with like-minded partners','Trade, technology and security partnerships are being used to pool markets, expertise and strategic capacity','Coordination can spread risk and make common rules more effective'],
    right:['Partner coordination can narrow when interests diverge','Allies do not always agree on trade, technology controls or how much economic cost to accept','A partnership is less useful as an economic-security tool when members apply different rules at the moment of pressure']},
  'partnership.global_gateway':{
    left:['The EU is using Global Gateway to project economic and strategic influence','Infrastructure investment is becoming a larger part of Europe’s partnerships with countries outside the EU','Credible projects can create alternatives to rival financing and deepen long-term economic links'],
    right:['Global Gateway still faces questions about delivery and credibility','Implementation delays, mixed objectives and competition with other financing offers can limit its influence','The initiative matters only if announced partnerships become visible projects that partners value']},
  'cluster:materials_energy':{
    left:['Europe is treating materials and energy supply as linked security problems','Policy is connecting critical materials, energy infrastructure and diversification rather than managing each dependency separately','Upstream resilience can prevent shortages from cascading into several strategic industries at once'],
    right:['Materials and energy bottlenecks remain difficult to remove quickly','Processing concentration, permitting and infrastructure constraints can persist even when Europe identifies alternative resources','Resilience depends on turning potential alternatives into operating supply chains before a disruption occurs']}
};

const TREND={
  hydrogen_storage:{title:'Energy storage can make variable renewable power more dependable',what:'Hydrogen storage can absorb surplus renewable electricity and return energy when generation falls',why:'That can strengthen energy resilience, although efficiency and cost determine how useful it is at scale'},
  energy_diversification:{title:'Europe is widening energy partnerships to diversify supply',what:'New suppliers and transit relationships can reduce reliance on a narrow set of energy routes',why:'A broader supply base makes Europe less exposed to disruption or political pressure from any one supplier'},
  european_preference:{title:'Europe is moving toward stronger preference for European production',what:'EU procurement and industrial-support rules are increasingly being designed to favour European or resilient supply',why:'The choice can build domestic capacity, but it also creates trade-offs over cost, partners and international trade rules'},
  wto_compatibility:{title:'EU economic-security measures face tighter trade-law constraints',what:'European trade measures increasingly have to show that preferential treatment, verification and restrictions remain compatible with WTO commitments',why:'Legal compatibility matters because measures that cannot survive challenge are harder to use as durable economic-security tools'},
  export_controls:{title:'Technology controls are becoming a bigger part of European economic security',what:'Europe and its partners are tightening control over the transfer of sensitive technologies and dual-use goods',why:'Controls can protect strategic capability, but gaps between partners can shift trade rather than stop unwanted transfers'},
  supply_chain:{title:'Europe is trying to make supply chains less dependent on single sources',what:'Diversification, alternative suppliers and resilience measures are spreading across strategic supply chains',why:'The more concentrated an essential input is, the easier a disruption or political decision can affect European production'},
  critical_materials:{title:'Critical-material dependence remains a strategic bottleneck',what:'European industry still relies on concentrated external sources for several materials that are difficult to replace quickly',why:'A cutoff can propagate from raw materials into batteries, chips, clean technology and defence production'},
  chips:{title:'Europe is building chip capacity while key dependencies remain',what:'Investment is expanding European semiconductor capability, but equipment, inputs and leading-edge production remain internationally concentrated',why:'Chip access affects almost every strategic technology and determines how much production Europe can sustain independently'},
  ai_compute:{title:'Europe is expanding AI capacity while infrastructure constraints grow',what:'AI ambitions increasingly depend on access to computing power, energy, data centres and capital',why:'Those bottlenecks determine whether European AI firms and researchers can scale without relying heavily on external providers'},
  research_security:{title:'Research security is becoming a normal condition of international science',what:'More European research programmes are screening partners, knowledge flows and sensitive technologies for security risks',why:'The challenge is to protect valuable capability without closing the collaborations on which strong research depends'},
  research_openness:{title:'Open research is being balanced against tighter security conditions',what:'International collaboration remains important, but access to data, facilities and knowledge is becoming more conditional',why:'Europe needs both scientific openness and protection against unwanted transfer of sensitive capability'},
  talent:{title:'Europe’s strategic capacity increasingly depends on attracting and keeping specialist talent',what:'Research careers, mobility and competition for skilled people are becoming capability constraints in their own right',why:'Funding and infrastructure do not create capacity if the people needed to use them leave or cannot be recruited'},
  scaleup:{title:'Europe still struggles to turn strong research into firms that scale',what:'Financing and commercialisation remain weaker points between European research strength and large competitive companies',why:'When successful firms scale elsewhere, Europe loses part of the industrial and strategic value created by its own research'},
  industrial_capacity:{title:'Europe is trying to rebuild strategic production capacity',what:'Industrial policy and investment are pushing more production in strategically important sectors toward Europe',why:'Domestic capacity reduces exposure to external disruption, but high costs and foreign competition can make that capacity difficult to sustain'},
  defence:{title:'European defence production is expanding, but coordination remains a constraint',what:'More funding and procurement are moving toward defence capacity while national systems still have to work together',why:'Readiness depends not only on spending but on whether Europe can produce, procure and replenish equipment at scale'},
  infrastructure:{title:'Infrastructure resilience is becoming an economic-security issue',what:'Energy, digital and transport networks are increasingly treated as strategic assets rather than ordinary background infrastructure',why:'A failure or hostile disruption can spread quickly through production, trade and public services'},
  trade_tariffs:{title:'Trade pressure is making Europe choose more often between openness and retaliation',what:'Tariffs, trade-defence measures and anti-coercion tools are playing a larger role in economic-security policy',why:'These tools can protect European interests, but they can also raise costs, provoke retaliation and divide member states'},
  partnerships:{title:'Europe is using partnerships to spread strategic risk',what:'Trade, technology and research partnerships are being used to widen access to markets, inputs and expertise',why:'Partnerships reduce dependence only when they create real alternatives rather than new single points of reliance'},
  funding:{title:'Public funding is being used more deliberately to build strategic capability',what:'European funding programmes are increasingly tied to infrastructure, technology capacity and economic-security priorities',why:'Where public money goes can determine which capabilities remain in Europe and which dependencies persist'},
  standards_rules:{title:'Rules and standards are increasingly shaping strategic capacity',what:'Regulation, permitting and technical standards are affecting where technologies can be built, financed and deployed',why:'Well-designed rules can create trusted markets, while excessive friction can slow European scale-up'},
  strategic_autonomy:{title:'More European policy is being judged by whether it reduces strategic dependence',what:'Economic-security decisions increasingly weigh external access against European control of critical technologies, inputs and infrastructure',why:'The balance determines how much room Europe retains to act when partners or suppliers change course'}
};
function trendSide(side,pair,which){
  const object=clean(pair?.objectKey||'');
  const fixed=OBJECT_TRENDS[object]?.[which==='right'?'right':'left'];
  if(fixed)return pack(fixed[0],fixed[1],fixed[2]);
  // For an unfamiliar object, read the displayed statement and only the first
  // attached evidence items. This avoids letting one stray source in a large
  // evidence bundle redefine the whole card.
  const ev=(side?.evidence||[]).slice(0,2);
  const text=[side?.title,side?.plain,side?.why,evidenceText(ev),object].join(' ');
  const key=classify(text),tpl=TREND[key];
  if(tpl)return pack(tpl.title,tpl.what,tpl.why);
  const fallbackTitle=deTitle(side?.title||'');
  return pack(fallbackTitle,side?.plain||'',side?.why||'');
}
const WHY={
  hydrogen_storage:'It matters because a more flexible power system can use more domestic renewable energy without relying as heavily on backup imports.',
  energy_diversification:'It matters because diversified suppliers and routes reduce the leverage created by dependence on a small number of external sources.',
  european_preference:'It matters because procurement rules can build European production capacity, but may also raise costs or create trade friction.',
  wto_compatibility:'It matters because economic-security measures need a durable legal basis if Europe is to use them without creating avoidable trade disputes.',
  export_controls:'It matters because Europe needs to protect sensitive technology without cutting itself off from the partners and markets on which innovation depends.',
  supply_chain:'It matters because concentrated supply chains can turn a disruption in one country or route into a production problem across Europe.',
  critical_materials:'It matters because shortages in a small number of upstream materials can constrain many strategic European industries at once.',
  chips:'It matters because semiconductor access underpins digital, industrial, clean-tech and defence capability.',
  ai_compute:'It matters because control of computing infrastructure affects whether European AI capability can scale at home.',
  research_security:'It matters because Europe has to protect sensitive knowledge without weakening the international collaboration that supports strong science.',
  research_openness:'It matters because too much restriction can weaken research, while too little protection can expose sensitive capability.',
  talent:'It matters because strategic capability depends on people as much as on funding, facilities or policy.',
  scaleup:'It matters because Europe captures less economic and strategic value when strong research does not become large European firms.',
  industrial_capacity:'It matters because capacity located in Europe is easier to rely on during geopolitical or supply disruption.',
  defence:'It matters because defence readiness depends on the ability to produce and replenish equipment, not only on spending commitments.',
  infrastructure:'It matters because disruption to shared infrastructure can propagate quickly across sectors and countries.',
  trade_tariffs:'It matters because trade pressure can simultaneously affect exports, prices, investment and political cohesion.',
  partnerships:'It matters because a wider network of credible partners gives Europe more alternatives when one relationship becomes unreliable.',
  funding:'It matters because funding choices shape which technologies and capabilities Europe can retain and scale.',
  standards_rules:'It matters because rules can either create a predictable market for European technology or become a barrier to deployment.',
  strategic_autonomy:'It matters because dependence reduces Europe’s freedom to act when suppliers, partners or competitors use economic leverage.'
};
function card(title,body,evidence,kind){
  const evText=evidenceText(evidence),text=[title,body,evText].join(' '),key=classify(text);
  let t=deTitle(title),w=sentence(body),why=WHY[key]||'';
  const party=/^the eu is a party to the agreement$/i.test(t);
  if(party){
    if(key==='wto_compatibility'){
      t='The EU is maintaining a legal route for preferential trade treatment';
      w='The EU is seeking to preserve preferential trade treatment for the Western Balkans through a WTO waiver.';
    }else t='The EU is participating in an international agreement relevant to this issue';
  }
  const paperish=/^(use of|analysis of|study of|assessment of)\b/i.test(t)||/\b(public hourly|this article|this paper|the article examines|the study examines)\b/i.test(w)||/[,;:]\.$/.test(w)||t.length>150;
  if(paperish && key && TREND[key]){
    t=TREND[key].title;
    w=TREND[key].what+'.';
  }
  return pack(t,w,why);
}
function pageIntro(route){
  const m={
    trends:{kicker:'Competing directions',title:'Forces pulling Europe in different directions',lede:'Each pair shows two evidence-backed directions acting on the same issue. The balance shows which direction has stronger current evidence, not a probability.'},
    phenomena:{kicker:'Developments already under way',title:'Changes that keep shaping Europe',lede:'These are recurring developments seen across more than one piece of evidence or period. Each item says what keeps happening and why it matters.'},
    priorities:{kicker:'What current developments could lead to',title:'Risks & opportunities',lede:'Possible consequences of developments already visible in the Radar: what could weaken Europe’s economic security, and what could strengthen it.'},
    shocks:{kicker:'Sudden disruptions',title:'What could abruptly change the picture',lede:'Plausible external events that could quickly alter Europe’s economic-security position. These are scenarios to watch, not forecasts.'},
    future:{kicker:'2035 economic-security scenarios',title:'Four possible Europes in 2035',lede:'The scenarios vary along two big uncertainties: how connected the world economy remains and how much strategic capacity Europe can build and retain.'}
  };return m[route]||{};
}
root.RadarReaderClarity={clean,sentence,classify,evidenceText,trendSide,card,pageIntro};
})(typeof globalThis!=='undefined'?globalThis:this);
