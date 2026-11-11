#!/usr/bin/env node
// Regenerate *retrospective model* figures; the existing F1 observed charts
// are untouched. Node.js 18+, no external dependencies.
// Run from repository root: node results/figures/build_f1_reconstruction.mjs
import fs from "node:fs";
import path from "node:path";
const renderF1 = function renderF1(){
  const PI=Math.PI,c1=.5-PI/40,c2=.55+PI/40;
  const fn=(x,y)=>{
    const g=(c,a)=>{let dx=x-c,dy=y-c;return a*Math.exp(-1600*(dx*dx+dy*dy))*Math.cos(40*dx)*Math.cos(40*dy)};
    return g(c1,1)+g(c2,2)
  };
  const low=.32,high=.74,span=high-low;const dim=900;
  const fmt=n=>n.toFixed(3),safe=s=>String(s).replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;");
  const colour=v=>{
    if(v<0){let t=Math.sqrt(Math.min(1,-v/.45));return `rgb(${Math.round(40+115*t)},${Math.round(66-23*t)},${Math.round(130+28*t)})`}
    let t=Math.sqrt(Math.min(1,v/2));return `rgb(${Math.round(30+224*t)},${Math.round(70+145*t)},${Math.round(131-73*t)})`
  };
  const title='F1 · Reconstructed Gabor-type model';
  const credits=`Model estimate, NOT new portal evaluations. Domain cropped to x1,x2 in [${low.toFixed(2)}, ${high.toFixed(2)}].`;
  const wrap=(inner,detail)=>`<svg xmlns="http://www.w3.org/2000/svg" width="${dim}" height="710" viewBox="0 0 ${dim} 710" role="img"><title>${safe(title)} — ${detail}</title><desc>Retrospective model fitted using the original observations; the model family is from separately recovered code. ${credits}</desc><rect width="${dim}" height="710" fill="#f6f9fc"/><g font-family="Arial,Helvetica,sans-serif"><text x="48" y="45" fill="#19354f" font-size="28" font-weight="700">${safe(title)}</text><text x="48" y="74" fill="#53677d" font-size="15">${safe(detail)}</text>${inner}<text x="48" y="675" font-size="13" fill="#344b63">${safe(credits)}</text><text x="48" y="695" font-size="12" fill="#596c80">Values are predictions of the recovered equation; original measured observations remain in the F1 history.</text></g></svg>`;
  const x0=115,y0=106,w=590,h=505,N=72;
  const px=x=>x0+(x-low)/span*w,py=y=>y0+h-(y-low)/span*h;
  let heat=`<rect x="${x0}" y="${y0}" width="${w}" height="${h}" fill="white" stroke="#667b91"/>`;
  for(let iy=0;iy<N;iy++)for(let ix=0;ix<N;ix++){
    const x=low+(ix+.5)/N*span,y=low+(iy+.5)/N*span,v=fn(x,y);
    let xx=x0+ix*w/N,yy=y0+h-(iy+1)*h/N;
    heat+=`<rect x="${xx.toFixed(2)}" y="${yy.toFixed(2)}" width="${(w/N+.25).toFixed(2)}" height="${(h/N+.25).toFixed(2)}" fill="${colour(v)}"/>`;
  }
  for(let i=0;i<=4;i++){let x=low+span*i/4;
    heat+=`<text x="${px(x).toFixed(2)}" y="631" text-anchor="middle" font-size="14" fill="#405974">${fmt(x)}</text>`;
    heat+=`<text x="98" y="${(py(x)+5).toFixed(2)}" text-anchor="end" font-size="14" fill="#405974">${fmt(x)}</text>`;
  }
  heat+=`<text x="410" y="655" font-size="17" fill="#25425e" text-anchor="middle">x1</text><text x="36" y="367" font-size="17" fill="#25425e" text-anchor="middle" transform="rotate(-90 36 367)">x2</text>`;
  const locs=[[c1,1,"minor"],[c2,2,"major"],[.62854,null,"R11"]];
  for(let [c,a,label] of locs){
    let xx=px(c),yy=py(c);heat+=`<circle cx="${xx.toFixed(2)}" cy="${yy.toFixed(2)}" r="${label==="R11"?4:11}" fill="none" stroke="${label==="R11"?"#162232":"#fff"}" stroke-width="${label==="R11"?2:2.5}"/>`;
  }
  heat+=`<text x="742" y="150" font-size="16" fill="#19354f" font-weight="700">Model highlights</text><text x="742" y="191" font-size="13" fill="#405974">Minor centre</text><text x="742" y="212" font-size="14" fill="#102b43">${c1.toFixed(6)}</text><text x="742" y="254" font-size="13" fill="#405974">Major centre</text><text x="742" y="275" font-size="14" fill="#102b43">${c2.toFixed(6)}</text><text x="742" y="325" font-size="13" fill="#405974">Six-decimal R11 query</text><text x="742" y="345" font-size="14" fill="#102b43">0.628540</text><text x="742" y="395" font-size="13" fill="#405974">Colour: model score</text>`;
  for(let i=0;i<20;i++)heat+=`<rect x="747" y="${(413+i*8.4).toFixed(2)}" width="24" height="9" fill="${colour(2*(1-i/19))}"/>`;
  heat+=`<text x="783" y="428" font-size="12" fill="#405974">2.0</text><text x="783" y="582" font-size="12" fill="#405974">0.0</text><text x="742" y="607" font-size="12" fill="#6b405b">Purple: negative lobes</text>`;
  const two=wrap(heat,"2D model heatmap · two peaks and oscillatory neighbourhoods");
  const M=44;let cells=[];
  const project=(u,v,z)=>[436+(u-v)*260,520+(u+v)*90-z*240];
  let base='<polygon points="436,520 696,610 436,700 176,610" fill="#fff" stroke="#d1dfeb"/>';
  // Note: bottom can reach y=700; footnote will appear above; adjust coordinate.
  // Orbit the camera 45 degrees around the vertical axis: 45° -> 90°.
  // The old view projected both centres (x1 = x2) onto the same screen
  // column, obscuring the separation between the two modelled peaks.
  // Preserve the same data, model, plot bounds, and vertical exaggeration.
  const cameraYaw = Math.PI / 4 + Math.PI / 4;
  const cosYaw = Math.cos(cameraYaw), sinYaw = Math.sin(cameraYaw);
  const horizontalScale = 248 / Math.SQRT1_2;
  const depthScale = 82 / Math.SQRT1_2;
  const pp=(x,y,z)=>{
    const u=(x-low)/span - .5, v=(y-low)/span - .5;
    return [
      430 + horizontalScale*(u*cosYaw-v*sinYaw),
      547 + depthScale*(u*sinYaw+v*cosYaw)-z*200
    ];
  };
  for(let i=0;i<M;i++)for(let j=0;j<M;j++){
    let xs=[low+i/M*span,low+(i+1)/M*span],ys=[low+j/M*span,low+(j+1)/M*span];
    const q=[[xs[0],ys[0]],[xs[1],ys[0]],[xs[1],ys[1]],[xs[0],ys[1]]];
    let vals=q.map(([x,y])=>fn(x,y)),points=q.map(([x,y],k)=>pp(x,y,vals[k]/2));
    const poly=points.map(([x,y])=>`${x.toFixed(1)},${y.toFixed(1)}`).join(" ");
    // Sort by camera-space depth rather than the old fixed i+j order.
    const depth=(i+.5)*sinYaw+(j+.5)*cosYaw;
    cells.push({depth,markup:`<polygon points="${poly}" fill="${colour(vals.reduce((a,b)=>a+b,0)/4)}" stroke="#f3f8fc" stroke-width=".45" stroke-opacity=".55"/>`});
  }
  cells.sort((a,b)=>a.depth-b.depth);
  let sur=`<polygon points="${[[0,0],[1,0],[1,1],[0,1]].map(([u,v])=>pp(low+u*span,low+v*span,0).map(z=>z.toFixed(1)).join(",")).join(" ")}" fill="#eef2f7" stroke="#b5c7d9"/>`+cells.map(c=>c.markup).join("");
  const x1End=pp(high,low,0), x2End=pp(low,high,0);
  sur+=`<text x="${(x1End[0]+35).toFixed(1)}" y="${(x1End[1]+20).toFixed(1)}" font-size="17" fill="#25425e">x1</text><text x="${(x2End[0]-35).toFixed(1)}" y="${(x2End[1]-15).toFixed(1)}" font-size="17" fill="#25425e">x2</text><text x="435" y="178" font-size="17" fill="#25425e">Predicted score</text><text x="730" y="220" font-size="14" fill="#19354f">High peak ≈ 2.0</text><text x="730" y="245" font-size="14" fill="#19354f">Minor peak ≈ 1.0</text><text x="730" y="285" font-size="13" fill="#405974">Gaussian envelopes with</text><text x="730" y="304" font-size="13" fill="#405974">cosine oscillations</text>`;
  const three=wrap(sur,"3D reconstructed model · camera rotated 45° · two response regions");
  return {"results/figures/f1_model_2d.svg":two,"results/figures/f1_model_3d.svg":three};
};
for(const [filename,contents] of Object.entries(renderF1())){
  fs.mkdirSync(path.dirname(filename),{recursive:true});
  fs.writeFileSync(filename,contents,"utf8");
  console.log("Wrote",filename);
}
