#!/usr/bin/env node
// Rebuild the documented figures from the repository's returned observations.
// Node.js 18+; no external JavaScript dependencies.
// Run from the repository root: node results/figures/build_visual_gallery.mjs
import fs from "node:fs";
import path from "node:path";
const dims=[2,2,3,4,4,5,6,8];
function parseCsv(filename){
  const lines=fs.readFileSync(filename,"utf8").trim().split(/\r?\n/);
  const header=lines.shift().split(",");
  return lines.map(line=>Object.fromEntries(line.split(",").map((value,i)=>[header[i],value])));
}
const data=Array.from({length:8},(_,i)=>{
  const f=i+1;
  const rows=parseCsv(`data/accumulated/function_${f}/observations_through_week10.csv`).map(r=>({
    x:Array.from({length:dims[i]},(_,j)=>Number(r["x"+(j+1)])),
    y:Number(r.output),stage:r.stage
  }));
  return {f,rows};
});
for (const source of ["data/portal_rounds_11_12.csv","data/portal_rounds_13.csv"]){
  for (const row of parseCsv(source)){
    if(!row.Input) throw new Error(`Verified portal record missing input: ${source}, F${row.Function} R${row.Round}`);
    data[Number(row.Function)-1].rows.push({
      x:row.Input.split("-").map(Number),y:Number(row.Output),stage:"R"+row.Round
    });
  }
}
function renderGallery(data){
 const W=1040,H=690,N=34,S=23;
 const details={
 1:{title:"F1 · Narrow response",kind:"observed",axes:[0,1],fixed:null,short:"Observed points; log10(score) clipped at 10^-60"},
 2:{title:"F2 · Multiple candidate regions",kind:"observed",axes:[0,1],fixed:null,short:"Observed points; values are raw portal scores"},
 3:{title:"F3 · Negative-valued objective",kind:"observed",axes:[0,1],fixed:null,short:"Projection only: x3 varies across points"},
 4:{title:"F4 · Local sensitivity",kind:"observed",axes:[0,1],fixed:null,short:"Projection only: x3 and x4 vary across points"},
 5:{title:"F5 · Power-sum reconstruction",kind:"model",axes:[0,1],fixed:[.999999,.999999,.999999,.999999],short:"Equation slice; x3=x4=0.999999; display uses log1p(score)"},
 6:{title:"F6 · Incompletely understood",kind:"observed",axes:[0,1],fixed:null,short:"Projection only: x3, x4 and x5 vary across points"},
 7:{title:"F7 · Positive Hartmann-6",kind:"model",axes:[0,1],fixed:[.201689,.150011,.476874,.275332,.311652,.657301],short:"Benchmark-model slice; x3...x6 fixed at best R12 values"},
 8:{title:"F8 · Additive quadratic",kind:"model",axes:[2,7],fixed:[.1,.15,.13,.15,.8,.5,.2,.6],short:"Equation slice; all other inputs fixed at fitted vertex"}
 };
 const A=[[10,3,17,3.5,1.7,8],[.05,10,17,.1,8,14],[3,3.5,1.7,10,17,8],[17,8,.05,10,.1,14]];
 const P=[[.1312,.1696,.5569,.0124,.8283,.5886],[.2329,.4135,.8307,.3736,.1004,.9991],[.2348,.1451,.3522,.2883,.3047,.6650],[.4047,.8828,.8732,.5743,.1091,.0381]];
 const alpha=[1,1.2,3,3.2],centre=[.1,.15,.13,.15,.8,.5,.2,.6],weights=[2,1,3,1,.5,1,2,.1],b=[7.5,16,40,120];
 function f(x,i){
   if(i===5){let sum=0;for(let k=1;k<=4;k++){let inner=x.reduce((s,a)=>s+(4*a)**k,0)-b[k-1];sum+=inner*inner;}return .01*sum;}
   if(i===7)return alpha.reduce((sum,a,k)=>sum+a*Math.exp(-x.reduce((q,v,j)=>q+A[k][j]*(v-P[k][j])**2,0)),0);
   if(i===8)return 10-x.reduce((sum,v,k)=>sum+weights[k]*(v-centre[k])**2,0);
   throw Error("no reconstructed model for F"+i);
 }
 const best=Object.fromEntries(data.map(z=>[z.f,z.rows.reduce((a,b)=>b.y>a.y?b:a,z.rows[0])]));
 const palette=t=>{t=Math.max(0,Math.min(1,t));let stops=[[41,68,132],[35,128,177],[44,166,151],[246,193,92]],j=Math.min(2,Math.floor(t*3)),w=t*3-j;let a=stops[j],b=stops[j+1];return "#"+a.map((n,k)=>Math.round(n+(b[k]-n)*w).toString(16).padStart(2,"0")).join("")};
 const textesc=s=>String(s).replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;");
 const num=n=>Math.abs(n)<1e-8?n.toExponential(2):Math.abs(n)>1000?n.toLocaleString("en-GB",{maximumFractionDigits:2}):Number(n).toFixed(4);
 const tr=(y,f,model)=>f===1?Math.log10(Math.max(y,1e-60)):(f===5&&model?Math.log1p(Math.max(0,y)):y);
 const pos2=(a,c)=>[126+a*740,555-c*435];
 const project=(a,c,zn)=>[525+330*(a-c),390+135*(a+c)-290*zn];
 const basics=(title,subt)=>`<rect x="0" y="0" width="${W}" height="${H}" fill="#f6f9fc"/><text x="50" y="43" font-size="26" fill="#19354f" font-weight="700">${textesc(title)}</text><text x="50" y="70" font-size="14" fill="#53677d">${textesc(subt)}</text>`;
 const frame2=(d,caption)=>{let x0=126,x1=866,y0=120,y1=555,a=d.axes[0]+1,b=d.axes[1]+1,r=`<rect x="${x0}" y="${y0}" width="${x1-x0}" height="${y1-y0}" fill="#fff" stroke="#bdcad8"/>`;
 for(let t=0;t<=4;t++){let x=x0+(x1-x0)*t/4,y=y1-(y1-y0)*t/4;r+=`<line x1="${x}" y1="${y0}" x2="${x}" y2="${y1}" stroke="#e5edf4"/><line x1="${x0}" y1="${y}" x2="${x1}" y2="${y}" stroke="#e5edf4"/><text x="${x}" y="579" font-size="12" text-anchor="middle" fill="#65768a">${(t/4).toFixed(2)}</text><text x="108" y="${y+4}" text-anchor="end" font-size="12" fill="#65768a">${(t/4).toFixed(2)}</text>`;}
 return r+`<text x="495" y="623" font-size="16" fill="#334d66" text-anchor="middle">x${a}</text><text x="42" y="348" transform="rotate(-90,42,348)" font-size="16" text-anchor="middle" fill="#334d66">x${b}</text><text x="50" y="665" font-size="13" fill="#52657b">${textesc(caption)}</text>`;};
 function legend(lo,hi,functionId){let s=`<text x="909" y="136" font-size="12" fill="#334d66">High score</text>`;
 for(let i=0;i<20;i++)s+=`<rect x="913" y="${150+i*17}" width="23" height="18" fill="${palette(1-i/19)}"/>`;
 s+=`<text x="945" y="163" font-size="11" fill="#53677d">${textesc(functionId===1?"log10(y)†":functionId===5?"log1p(y)":"score")}</text><text x="913" y="505" font-size="12" fill="#53677d">Range</text><text x="913" y="529" font-size="10" fill="#53677d">Min: ${textesc(num(lo))}</text><text x="913" y="551" font-size="10" fill="#53677d">Max: ${textesc(num(hi))}</text>`;return s;}
 const outputs={};let manifest=[];
 for(const block of data){const id=block.f,d=details[id],observed=d.kind==="observed",pointBest=best[id],cols=d.axes;
   let axisSamples=[],grid=[],limlo=Infinity,limhi=-Infinity;
   if(observed){axisSamples=block.rows.map(r=>({a:r.x[cols[0]],c:r.x[cols[1]],v:r.y,h:tr(r.y,id,false),stage:r.stage,mark:r===pointBest}));}
   else{for(let i=0;i<=N;i++){let row=[];for(let j=0;j<=N;j++){let x=d.fixed.slice();x[cols[0]]=i/N*.999999;x[cols[1]]=j/N*.999999;let v=f(x,id),h=tr(v,id,true);row.push({a:i/N,c:j/N,v,h});}grid.push(row);}axisSamples=grid.flat();}
   for(const q of axisSamples){limlo=Math.min(limlo,q.h);limhi=Math.max(limhi,q.h);}
   if(!(limhi>limlo))limhi=limlo+1;
   const nz=h=>(h-limlo)/(limhi-limlo);
   // 2D: discrete heatmap only where a documented parametric equation exists; otherwise real returned points.
   let v2=`<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${W} ${H}" role="img"><title>${textesc(d.title)} — ${observed?"observed input projection":"model 2D slice"}</title><desc>${textesc(d.short)}. ${observed?"No estimated contour surface is shown.":"Other coordinates fixed as labelled."}</desc><g font-family="Arial,Helvetica,sans-serif">${basics(d.title,observed?"Measured input locations · no reconstructed surface":"Documented equation · two-input slice; remaining dimensions fixed")}`;
   v2+=frame2(d,observed?`${block.rows.length} input/output pairs available · colours encode returned scores · ${d.short}`:`F${id} modelled slice · ${d.short}`);
   if(observed){
      // F1/F2: full x1,x2 domain; higher dimensions: x1,x2 projections only.
      for(const q of axisSamples){const [x,y]=pos2(q.a,q.c);let t=nz(q.h);v2+=`<circle cx="${x.toFixed(2)}" cy="${y.toFixed(2)}" r="${q.mark?9:6}" fill="${palette(t)}" stroke="${q.mark?"#101e33":q.stage==="Initial"?"#f7fafc":"#334155"}" stroke-width="${q.mark?3:1.1}" opacity="${q.mark?1:.82}"/>`;}
   }else{
      for(let i=0;i<N;i++)for(let j=0;j<N;j++){let q=grid[i][j],q2=grid[i+1][j+1],av=(q.h+grid[i+1][j].h+grid[i][j+1].h+q2.h)/4,[x,yy]=pos2(i/N,(j+1)/N);
        v2+=`<rect x="${x.toFixed(2)}" y="${yy.toFixed(2)}" width="${(740/N+1).toFixed(2)}" height="${(435/N+1).toFixed(2)}" fill="${palette(nz(av))}"/>`;}
      const [x,y]=pos2(pointBest.x[cols[0]],pointBest.x[cols[1]]);v2+=`<circle cx="${x}" cy="${y}" r="11" fill="none" stroke="white" stroke-width="3"/><circle cx="${x}" cy="${y}" r="6.5" fill="#122c44" stroke="#fff" stroke-width="1.5"/>`;
   }
   v2+=legend(limlo,limhi,id)+`<text x="907" y="585" font-size="11" fill="#53677d">${textesc(observed?"● darker ring: best":"● model / observed best")}</text>${id===1?`<text x="907" y="609" font-size="10" fill="#53677d">† nonpositive y clipped</text>`:""}</g></svg>`;
   outputs[`results/figures/f${id}_2d.svg`]=v2;
   // 3D: projected surface for model; three-dimensional point cloud otherwise (x1, x2, observed y).
   let v3=`<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${W} ${H}" role="img"><title>${textesc(d.title)} — ${observed?"3D observation projection":"3D model slice"}</title><desc>${textesc(d.short)}. ${observed?"A point cloud only; no invented surface.":"Sliced reconstructed mathematical function."}</desc><g font-family="Arial,Helvetica,sans-serif">${basics(d.title,observed?"3D projection of actual observations; no fitted surface":"3D projected surface of the documented equation")}`;
   const [p00,p10,p01,p11]=[[0,0,0],[1,0,0],[0,1,0],[1,1,0]].map(x=>project(...x));
   v3+=`<polygon points="${[p00,p10,p11,p01].map(p=>p.map(v=>v.toFixed(1)).join(",")).join(" ")}" fill="#fff" stroke="#d0dbe6"/>`;
   if(!observed){
      let cells=[];for(let i=0;i<S;i++)for(let j=0;j<S;j++){
       const samp=(a,c)=>{let x=d.fixed.slice();x[cols[0]]=a*.999999;x[cols[1]]=c*.999999;let v=f(x,id);return {a,c,h:tr(v,id,true)};};
       let q=[samp(i/S,j/S),samp((i+1)/S,j/S),samp((i+1)/S,(j+1)/S),samp(i/S,(j+1)/S)],zm=q.reduce((s,t)=>s+t.h,0)/4,corners=q.map(t=>project(t.a,t.c,nz(t.h)));
       cells.push({depth:i+j,poly:`<polygon points="${corners.map(p=>p.map(v=>v.toFixed(2)).join(",")).join(" ")}" fill="${palette(nz(zm))}" stroke="#f1f5f9" stroke-opacity=".23" stroke-width=".6"/>`});}
      cells.sort((a,b)=>a.depth-b.depth);v3+=cells.map(q=>q.poly).join("");
      const [a,c]=[pointBest.x[cols[0]],pointBest.x[cols[1]]],zz=nz(tr(f(d.fixed,id),id,true)),[X,Y]=project(a,c,zz);
      v3+=`<circle cx="${X}" cy="${Y}" r="8" stroke="#fff" stroke-width="2.6" fill="#192a43"/>`;
   }else{
      let ordered=axisSamples.slice().sort((a,b)=>(a.a+a.c)-(b.a+b.c));
      for(const q of ordered){let [x,y]=project(q.a,q.c,nz(q.h)),[xx,yy]=project(q.a,q.c,0);
       v3+=`<line x1="${xx.toFixed(2)}" y1="${yy.toFixed(2)}" x2="${x.toFixed(2)}" y2="${y.toFixed(2)}" stroke="#8ea0b1" stroke-opacity=".28"/>`;
       v3+=`<circle cx="${x.toFixed(2)}" cy="${y.toFixed(2)}" r="${q.mark?8:5.5}" fill="${palette(nz(q.h))}" stroke="${q.mark?"#0b2036":"#fff"}" stroke-width="${q.mark?2.5:1}" opacity=".93"/>`;}
   }
   v3+=`<line x1="${p00[0]}" y1="${p00[1]}" x2="${p10[0]}" y2="${p10[1]}" stroke="#64798c" stroke-width="2"/><line x1="${p00[0]}" y1="${p00[1]}" x2="${p01[0]}" y2="${p01[1]}" stroke="#64798c" stroke-width="2"/><text x="${p10[0]+9}" y="${p10[1]+8}" font-size="14" fill="#29455e">x${cols[0]+1}</text><text x="${p01[0]-29}" y="${p01[1]+10}" font-size="14" fill="#29455e">x${cols[1]+1}</text><text x="905" y="210" font-size="12" fill="#455f74">${textesc(id===1?"z: log10(y), clipped":id===5?"z: log1p(y)":"z: output")}</text><text x="50" y="660" font-size="13" fill="#52657b">${textesc(observed?`${block.rows.length} observed points; higher-dimensional coordinates vary · ${d.short}`:`Reconstructed model · ${d.short}`)}</text></g></svg>`;
   outputs[`results/figures/f${id}_3d.svg`]=v3;
   manifest.push({function:id,kind:d.kind==="model"?"reconstructed-model-slice":"measured-points-only",observationsPlotted:block.rows.length,axes:cols.map(i=>i+1),fixed:d.fixed,note:d.short,assets:[`results/figures/f${id}_2d.svg`,`results/figures/f${id}_3d.svg`]});
 }
 return {files:outputs,manifest,modelChecks:{f5:f([.999999,.999999,.999999,.999999],5),f7:f([.201689,.150011,.476874,.275332,.311652,.657301],7),f8:f(centre,8)}};
}
const output=renderGallery(data);
for(const [filename,svg] of Object.entries(output.files)){
  fs.mkdirSync(path.dirname(filename),{recursive:true});
  fs.writeFileSync(filename,svg+"\n","utf8");
}
fs.writeFileSync("results/figures/gallery_manifest.json",JSON.stringify(output.manifest,null,2)+"\n","utf8");
const {f5,f7,f8}=output.modelChecks;
if(Math.abs(f5-8662.405001248297)>1e-9||
   Math.abs(f7-3.3223680113931557)>1e-12||Math.abs(f8-10)>1e-12)
   throw Error("A reconstructed model failed to reproduce a confirmed return");
console.log("Built "+Object.keys(output.files).length+" plots; checked F5/F7/F8.");
