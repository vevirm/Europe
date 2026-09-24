(function(root,factory){
  if(typeof module==='object'&&module.exports)module.exports=factory(require('../reader_rank.js'));
  else root.RadarShockScenarios=factory(root.RadarReaderRank);
})(typeof globalThis!=='undefined'?globalThis:this,function(ReaderRank){
  'use strict';
  const clean=v=>String(v||'').replace(/\s+/g,' ').trim();
  const low=v=>clean(v).toLowerCase();
  const dateValue=v=>{const n=Date.parse(v||'');return Number.isFinite(n)?n:0};
  const qualityScore=x=>Math.max(0,Math.min(100,Number(x?._storedQuality??ReaderRank?.scoreFor?.(x))||0));
  function rowText(x){return low([x.title,x.headline,x.what,x.core_message,x.summary,x.relevance_note,x.why_it_matters,x.source].join(' '))}
  function rx(v){return v instanceof RegExp?v:new RegExp(String(v),'i')}
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

  const DIRECT_TEMPLATES=[
    {
      id:'direct_materials_cutoff',direct:true,
      title:'A supplier country abruptly cuts exports of rare earths or other critical raw materials Europe cannot yet replace',
      plainly:'A handful of materials processed mainly in one country can stop whole European production lines: magnets, chips, batteries and defence equipment all depend on them.',
      secondOrder:'Prices spike, stockpiles run down, and firms with no second supplier halt lines before policy responses can take effect.',
      minEvidence:3,
      roles:[
        ['Raw-material concentration',{any:[/critical raw material/,/critical mineral/,/rare earth/,/gallium|germanium|graphite/],preferSource:/JRC|European Commission|IEA|Bruegel/}],
        ['Export-restriction mechanism',{any:[/export (?:control|restriction|ban|licen[cs])/,/economic coercion/,/weaponi[sz]/],preferSource:/MERICS|ECFR|EUISS|Rhodium/}],
        ['European mitigation effort',{any:[/stockpil/,/diversif/,/strategic project/,/resourceeu/,/critical raw materials act/,/partnership on critical raw materials/]}],
        ['Downstream industry exposure',{any:[/magnet/,/batter/,/semiconductor|chips?/,/defen[cs]e (?:industr|production)/]}],
      ],
      reasoning:[
        'The corpus documents European dependence on a few suppliers for critical raw materials and their processing.',
        'It also documents export restrictions and coercion as tools other states already use.',
        'Europe\u2019s mitigation (stockpiles, strategic projects, partnerships) is under way but not yet load-bearing.',
        'A sudden cutoff would therefore hit downstream industry before substitutes are ready.'
      ]
    },
    {
      id:'direct_tariff_escalation',direct:true,
      title:'A major trading partner imposes sweeping new tariffs on European goods and threatens more',
      plainly:'Tariffs are fast and cheap to impose: a single announcement can close part of a key export market and force Europe to choose between retaliation and negotiation.',
      secondOrder:'Exporters redirect sales, investment decisions freeze, and member states split over how hard to hit back.',
      minEvidence:3,
      roles:[
        ['Tariff mechanism',{any:[/tariff/,/customs dut/,/section 232/,/trade war/]}],
        ['European export exposure',{any:[/export dependence/,/exports? to the (?:us|united states)/,/market access/,/trade flows?/]}],
        ['Response toolbox',{any:[/anti-coercion/,/countermeasure/,/retaliat/,/rebalancing/]}],
        ['Transatlantic context',{any:[/transatlantic/,/eu-us/,/united states/]}],
      ],
      reasoning:[
        'The corpus shows European export dependence on large partner markets.',
        'It also shows tariffs being used as a political lever rather than only a trade instrument.',
        'The EU holds countermeasure and anti-coercion tools, but using them requires unity and accepts escalation risk.',
        'An abrupt tariff shock therefore tests both market diversification and political cohesion at once.'
      ]
    },
    {
      id:'direct_infrastructure_sabotage',direct:true,
      title:'Sabotage cuts subsea cables, pipelines or grid links that the European economy relies on',
      plainly:'A few physical links carry data, gas and electricity between member states and to partners; damaging several at once can disrupt services far from the incident.',
      secondOrder:'Repair capacity becomes the bottleneck, and ownership or vendor questions about the infrastructure move to the top of the agenda.',
      minEvidence:3,
      roles:[
        ['Critical infrastructure exposure',{any:[/critical infrastructure/,/subsea|undersea|submarine cable/,/pipeline/,/grid/]}],
        ['Hybrid / sabotage threat',{any:[/sabotage/,/hybrid/,/cyber ?attack/,/shadow fleet/]}],
        ['Ownership or vendor risk',{any:[/foreign ownership/,/high-risk vendor/,/port/,/5g/]}],
      ],
      reasoning:[
        'The corpus documents European reliance on a limited number of physical infrastructure links.',
        'It also documents hybrid threats and sabotage in European waters.',
        'Redundancy and repair capacity are thin relative to the number of critical links.',
        'Coordinated damage could therefore interrupt energy and data flows across several member states.'
      ]
    },
    {
      id:'direct_energy_cutoff',direct:true,
      title:'Europe\u2019s main remaining energy suppliers or routes are disrupted at once',
      plainly:'Having diversified away from Russian gas, Europe now leans on a few LNG suppliers and shipping routes; a disruption there would test the new arrangement.',
      secondOrder:'Energy-intensive industry curtails output, and pressure grows to relax other economic-security priorities to secure supply.',
      minEvidence:3,
      roles:[
        ['Supply concentration',{any:[/lng/,/gas supply/,/energy imports?/,/security of (?:oil|gas) supply/]}],
        ['Route or supplier disruption',{any:[/strait|red sea|suez|shipping/,/supply disruption/,/pipeline/]}],
        ['Industrial exposure',{any:[/energy[- ]intensive/,/energy prices?/,/deindustriali/]}],
        ['Mitigation',{any:[/diversif/,/storage/,/joint purchas/,/repowereu/]}],
      ],
      reasoning:[
        'The corpus documents the post-2022 shift of European energy supply to new suppliers and routes.',
        'It also documents industry\u2019s sensitivity to energy prices.',
        'Storage and joint purchasing help, but concentration has moved rather than disappeared.',
        'A simultaneous disruption would therefore land on industry and on the economic-security agenda at once.'
      ]
    },
    {
      id:'direct_secondary_sanctions',direct:true,
      title:'Foreign secondary sanctions force European firms and banks to cut ordinary business with a third country',
      plainly:'Sanctions set in another capital can reach European firms through the dollar, payments and supply chains, whatever the EU itself decides.',
      secondOrder:'European companies over-comply, and the EU\u2019s own trade and partnership choices narrow without a European decision.',
      minEvidence:3,
      roles:[
        ['Sanctions reach',{any:[/secondary sanctions/,/extraterritorial/,/entity list/,/financial sanctions/]}],
        ['Payments dependence',{any:[/payment|swift|dollar/,/international role of the euro/]}],
        ['European exposure',{any:[/european (?:firms|companies|banks)/,/circumvention/,/restrictive measures/]}],
      ],
      reasoning:[
        'The corpus documents the reach of sanctions through financial and payment channels.',
        'European firms depend on those channels for ordinary trade.',
        'The EU\u2019s blocking tools have historically been weak against this pressure.',
        'Secondary sanctions can therefore change European economic relations without a European decision.'
      ]
    },
  ];

  const TEMPLATES=[
    {
      id:'overcapacity_hollowing',
      title:'Subsidised overcapacity abroad hollows out a strategic European industry faster than trade defence can respond',
      plainly:'Trade-defence cases take months; a flood of cheap imports can close plants in weeks, and closed capacity rarely returns.',
      secondOrder:'Europe becomes dependent on imports in exactly the sector it was trying to protect, which turns a trade problem into a supply-security problem.',
      hidden:'Trade defence and supply security are handled by different teams; the link between plant closures now and dependence later is easy to miss.',
      minEvidence:3,
      roles:[
        ['Overcapacity pressure',{any:[/overcapacity/,/dumping/,/subsidi[sz]ed/,/foreign subsidies/]}],
        ['Trade-defence timing',{any:[/anti-dumping|anti-subsidy|countervailing|safeguard/,/trade defen[cs]e/]}],
        ['Industrial fragility',{any:[/plant closure|deindustriali|energy costs|energy prices/,/steel|chemicals|automotive|solar|batter/]}],
      ],
      reasoning:[
        'The corpus documents subsidised overcapacity in sectors where European producers already face high costs.',
        'Trade defence exists but works on a slower clock than market displacement.',
        'Once capacity closes, Europe relies on the very imports that displaced it.',
        'The shock is the timing gap between displacement and response.'
      ]
    },
    {
      id:'screening_capital_gap',
      title:'Europe blocks a foreign takeover of a strategic firm but has no European buyer ready',
      plainly:'Screening can stop a sale, but it cannot fund the company; a blocked firm without other capital may shrink, move, or be sold later on worse terms.',
      secondOrder:'Screening gets a reputation for destroying value, which weakens political support for using it.',
      hidden:'Investment screening and capital-markets policy are treated separately, though each depends on the other.',
      minEvidence:3,
      roles:[
        ['Screening instrument',{any:[/fdi screening|investment screening|screening regulation/,/golden power/]}],
        ['Foreign acquisition pressure',{any:[/acquisition|takeover|stake/,/state-owned/]}],
        ['European capital gap',{any:[/capital markets?|savings and investments union|scale-?up|venture/,/european competitiveness fund|eib/]}],
      ],
      reasoning:[
        'The corpus documents stronger EU and national investment screening.',
        'It also documents foreign interest in strategic European firms.',
        'European capital to replace a blocked buyer is limited.',
        'Blocking without an alternative can protect control while losing the capability.'
      ]
    },
    {
      id:'coercion_split',
      title:'A targeted coercion campaign against one member state splits the EU over using the anti-coercion instrument',
      plainly:'Coercion is often aimed at one country to test whether others will defend it; a divided response teaches the coercer that the method works.',
      secondOrder:'Future coercion becomes more likely, and member states hedge by making bilateral deals.',
      hidden:'The instrument\u2019s legal strength matters less than the speed and unity with which it is used.',
      minEvidence:3,
      roles:[
        ['Coercion mechanism',{any:[/economic coercion|coercive|weaponi[sz]/,/boycott|informal sanctions/]}],
        ['EU instrument',{any:[/anti-coercion/,/countermeasure/]}],
        ['Member-state divergence',{any:[/member states?/,/unanimity|qualified majority/,/divid|split|bilateral/]}],
      ],
      reasoning:[
        'The corpus documents coercion aimed at individual member states.',
        'The EU has an anti-coercion instrument but little experience using it.',
        'Member-state interests toward the coercer differ.',
        'The shock is a failed first test that changes expectations for every later case.'
      ]
    },
    {
      id:'derisking_cost_backlash',
      title:'The costs of de-risking trigger a backlash that stalls Europe\u2019s economic-security agenda',
      plainly:'Diversification, stockpiles and screening cost money and slow trade; if prices rise or partners retaliate, support for the agenda can collapse.',
      secondOrder:'Europe reverts to cheapest-supplier habits just as dependence risks peak.',
      hidden:'The dilemma between protection and openness becomes a political shock, not only an economic trade-off.',
      minEvidence:3,
      roles:[
        ['Cost of protection',{any:[/cost of de-?risking|costs? of (?:diversification|protection)/,/higher prices|price increases/,/welfare cost/]}],
        ['Openness argument',{any:[/openness|open trade|wto|protectionis/]}],
        ['Economic-security agenda',{any:[/economic security/,/de-?risk/,/strategic autonomy/]}],
      ],
      reasoning:[
        'The corpus contains evidence on the costs of de-risking and fragmentation.',
        'It also shows active debate over protectionism and WTO compatibility.',
        'Economic-security measures depend on sustained political support.',
        'A cost shock could turn the openness-protection dilemma into a reversal.'
      ]
    },
    {
      id:'partner_alignment_gap',
      title:'Like-minded partners diverge on export controls, leaving Europe exposed at the edges',
      plainly:'Controls only work if partners apply them together; when one tightens and another does not, technology leaks through the gap and trust erodes.',
      secondOrder:'Europe faces pressure to follow rules set elsewhere or accept being the weak link.',
      hidden:'Partnership and technology security are filed as separate topics though each depends on the other.',
      minEvidence:3,
      roles:[
        ['Export-control coordination',{any:[/export control/,/dual-use/,/entity list/]}],
        ['Partner divergence',{any:[/united states|japan|netherlands|g7/,/like-minded|partner/]}],
        ['Technology leakage risk',{any:[/leakage|technology transfer|circumvention/,/semiconductor|chips?/]}],
      ],
      reasoning:[
        'The corpus documents export controls coordinated among a small group of partners.',
        'Partners\u2019 priorities and timing differ.',
        'Gaps allow circumvention and put pressure on the least aligned member.',
        'The shock is divergence at the moment controls matter most.'
      ]
    },
  ];

  function buildFromTemplates(data,templates){
    const rows=corpus(data),out=[];
    for(const t of templates){
      const used=new Set(),roleEvidence=[];
      for(const [role,spec] of t.roles){const row=pick(rows,spec,used);if(row)roleEvidence.push({role,row,quality:qualityScore(row)})}
      if(roleEvidence.length<(t.minEvidence||t.roles.length))continue;
      const roleQs=roleEvidence.map(e=>e.quality),best=Math.max(...roleQs),avg=roleQs.reduce((a,b)=>a+b,0)/roleQs.length;
      const coverage=roleEvidence.length/t.roles.length;
      const sources=new Set(roleEvidence.map(e=>clean(e.row.source)).filter(Boolean)).size;
      const strands=new Set(roleEvidence.map(e=>e.row._strand).filter(Boolean)).size;
      // Inference is recall-first: if the required independent evidence roles are present,
      // the scenario is inferred. Publication quality changes its confidence and ordering;
      // it does not erase a supported seam merely because one supporting row ranks lower.
      const inferenceScore=Math.max(0,Math.min(100,Math.round(
        avg*0.55+best*0.20+coverage*15+Math.min(1,sources/3)*5+Math.min(1,strands/2)*5
      )));
      // Do not let an older top-ranked row hide a genuinely new contribution. If a new
      // scan adds evidence that matches any role, retain up to two such rows as explicit
      // corroboration. That makes existing shock hypotheses visibly UPDATED rather than
      // falsely NEW, while the core role evidence still anchors the inference.
      const fresh=rows.filter(x=>x.new_this_scan&&!used.has(x._row)&&t.roles.some(([,spec])=>matches(x,spec)))
        .sort((a,b)=>qualityScore(b)-qualityScore(a)||dateValue(b.date)-dateValue(a.date)).slice(0,2)
        .map(row=>({role:'New corroboration',row,quality:qualityScore(row)}));
      const evidence=[...roleEvidence,...fresh].sort((a,b)=>b.quality-a.quality);
      out.push({...t,evidence,coverage:roleEvidence.length+'/'+t.roles.length,evidenceQuality:{best,average:Math.round(avg)},inferenceScore,updatedThisScan:fresh.length>0});
    }
    return out.sort((a,b)=>b.inferenceScore-a.inferenceScore||b.evidenceQuality.best-a.evidenceQuality.best||a.title.localeCompare(b.title));
  }
  function dynamicRow(e){return {title:e.title||'Evidence',source:e.source||'',date:e.date||'',link:e.link||'',core_message:e.core_message||'',geo_evidence:Array.isArray(e.geo_evidence)?e.geo_evidence:[],ri_evidence:Array.isArray(e.ri_evidence)?e.ri_evidence:[],a_context_evidence:Array.isArray(e.a_context_evidence)?e.a_context_evidence:[],new_this_scan:!!e.new_this_scan,_row:e.row||'',_strand:e.strand||'',_storedQuality:Number(e.quality)||0}}
  function buildDynamic(data){
    const xs=Array.isArray(data?.shock_inference?.dynamic_shocks)?data.shock_inference.dynamic_shocks:[];
    return xs.map(s=>{
      const evidence=(Array.isArray(s.support)?s.support:[]).map(e=>({role:e.role||'Supporting evidence',row:dynamicRow(e),quality:Number(e.quality)||0}));
      const againstEvidence=(Array.isArray(s.against)?s.against:[]).map(e=>({role:e.role||'Counter-evidence',row:dynamicRow(e),quality:Number(e.quality)||0}));
      return {id:s.id,title:s.title,plainly:s.plainly,secondOrder:s.second_order||'',hidden:s.why_easy_to_miss||'',reasoning:Array.isArray(s.reasoning)?s.reasoning:[],conditions:Array.isArray(s.conditions)?s.conditions:[],caseAgainst:Array.isArray(s.case_against)?s.case_against:[],preventionActions:Array.isArray(s.prevention_actions)?s.prevention_actions:[],watchFor:Array.isArray(s.watch_for)?s.watch_for:[],netAssessment:s.net_assessment||'',officialTriggerPresent:!!s.official_trigger_present,couplingCount:Number(s.coupling_count)||0,evidence,againstEvidence,dynamic:true,status:s.status||'unchanged',newThisScan:!!s.new_this_scan,updatedThisScan:!!s.updated_this_scan,inferenceScore:Number(s.inference_score)||0,evidenceQuality:{best:Number(s.best_quality)||0,average:Number(s.average_quality)||0},coverage:`${evidence.length} evidence rows`};
    }).filter(s=>s.id&&s.title&&s.evidence.length).sort((a,b)=>b.inferenceScore-a.inferenceScore||a.title.localeCompare(b.title));
  }
  function build(data){return buildFromTemplates(data,TEMPLATES)}
  function buildDirect(data){return buildFromTemplates(data,DIRECT_TEMPLATES)}
  return {build,buildDirect,buildDynamic,templates:TEMPLATES,directTemplates:DIRECT_TEMPLATES,rowText};
});
