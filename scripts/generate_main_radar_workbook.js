#!/usr/bin/env node
'use strict';
// Active Radar-only workbook, rebuilt after normal scan alongside legacy Excel.
const fs=require('fs');
const path=require('path');
const ROOT=path.resolve(__dirname,'..');
const input=path.join(ROOT,'radar_active.json');
if(!fs.existsSync(input))throw new Error('Authoritative radar_active.json is missing');
const data=JSON.parse(fs.readFileSync(input,'utf8'));
const Merit=require('../source_merit.js');
const Workbook=require('../stuff/workbook.js');
const bytes=Workbook.buildMainRadarXlsx(data,Merit);
const out=path.join(ROOT,'stuff','main_radar_stuff.xlsx');
fs.writeFileSync(out,Buffer.from(bytes));
console.log(`Wrote ${out}: ${Workbook.buildRows(data,Merit).length} active ranked records, no Historical findings sheet`);
