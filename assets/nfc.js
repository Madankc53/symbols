(function(){
'use strict';

/* =========================================================
   1. GEOMETRY — computed from Schedule 1 (AB = 1, y points up)
   ========================================================= */
function ss(t,a,b){var x=(t-a)/(b-a);x=x<0?0:x>1?1:x;return x*x*(3-2*x);}
function clamp(x,a,b){return x<a?a:x>b?b:x;}
function arcPoints(c,r,a0,a1,n){var o=[],i,a;for(i=0;i<=n;i++){a=a0+(a1-a0)*i/n;o.push([c[0]+r*Math.cos(a),c[1]+r*Math.sin(a)]);}return o;}
function pol(c,r,a){return [c[0]+r*Math.cos(a),c[1]+r*Math.sin(a)];}

/* Offset a counter-clockwise polygon outward by w with mitred corners
   (Schedule 1, clause 23: outer angles equal inner angles). */
function offsetPoly(pts,w){
  var n=pts.length,L=[],i,out=[];
  for(i=0;i<n;i++){
    var p=pts[i],q=pts[(i+1)%n],dx=q[0]-p[0],dy=q[1]-p[1],len=Math.hypot(dx,dy);
    dx/=len;dy/=len;
    L.push({x:p[0]+dy*w,y:p[1]-dx*w,dx:dx,dy:dy});
  }
  for(i=0;i<n;i++){
    var a=L[(i-1+n)%n],b=L[i],rx=b.x-a.x,ry=b.y-a.y,det=-a.dx*b.dy+b.dx*a.dy;
    var s=(-rx*b.dy+b.dx*ry)/det;
    out.push([a.x+a.dx*s,a.y+a.dy*s]);
  }
  return out;
}

function computeGeometry(){
  var s2=Math.SQRT2,P={},i;
  P.A=[0,0]; P.B=[1,0];                              /* clause 1 */
  P.C=[0,4/3]; P.D=[0,1];                            /* clause 2: AC = AB + AB/3, AD = AB */
  P.E=[1-1/s2,1/s2];                                 /* clause 3: BE = AB along BD */
  P.F=[0,1/s2]; P.G=[1,1/s2];                        /* clause 4: FG through E, FG = AB */
  var slope=P.G[1]-P.C[1];                           /* clause 5: line CG, y = C.y + slope*x */
  P.H=[0.25,0];                                      /* clause 6: AH = AB/4 */
  P.I=[0.25,P.C[1]+slope*0.25];
  P.J=[0,(P.C[1]+P.F[1])/2];                         /* clause 7: bisect CF */
  P.K=[(P.J[1]-P.C[1])/slope,P.J[1]];
  P.L=[0.25,P.J[1]];                                 /* clause 8 */
  var sJG=(P.G[1]-P.J[1])/(P.G[0]-P.J[0]);           /* clause 9 */
  P.M=[0.25,P.J[1]+sJG*0.25];                        /* clause 10 */
  var MN=Math.abs(P.M[0]+P.M[1]-1)/s2;               /* clause 11: shortest distance from M to line BD (x+y=1) */
  P.N=[0.25,P.M[1]-MN];
  var sh=(P.M[0]+P.M[1]-1)/2; P.foot=[P.M[0]-sh,P.M[1]-sh];
  P.O=[0,P.M[1]];                                    /* clause 12 */
  var LN=P.L[1]-P.N[1],LM=P.L[1]-P.M[1];             /* clause 13 */
  var MQ=Math.sqrt(LN*LN-LM*LM);                     /* clause 14: P, Q = circle(L,LN) ∩ line OM */
  P.P=[0.25-MQ,P.M[1]]; P.Q=[0.25+MQ,P.M[1]];
  var a=(LN*LN-MN*MN+LN*LN)/(2*LN),h=Math.sqrt(LN*LN-a*a);   /* clause 15: circle(N,NM) ∩ circle(L,LN) */
  P.R=[0.25-h,P.L[1]-a]; P.S=[0.25+h,P.L[1]-a]; P.T=[0.25,P.L[1]-a];
  var TS=h,TM=P.M[1]-P.T[1];                         /* clauses 16, 17 */
  var dLT=P.L[1]-P.T[1],a2=(LN*LN-TM*TM+dLT*dLT)/(2*dLT),h2=Math.sqrt(LN*LN-a2*a2);
  P.X1=[0.25-h2,P.L[1]-a2]; P.X2=[0.25+h2,P.L[1]-a2];        /* arc 17 meets PNQ */
  P.U=[0,P.F[1]/2]; P.V=[1-P.U[1],P.U[1]]; P.W=[0.25,P.U[1]]; /* clauses 19, 20 */
  var w=P.T[1]-P.N[1];                               /* clause 23: border width = TN */
  var poly=[P.A,P.B,P.E,P.G,P.C],outer=offsetPoly(poly,w),x0=1e9,y0=1e9,x1=-1e9,y1=-1e9;
  for(i=0;i<outer.length;i++){x0=Math.min(x0,outer[i][0]);x1=Math.max(x1,outer[i][0]);y0=Math.min(y0,outer[i][1]);y1=Math.max(y1,outer[i][1]);}
  var G={P:P,MN:MN,LN:LN,MQ:MQ,TS:TS,TM:TM,w:w,poly:poly,outer:outer,bb:{x0:x0,y0:y0,x1:x1,y1:y1,w:x1-x0,h:y1-y0}};
  G.cx=(x0+x1)/2; G.cy=(y0+y1)/2; G.ratio=G.bb.h/G.bb.w;
  function ang(c,p){return Math.atan2(p[1]-c[1],p[0]-c[0]);}
  G.aP=ang(P.L,P.P); G.aQ=ang(P.L,P.Q);
  G.aSN=ang(P.N,P.S); G.aRN=ang(P.N,P.R);
  G.aX2=ang(P.T,P.X2); G.aX1L=ang(P.L,P.X1); G.aX2L=ang(P.L,P.X2);
  return G;
}
var G=computeGeometry();
if(typeof window!=='undefined'){window.NFC_GEOMETRY=computeGeometry;}

/* White emblem shapes (flag units) */
function whiteShapes(){
  var P=G.P,o={crescent:null,moonDisc:null,moonTris:[],sunDisc:null,sunTris:[]},k;
  o.crescent=arcPoints(P.M,G.MQ,Math.PI,2*Math.PI,72).concat(arcPoints(P.L,G.LN,G.aQ,G.aP,60));
  o.moonDisc=arcPoints(P.T,G.TM,G.aX2,Math.PI-G.aX2,64).concat(arcPoints(P.L,G.LN,G.aX1L,G.aX2L,24));
  for(k=0;k<8;k++){var a0=Math.PI*k/8,a1=Math.PI*(k+1)/8;o.moonTris.push([pol(P.T,G.TM,a0),pol(P.T,G.TS,(a0+a1)/2),pol(P.T,G.TM,a1)]);}
  o.sunDisc=arcPoints(P.W,G.MN,0,2*Math.PI,72);
  for(k=0;k<12;k++){var f=Math.PI/2+k*Math.PI/6;o.sunTris.push([pol(P.W,G.MN,f-Math.PI/12),pol(P.W,G.LN,f),pol(P.W,G.MN,f+Math.PI/12)]);}
  return o;
}
var WS=whiteShapes();

/* =========================================================
   2. CONSTANTS, TIMELINE
   ========================================================= */
var S=3.2;                         /* world units per AB */
var END=48,PH=[0,4,12.5,26.6,33,40,47];
var BW=1.7,BH=2.0,BX0=G.cx-BW/2,BY0=G.cy-BH/2;     /* blueprint board, flag units */
var CRIMSON='#dc143c',BLUE='#003893';
var PCAP=[],PH_LABEL=[];

var LBL={A:[-26,28],B:[16,28],C:[-28,-8],D:[-28,12],E:[-30,-14],F:[-28,8],G:[16,-6],H:[0,32],I:[14,-12],J:[-28,-8],K:[14,-12],L:[-6,30],M:[14,-10],N:[14,22],O:[-28,12],P:[-8,-18],Q:[12,-14],R:[-30,2],S:[14,2],T:[14,-12],U:[-28,8],V:[14,-14],W:[10,-14]};
var STY={
 solid:{c:'#ffe3a8',w:3.2,g:'rgba(255,205,120,.75)',gb:10,d:null},
 guide:{c:'rgba(125,205,255,.92)',w:1.7,d:[10,8]},
 comp:{c:'rgba(255,176,82,.95)',w:2.1,d:[3,6]},
 white:{c:'#ffffff',w:3,g:'rgba(255,255,255,.7)',gb:8,d:null},
 outline:{c:'#ffd27a',w:5,g:'rgba(255,190,90,.95)',gb:16,d:null}
};

var OPS=[],STEP_T=[];
(function build(){
  var P=G.P;
  function st(n,t){STEP_T[n-1]=t;}
  function ln(t0,d,a,b,s){OPS.push({k:'p',t0:t0,d:d,pts:[P[a],P[b]],s:s});}
  function pl(t0,d,pts,s){OPS.push({k:'p',t0:t0,d:d,pts:pts,s:s});}
  function pt(t0,n){OPS.push({k:'pt',t0:t0,n:n});}
  var PI=Math.PI;
  st(1,4.3);  ln(4.3,1.2,'A','B','solid'); pt(4.3,'A'); pt(5.4,'B');
  st(2,5.7);  ln(5.7,1.1,'A','C','solid'); pt(6.7,'C'); pl(6.9,.9,arcPoints(P.A,1,0,PI/2,48),'comp'); pt(7.8,'D'); ln(7.8,.7,'B','D','guide');
  st(3,8.4);  pl(8.4,.8,arcPoints(P.B,1,PI,3*PI/4,32),'comp'); pt(9.2,'E');
  st(4,9.3);  ln(9.3,1.0,'F','G','solid'); pt(9.3,'F'); pt(10.2,'G');
  st(5,10.3); ln(10.3,.9,'C','G','solid'); pl(11.2,1.2,[P.A,P.B,P.E,P.G,P.C,P.A],'outline');
  st(6,12.7); pt(12.7,'H'); ln(12.8,1.0,'H','I','guide'); pt(13.8,'I');
  st(7,14.0); pt(14.0,'J'); ln(14.1,.9,'J','K','guide'); pt(15.0,'K');
  st(8,15.1); pt(15.1,'L');
  st(9,15.5); ln(15.5,.9,'J','G','guide');
  st(10,16.4);pt(16.4,'M');
  st(11,16.8);ln(16.8,.5,'M','foot','guide'); pl(17.3,.6,arcPoints(P.M,G.MN,-3*PI/4,-PI/2,16),'comp'); pt(17.9,'N');
  st(12,18.1);pl(18.1,.9,[P.O,[0.5,P.M[1]]],'guide'); pt(18.1,'O');
  st(13,19.2);pl(19.2,1.1,arcPoints(P.L,G.LN,PI,2*PI,64),'comp'); pt(20.3,'P'); pt(20.3,'Q'); pl(20.3,.5,arcPoints(P.L,G.LN,G.aP,G.aQ,40),'solid');
  st(14,20.9);pl(20.9,1.0,arcPoints(P.M,G.MQ,PI,2*PI,64),'white');
  st(15,22.0);pl(22.0,.8,arcPoints(P.N,G.MN,G.aSN,G.aRN,40),'comp'); pt(22.8,'R'); pt(22.8,'S'); ln(22.8,.5,'R','S','guide'); pt(23.3,'T');
  st(16,23.5);pl(23.5,.9,arcPoints(P.T,G.TS,0,PI,48),'white');
  st(17,24.4);pl(24.4,.8,arcPoints(P.T,G.TM,G.aX2,PI-G.aX2,48),'white');
  st(18,25.3);
  st(19,26.8);pt(26.8,'U'); ln(26.9,.9,'U','V','guide'); pt(27.8,'V');
  st(20,28.0);pt(28.0,'W'); pl(28.1,.9,arcPoints(P.W,G.MN,PI/2,PI/2+2*PI,72),'comp');
  st(21,29.1);pl(29.1,1.0,arcPoints(P.W,G.LN,PI/2,PI/2+2*PI,96),'comp');
  st(22,30.3);
  st(23,33.1);ln(34.4,.8,'T','N','guide'); OPS.push({k:'tx',t0:35.0,x:P.T[0],y:P.T[1],s:'TN',dx:12,dy:-8});
  st(24,38.0);
})();

/* camera keyframes: time, azimuth°, elevation°, distance multiplier, target (flag units) */
var KF=[
 [0,-42,24,2.5,G.cx,G.cy],[4,-16,12,1.85,G.cx,G.cy],[8.5,-4,4,1.62,G.cx,G.cy],[12.4,0,3,1.55,G.cx,G.cy],
 [14,3,2,.62,.26,.93],[25.5,-2,2,.52,.26,.93],[27.8,2,2,.62,.26,.40],[32.4,0,2,.58,.26,.38],
 [34.4,0,3,1.5,G.cx,G.cy],[39.8,0,2,1.5,G.cx,G.cy],[43,26,9,1.55,G.cx,G.cy],[45.5,-12,6,1.4,G.cx,G.cy],[48,8,3,1.32,G.cx,G.cy]
];
function camPose(t){
  var i=0;while(i<KF.length-2&&t>KF[i+1][0])i++;
  var a=KF[i],b=KF[i+1],p=clamp((t-a[0])/(b[0]-a[0]),0,1);p=p*p*p*(p*(6*p-15)+10);
  var o={},k;for(k=1;k<6;k++)o[k]=a[k]+(b[k]-a[k])*p;
  return {az:o[1],el:o[2],dm:o[3],tx:o[4],ty:o[5]};
}

/* =========================================================
   3. 2D DRAWING (blueprint board, flag texture, fallback)
   ========================================================= */
function pathPoly(c,pts,X,Y){var i;c.moveTo(X(pts[0][0]),Y(pts[0][1]));for(i=1;i<pts.length;i++)c.lineTo(X(pts[i][0]),Y(pts[i][1]));c.closePath();}
function partialPts(pts,f){
  if(f>=1)return pts;
  var segs=[],tot=0,i,d;
  for(i=1;i<pts.length;i++){d=Math.hypot(pts[i][0]-pts[i-1][0],pts[i][1]-pts[i-1][1]);segs.push(d);tot+=d;}
  var tgt=tot*f,acc=0,out=[pts[0]];
  for(i=1;i<pts.length;i++){
    d=segs[i-1];
    if(acc+d>=tgt){var r=d?(tgt-acc)/d:0;out.push([pts[i-1][0]+(pts[i][0]-pts[i-1][0])*r,pts[i-1][1]+(pts[i][1]-pts[i-1][1])*r]);return out;}
    acc+=d;out.push(pts[i]);
  }
  return out;
}
function rrect(c,x,y,w,h,r){c.beginPath();c.moveTo(x+r,y);c.lineTo(x+w-r,y);c.quadraticCurveTo(x+w,y,x+w,y+r);c.lineTo(x+w,y+h-r);c.quadraticCurveTo(x+w,y+h,x+w-r,y+h);c.lineTo(x+r,y+h);c.quadraticCurveTo(x,y+h,x,y+h-r);c.lineTo(x,y+r);c.quadraticCurveTo(x,y,x+r,y);c.closePath();}

var bcv=null,bctx=null;
function makeBoard(cw){
  bcv=document.createElement('canvas');bcv.width=cw;bcv.height=Math.round(cw*BH/BW);bctx=bcv.getContext('2d');
  return bcv;
}

function drawBoard(t){
  var c=bctx,W=bcv.width,H=bcv.height,u=W/1024,head=null,i,o;
  function X(x){return (x-BX0)/BW*W;}
  function Y(y){return (BY0+BH-y)/BH*H;}
  c.setTransform(1,0,0,1,0,0);c.globalAlpha=1;c.setLineDash([]);c.shadowBlur=0;c.clearRect(0,0,W,H);
  c.lineCap='round';c.lineJoin='round';

  /* sheet */
  var pa=ss(t,1.0,2.4);
  if(pa>0){
    c.globalAlpha=pa;
    var gr=c.createRadialGradient(W/2,H/2,H*.1,W/2,H/2,H*.75);
    gr.addColorStop(0,'rgba(34,54,108,.80)');gr.addColorStop(1,'rgba(12,20,48,.90)');
    rrect(c,8*u,8*u,W-16*u,H-16*u,30*u);c.fillStyle=gr;c.fill();
    c.lineWidth=2*u;c.strokeStyle='rgba(140,175,255,.28)';c.stroke();
    c.globalAlpha=1;
  }
  /* grid, revealed outward from the centre */
  var rv=ss(t,1.6,4.2);
  if(rv>0){
    var step=0.05,i0=Math.ceil((BX0+0.02)/step),i1=Math.floor((BX0+BW-0.02)/step),j0=Math.ceil((BY0+0.02)/step),j1=Math.floor((BY0+BH-0.02)/step);
    var yA=G.cy+rv*BH/2*0.97,yB=G.cy-rv*BH/2*0.97,xA=G.cx-rv*BW/2*0.97,xB=G.cx+rv*BW/2*0.97;
    for(i=i0;i<=i1;i++){var gx=i*step,maj=(i%5===0);c.beginPath();c.moveTo(X(gx),Y(yA));c.lineTo(X(gx),Y(yB));c.lineWidth=(maj?1.4:.8)*u;c.strokeStyle=i===0?'rgba(255,210,122,.45)':'rgba(140,175,255,'+(maj?.2:.085)+')';c.stroke();}
    for(i=j0;i<=j1;i++){var gy=i*step,maj2=(i%5===0);c.beginPath();c.moveTo(X(xA),Y(gy));c.lineTo(X(xB),Y(gy));c.lineWidth=(maj2?1.4:.8)*u;c.strokeStyle=i===0?'rgba(255,210,122,.45)':'rgba(140,175,255,'+(maj2?.2:.085)+')';c.stroke();}
  }
  /* pennant tints */
  var pt=ss(t,11.4,12.3)*(1-ss(t,33.1,34.4));
  if(pt>0){
    var P=G.P;
    c.beginPath();pathPoly(c,[P.A,P.B,P.E,P.F],X,Y);c.fillStyle='rgba(70,185,215,'+(.30*pt)+')';c.fill();
    c.beginPath();pathPoly(c,[P.C,P.F,P.G],X,Y);c.fillStyle='rgba(255,190,90,'+(.28*pt)+')';c.fill();
  }
  /* crimson cloth: wipe from the hoist side */
  var cf=ss(t,33.2,35.8);
  if(cf>0){
    var wx=-0.06+cf*1.2;
    c.save();c.beginPath();c.rect(0,0,Math.max(0,X(wx)),H);c.clip();
    c.beginPath();pathPoly(c,G.poly,X,Y);c.fillStyle=CRIMSON;c.fill();c.restore();
    if(cf<1){var ed=c.createLinearGradient(X(wx)-30*u,0,X(wx)+4*u,0);ed.addColorStop(0,'rgba(255,220,160,0)');ed.addColorStop(1,'rgba(255,220,160,.9)');c.fillStyle=ed;c.fillRect(X(wx)-30*u,Y(G.bb.y1),34*u,Y(G.bb.y0)-Y(G.bb.y1));}
  }
  /* border grows outward to TN */
  var bf=ss(t,35.8,38.0);
  if(bf>0){
    c.beginPath();pathPoly(c,offsetPoly(G.poly,G.w*bf),X,Y);pathPoly(c,G.poly,X,Y);c.fillStyle=BLUE;c.fill('evenodd');
  }
  /* white emblems */
  function fp(pts,al){if(al<=0)return;c.globalAlpha=al;c.beginPath();pathPoly(c,pts,X,Y);c.fillStyle='#fff';c.fill();c.globalAlpha=1;}
  var mA=ss(t,25.3,26.0);fp(WS.crescent,mA);fp(WS.moonDisc,mA);
  for(i=0;i<8;i++)fp(WS.moonTris[i],ss(t,25.5+i*.09,25.85+i*.09));
  fp(WS.sunDisc,ss(t,30.3,31.0));
  for(i=0;i<12;i++)fp(WS.sunTris[i],ss(t,30.5+i*.13,30.85+i*.13));

  /* construction lines */
  var lA=1-ss(t,37.4,39.6),pts=[];
  c.globalAlpha=lA;
  for(i=0;i<OPS.length;i++){
    o=OPS[i];if(t<o.t0)continue;
    if(o.k!=='p'){pts.push(o);continue;}
    var f=ss(t,o.t0,o.t0+o.d),sty=STY[o.s],pp=partialPts(o.pts,f),j;
    if(pp.length<2)continue;
    c.beginPath();c.moveTo(X(pp[0][0]),Y(pp[0][1]));for(j=1;j<pp.length;j++)c.lineTo(X(pp[j][0]),Y(pp[j][1]));
    c.lineWidth=sty.w*u;c.strokeStyle=sty.c;c.setLineDash(sty.d?[sty.d[0]*u,sty.d[1]*u]:[]);
    if(sty.g){c.shadowColor=sty.g;c.shadowBlur=sty.gb*u;}
    c.stroke();c.shadowBlur=0;
    if(f>0&&f<1)head=pp[pp.length-1];
  }
  c.setLineDash([]);
  /* points and labels */
  c.font='700 '+(21*u)+'px Inter,system-ui,sans-serif';c.textAlign='center';c.textBaseline='middle';
  for(i=0;i<pts.length;i++){
    o=pts[i];var al=ss(t,o.t0,o.t0+.35)*lA;if(al<=0)continue;
    c.globalAlpha=al;
    if(o.k==='pt'){
      var p=G.P[o.n],d=LBL[o.n]||[12,-12],px=X(p[0]),py=Y(p[1]);
      c.beginPath();c.arc(px,py,4.4*u,0,6.2832);c.fillStyle='#ffd27a';c.fill();
      c.lineWidth=4*u;c.strokeStyle='rgba(8,12,30,.92)';c.strokeText(o.n,px+d[0]*u,py+d[1]*u);
      c.fillStyle='#eef3ff';c.fillText(o.n,px+d[0]*u,py+d[1]*u);
    }else{
      var tx=X(o.x)+o.dx*u,ty=Y(o.y)+o.dy*u;
      c.lineWidth=4*u;c.strokeStyle='rgba(8,12,30,.92)';c.strokeText(o.s,tx,ty);c.fillStyle='#8fd8ff';c.fillText(o.s,tx,ty);
    }
  }
  c.globalAlpha=1;
  return head;
}

/* Final cloth texture (and static fallback). weave=true adds a fine cloth pattern. */
function drawFlagCanvas(ctx,cw,ch,weave){
  var bb=G.bb,k;
  function X(x){return (x-bb.x0)/bb.w*cw;}
  function Y(y){return (bb.y1-y)/bb.h*ch;}
  ctx.clearRect(0,0,cw,ch);
  ctx.beginPath();pathPoly(ctx,G.outer,X,Y);ctx.fillStyle=BLUE;ctx.fill();
  ctx.beginPath();pathPoly(ctx,G.poly,X,Y);ctx.fillStyle=CRIMSON;ctx.fill();
  ctx.fillStyle='#fff';
  var all=[WS.crescent,WS.moonDisc,WS.sunDisc].concat(WS.moonTris,WS.sunTris);
  for(k=0;k<all.length;k++){ctx.beginPath();pathPoly(ctx,all[k],X,Y);ctx.fill();}
  if(weave){
    var tile=document.createElement('canvas');tile.width=tile.height=10;var tc=tile.getContext('2d');
    tc.fillStyle='rgba(0,0,0,.035)';tc.fillRect(0,0,5,5);tc.fillRect(5,5,5,5);
    tc.fillStyle='rgba(255,255,255,.02)';tc.fillRect(5,0,5,5);tc.fillRect(0,5,5,5);
    ctx.globalCompositeOperation='source-atop';ctx.fillStyle=ctx.createPattern(tile,'repeat');ctx.fillRect(0,0,cw,ch);ctx.globalCompositeOperation='source-over';
  }
}
function makeBump(){
  var cv=document.createElement('canvas');cv.width=cv.height=1024;var c=cv.getContext('2d');
  c.fillStyle='#808080';c.fillRect(0,0,1024,1024);
  var tile=document.createElement('canvas');tile.width=tile.height=8;var t=tile.getContext('2d');
  t.fillStyle='#9a9a9a';t.fillRect(0,0,4,4);t.fillRect(4,4,4,4);t.fillStyle='#666';t.fillRect(4,0,4,4);t.fillRect(0,4,4,4);
  c.fillStyle=c.createPattern(tile,'repeat');c.fillRect(0,0,1024,1024);
  return cv;
}


var root=document.getElementById('nfc');
if(!root)return;
var I={};try{I=JSON.parse(root.getAttribute('data-i18n')||'{}');}catch(e){}
var NE=(root.getAttribute('lang')||document.documentElement.lang||'en').slice(0,2)==='ne';
var DG='०१२३४५६७८९';function nd(n){n=String(n);return NE?n.replace(/[0-9]/g,function(d){return DG.charAt(+d);}):n;}
function tr(k,d){return I[k]!==undefined?I[k]:d;}

/* =========================================================
   4. UI, STATE
   ========================================================= */
(function(){var pc=I.pcap||[];var EN_PC=[{"t": "Start with one unit", "x": "Schedule 1 builds the flag from straight lines, arcs and circles. Every length comes from the base line AB."}, {"t": "The shape · clauses 1–5", "x": "Two stacked pennants, drawn with a ruler and a compass."}, {"t": "The moon · clauses 6–18", "x": "A crescent that cradles a fan of eight rays."}, {"t": "The sun · clauses 19–22", "x": "A twelve-rayed sun, built from two circles."}, {"t": "Border and cloth · clauses 23–24", "x": "Crimson cloth, then a deep blue border as wide as TN."}, {"t": "From pattern to cloth", "x": "The finished pattern becomes a flag. Its outline is the two pennants you just drew."}, {"t": "The national flag of Nepal", "x": "Drag to look around. Use Replay to watch it built again."}];var EN_PH=["Grid", "Shape", "Moon", "Sun", "Border and cloth", "3D flag", "Full view"];for(var q=0;q<7;q++){PCAP.push(pc[q]||EN_PC[q]);PH_LABEL.push((I.ph&&I.ph[q])||EN_PH[q]);}})();
var stage=document.getElementById('nfc-stage'),canvas=document.getElementById('nfc-canvas'),loadEl=document.getElementById('nfc-load');
var elClause=document.getElementById('nfc-clause'),elTitle=document.getElementById('nfc-ctitle'),elText=document.getElementById('nfc-ctext');
var scrub=document.getElementById('nfc-scrub'),btnPlay=document.getElementById('nfc-play'),sr=document.getElementById('nfc-sr');
var chips=root.querySelectorAll('.nfc-chip');
var stepEls=root.querySelectorAll('#nfc-steps li'),STEP_TITLE=[],STEP_TEXT=[],i;
for(i=0;i<stepEls.length;i++){var sg=stepEls[i].querySelector('strong');STEP_TITLE.push(sg?sg.textContent:'');STEP_TEXT.push(stepEls[i].textContent.replace(sg?sg.textContent:'','').replace(/^\s+/,''));}

var reduced=window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches;
var coarse=window.matchMedia&&window.matchMedia('(pointer: coarse)').matches;
var small=Math.min(window.innerWidth,window.innerHeight)<700||coarse;
var lowPower=small||(navigator.hardwareConcurrency&&navigator.hardwareConcurrency<=4);

var t=reduced?END:0,windT=2.2,playing=false,speed=1,visible=false,started=false,ready=false,userCam=false,zoomMul=1,orbitOn=!coarse;
var THREE=null,renderer,scene,camera,controls,board,btex,cloth,cgeo,cbx,cby,cmat,pole,floorGrid,backGrid,wall,hemi,key,rim,pen,dust,dustP,d0=10,raf=0,last=0,dirty=true,lastBoardT=-1,lastHead=null,lastPhase=-1,lastCap='',fpsAcc=0,fpsN=0,scrubbing=false,wasPlaying=false;

function phaseIndex(x){var k=0;for(var j=0;j<PH.length;j++)if(x>=PH[j])k=j;return k;}
function setCaption(cl,ti,tx){var key=cl+'|'+ti;if(key===lastCap)return;lastCap=key;elClause.textContent=cl;elTitle.textContent=ti;elText.textContent=tx;}
function syncUI(){
  var ic=document.getElementById('nfc-play-ic'),tt=document.getElementById('nfc-play-t'),atEnd=t>=END-0.001;
  if(playing){ic.setAttribute('d','M7 5v14M17 5v14');tt.textContent=tr('pause','Pause');btnPlay.setAttribute('aria-label',tr('pause','Pause'));}
  else{ic.setAttribute('d',atEnd?'M3 12a9 9 0 1 0 3-6.7M3 4v5h5':'M7 4l12 8-12 8z');tt.textContent=atEnd?tr('replay','Replay'):tr('play','Play');btnPlay.setAttribute('aria-label',atEnd?tr('replayAria','Replay from the start'):tr('play','Play'));var rb=document.getElementById('nfc-replay');if(rb)rb.hidden=atEnd;}
}
function updateUI(){
  var pi=phaseIndex(t);
  if(pi!==lastPhase){
    lastPhase=pi;
    for(var j=0;j<chips.length;j++){if(j===pi)chips[j].setAttribute('aria-current','step');else chips[j].removeAttribute('aria-current');}
    sr.textContent=PH_LABEL[pi]+'. '+PCAP[pi].t+'. '+PCAP[pi].x;
  }
  var n=0;if(pi>=1&&pi<=4){for(var k=0;k<24;k++){if(STEP_T[k]!==undefined&&t>=STEP_T[k])n=k+1;}}
  if(n>0)setCaption(tr('clause','Clause {n} of 24').replace('{n}',nd(n)),STEP_TITLE[n-1],STEP_TEXT[n-1]);else setCaption('',PCAP[pi].t,PCAP[pi].x);
  stage.classList.toggle('nfc-final',t>=END-0.8);
  if(!scrubbing)scrub.value=t;
}

function seek(x,keepPlay){t=clamp(x,0,END);userCam=false;zoomMul=1;lastBoardT=-1;dirty=true;if(!keepPlay)playing=false;syncUI();updateUI();kick();}
function play(){if(!ready)return;if(t>=END-0.001)t=0;userCam=false;playing=true;syncUI();kick();}
function pause(){playing=false;syncUI();}
function replay(){t=0;zoomMul=1;userCam=false;lastBoardT=-1;if(controls)controls.enableZoom=false;playing=true;dirty=true;syncUI();updateUI();kick();}
btnPlay.addEventListener('click',function(){if(playing)pause();else play();});
document.getElementById('nfc-replay').addEventListener('click',function(){replay();});
document.getElementById('nfc-end').addEventListener('click',function(){seek(END);});
document.getElementById('nfc-speed').addEventListener('click',function(){speed=speed===1?2:1;this.textContent=nd(speed)+'×';this.setAttribute('aria-label',tr('speedAria','Playback speed {n} times').replace('{n}',nd(speed)));});
for(i=0;i<chips.length;i++){chips[i].addEventListener('click',(function(j){return function(){seek(j===6?END:PH[j]+0.02,!reduced&&j!==6);if(j!==6&&!reduced){playing=true;syncUI();}};})(i));}
scrub.addEventListener('input',function(){if(!scrubbing){scrubbing=true;wasPlaying=playing;playing=false;}seek(parseFloat(scrub.value),false);});
scrub.addEventListener('change',function(){scrubbing=false;if(wasPlaying&&t<END-0.001){playing=true;}syncUI();kick();});
document.getElementById('nfc-orbit').addEventListener('click',function(){orbitOn=!orbitOn;this.setAttribute('aria-pressed',orbitOn?'true':'false');applyOrbit();});
function zoomBy(f){
  if(!ready)return;
  if(userCam){var v=camera.position.clone().sub(controls.target).multiplyScalar(f);camera.position.copy(controls.target).add(v);}
  else zoomMul=clamp(zoomMul*f,.5,2.4);
  dirty=true;kick();
}
document.getElementById('nfc-zin').addEventListener('click',function(){zoomBy(.82);});
document.getElementById('nfc-zout').addEventListener('click',function(){zoomBy(1.22);});

function pseudo(on){stage.classList.toggle('nfc-pseudo',on);document.documentElement.style.overflow=on?'hidden':'';}
document.getElementById('nfc-fs').addEventListener('click',toggleFS);
function toggleFS(){
  var fe=document.fullscreenElement||document.webkitFullscreenElement;
  if(!fe&&!stage.classList.contains('nfc-pseudo')){
    var rq=stage.requestFullscreen||stage.webkitRequestFullscreen;
    if(rq){try{var pr=rq.call(stage);if(pr&&pr.catch)pr.catch(function(){pseudo(true);});}catch(e){pseudo(true);}}else pseudo(true);
  }else{
    if(fe){(document.exitFullscreen||document.webkitExitFullscreen).call(document);}
    pseudo(false);
  }
}
['fullscreenchange','webkitfullscreenchange'].forEach(function(ev){document.addEventListener(ev,function(){dirty=true;});});
document.addEventListener('keydown',function(e){if(e.key==='Escape'&&stage.classList.contains('nfc-pseudo'))pseudo(false);});
stage.addEventListener('keydown',function(e){
  if(e.target&&e.target.tagName==='INPUT')return;
  var k=e.key;
  if(k===' '&&e.target===stage){e.preventDefault();if(playing)pause();else play();}
  else if(k==='ArrowRight'){e.preventDefault();var p=phaseIndex(t);seek(p>=5?END:PH[p+1]+0.02,true);}
  else if(k==='ArrowLeft'){e.preventDefault();var q=phaseIndex(t);seek(t-PH[q]>1.5?PH[q]:PH[Math.max(0,q-1)],true);}
  else if(k==='r'||k==='R'){replay();}
  else if(k==='f'||k==='F'){toggleFS();}
});

/* =========================================================
   5. THREE.JS SCENE
   ========================================================= */
function loadScript(src){
  return new Promise(function(res,rej){
    var s=document.createElement('script');s.src=src;s.async=true;s.crossOrigin='anonymous';
    s.onload=res;s.onerror=function(){rej(new Error('load '+src));};document.head.appendChild(s);
  });
}
function glowTexture(){
  var cv=document.createElement('canvas');cv.width=cv.height=64;var c=cv.getContext('2d');
  var g=c.createRadialGradient(32,32,0,32,32,32);g.addColorStop(0,'rgba(255,255,255,1)');g.addColorStop(.25,'rgba(255,214,140,.7)');g.addColorStop(1,'rgba(255,200,120,0)');
  c.fillStyle=g;c.fillRect(0,0,64,64);return new THREE.CanvasTexture(cv);
}
function frameD(aspect){
  var th=Math.tan(camera.fov*Math.PI/360),h=G.bb.h*S/2/(0.88*th),w=G.bb.w*S/2/(0.88*th*aspect);
  return Math.max(h,w);
}
function applyOrbit(){
  if(!controls)return;
  controls.enabled=orbitOn;canvas.style.touchAction=orbitOn?'none':'pan-y';canvas.style.cursor=orbitOn?'grab':'default';
  if(!orbitOn){controls.enableZoom=false;}
}

function init3D(){
  THREE=window.THREE;
  try{renderer=new THREE.WebGLRenderer({canvas:canvas,antialias:true,alpha:true,powerPreference:'high-performance'});}
  catch(e){throw new Error('webgl');}
  renderer.setClearColor(0x000000,0);
  renderer.setPixelRatio(Math.min(window.devicePixelRatio||1,small?1.5:2));
  renderer.outputEncoding=THREE.sRGBEncoding;
  renderer.toneMapping=THREE.ACESFilmicToneMapping;renderer.toneMappingExposure=.9;
  renderer.shadowMap.enabled=true;renderer.shadowMap.type=THREE.PCFSoftShadowMap;

  scene=new THREE.Scene();
  camera=new THREE.PerspectiveCamera(32,1,0.1,160);
  if(THREE.OrbitControls){
    controls=new THREE.OrbitControls(camera,canvas);
    controls.enableDamping=true;controls.dampingFactor=.08;controls.enablePan=false;controls.rotateSpeed=.7;controls.zoomSpeed=.8;
    controls.minDistance=2.5;controls.maxDistance=34;controls.minPolarAngle=.25;controls.maxPolarAngle=Math.PI*.64;
    controls.enableZoom=false;
    controls.addEventListener('start',function(){userCam=true;dirty=true;kick();});
    controls.addEventListener('change',function(){dirty=true;});
    canvas.addEventListener('pointerdown',function(){if(orbitOn)controls.enableZoom=true;});
    canvas.addEventListener('pointerleave',function(){controls.enableZoom=false;});
  }else{orbitOn=false;document.getElementById('nfc-orbit').style.display='none';}

  /* lights */
  hemi=new THREE.HemisphereLight(0xbfd4ff,0x1a1428,.5);scene.add(hemi);
  key=new THREE.DirectionalLight(0xfff1dd,2.2);key.position.set(5,6,8);key.castShadow=true;
  var ms=lowPower?1024:2048;key.shadow.mapSize.set(ms,ms);
  var sc=key.shadow.camera;sc.left=-7;sc.right=7;sc.top=7;sc.bottom=-7;sc.near=1;sc.far=34;
  key.shadow.bias=-0.0008;key.shadow.normalBias=0.03;scene.add(key);
  rim=new THREE.DirectionalLight(0x6fa0ff,.9);rim.position.set(-6,3,-5);scene.add(rim);

  /* blueprint board */
  btex=new THREE.CanvasTexture(makeBoard(small?800:1280));
  btex.encoding=THREE.sRGBEncoding;btex.minFilter=THREE.LinearFilter;btex.generateMipmaps=false;
  board=new THREE.Mesh(new THREE.PlaneGeometry(BW*S,BH*S),new THREE.MeshBasicMaterial({map:btex,transparent:true,depthWrite:false,toneMapped:false}));
  board.position.z=-0.03;board.renderOrder=1;scene.add(board);

  /* 3D construction grids */
  var floorY=-(BH/2+0.12)*S;
  floorGrid=new THREE.GridHelper(60,120,0x4f7cff,0x24366e);floorGrid.position.y=floorY;floorGrid.material.transparent=true;floorGrid.material.opacity=0;floorGrid.material.depthWrite=false;scene.add(floorGrid);
  backGrid=new THREE.GridHelper(44,88,0x4f7cff,0x1d2c5e);backGrid.rotation.x=Math.PI/2;backGrid.position.z=-6;backGrid.material.transparent=true;backGrid.material.opacity=0;backGrid.material.depthWrite=false;scene.add(backGrid);

  /* shadow-catching backdrop */
  wall=new THREE.Mesh(new THREE.PlaneGeometry(70,46),new THREE.ShadowMaterial({opacity:0}));wall.position.z=-2.4;wall.receiveShadow=true;scene.add(wall);

  /* cloth */
  var cw=small?1024:1536,ch=Math.round(cw*G.bb.h/G.bb.w),cv=document.createElement('canvas');cv.width=cw;cv.height=ch;
  drawFlagCanvas(cv.getContext('2d'),cw,ch,false);
  var ctex=new THREE.CanvasTexture(cv);ctex.encoding=THREE.sRGBEncoding;ctex.minFilter=THREE.LinearFilter;ctex.generateMipmaps=false;
  var bump=new THREE.CanvasTexture(makeBump());bump.wrapS=bump.wrapT=THREE.RepeatWrapping;
  var NX=lowPower?48:72,NY=Math.round(NX*G.bb.h/G.bb.w);
  var bwW=G.bb.w*S,bhW=G.bb.h*S;
  cgeo=new THREE.PlaneGeometry(bwW,bhW,NX,NY);
  var pos=cgeo.attributes.position,n=pos.count;cbx=new Float32Array(n);cby=new Float32Array(n);
  for(i=0;i<n;i++){cbx[i]=(pos.getX(i)+bwW/2)/S;cby[i]=pos.getY(i)/S;}
  cmat=new THREE.MeshStandardMaterial({map:ctex,roughness:.9,metalness:0,side:THREE.DoubleSide,alphaTest:.5,transparent:true});
  cloth=new THREE.Mesh(cgeo,cmat);cloth.castShadow=true;cloth.receiveShadow=true;cloth.frustumCulled=false;
  cloth.customDepthMaterial=new THREE.MeshDepthMaterial({depthPacking:THREE.RGBADepthPacking,map:ctex,alphaTest:.5});
  cloth.visible=false;scene.add(cloth);

  /* pole, rings, finial */
  pole=new THREE.Group();
  var px=-(G.bb.w/2)*S-0.075,topY=bhW/2+0.9,metal=new THREE.MeshStandardMaterial({color:0xc9ccd6,metalness:.55,roughness:.38}),gold=new THREE.MeshStandardMaterial({color:0xd9a548,metalness:.6,roughness:.34});
  var cyl=new THREE.Mesh(new THREE.CylinderGeometry(.055,.065,24,28),metal);cyl.position.set(px,topY-12,0);cyl.castShadow=true;pole.add(cyl);
  var fin=new THREE.Mesh(new THREE.SphereGeometry(.14,28,18),gold);fin.position.set(px,topY+.1,0);fin.castShadow=true;pole.add(fin);
  var col=new THREE.Mesh(new THREE.TorusGeometry(.075,.018,10,28),gold);col.rotation.x=Math.PI/2;col.position.set(px,topY-.08,0);pole.add(col);
  [-.78,-.1,.62].forEach(function(f){var rg=new THREE.Mesh(new THREE.TorusGeometry(.088,.013,10,28),gold);rg.rotation.x=Math.PI/2;rg.position.set(px,f*bhW/2,0);rg.castShadow=true;pole.add(rg);});
  pole.visible=false;scene.add(pole);

  /* drawing-tip glow and floating dust for depth */
  var gt=glowTexture();
  pen=new THREE.Sprite(new THREE.SpriteMaterial({map:gt,color:0xffd27a,blending:THREE.AdditiveBlending,depthWrite:false,transparent:true}));pen.scale.set(.42,.42,1);pen.renderOrder=3;pen.visible=false;scene.add(pen);
  var dn=small?70:150,dp=new Float32Array(dn*3);
  for(i=0;i<dn;i++){dp[3*i]=(Math.random()-.5)*22;dp[3*i+1]=(Math.random()-.5)*14;dp[3*i+2]=-5+Math.random()*9;}
  var dg=new THREE.BufferGeometry();dg.setAttribute('position',new THREE.BufferAttribute(dp,3));dustP=dp;
  dust=new THREE.Points(dg,new THREE.PointsMaterial({size:.09,map:gt,color:0x9fb8ff,transparent:true,opacity:.5,depthWrite:false,blending:THREE.AdditiveBlending}));dust.frustumCulled=false;scene.add(dust);

  resize();applyOrbit();
}

function resize(){
  if(!renderer)return;
  var r=stage.getBoundingClientRect(),w=Math.max(2,Math.floor(r.width)),h=Math.max(2,Math.floor(r.height));
  renderer.setSize(w,h,false);camera.aspect=w/h;camera.updateProjectionMatrix();d0=frameD(w/h);dirty=true;
}

function updateCloth(tt,amp){
  var pos=cgeo.attributes.position,a=pos.array,n=pos.count,bw=G.bb.w,half=bw/2,k,xf,yf,env,z,dx,dy;
  for(k=0;k<n;k++){
    xf=cbx[k];yf=cby[k];
    env=Math.pow(xf/bw,1.2)*amp;
    z=env*0.105*(0.62*Math.sin(6.2*xf-2.6*tt+1.1*yf)+0.30*Math.sin(10.8*xf-4.4*tt+2.5*yf+1.7)+0.20*Math.sin(3.4*yf-1.7*tt+1.8*xf));
    dx=-1.6*z*z;dy=-0.045*env;
    a[3*k]=(xf+dx-half)*S;a[3*k+1]=(yf+dy)*S;a[3*k+2]=z*S;
  }
  pos.needsUpdate=true;cgeo.computeVertexNormals();
}

function placeCamera(){
  var q=camPose(t),sway=(!reduced&&t>=END-0.01)?Math.sin(windT*.35)*5:0;
  var d=d0*q.dm*zoomMul,az=(q.az+sway)*Math.PI/180,el=q.el*Math.PI/180;
  var tx=(q.tx-G.cx)*S,ty=(q.ty-G.cy)*S;
  camera.position.set(tx+Math.sin(az)*Math.cos(el)*d,ty+Math.sin(el)*d,Math.cos(az)*Math.cos(el)*d);
  camera.lookAt(tx,ty,0);
  if(controls)controls.target.set(tx,ty,0);
}

function applyTime(){
  /* board */
  var boardOn=t<42.3;
  board.visible=boardOn;
  if(boardOn){
    board.material.opacity=ss(t,0.8,2.0)*(1-ss(t,40.8,42.2));
    if(lastBoardT!==t){lastHead=drawBoard(t);btex.needsUpdate=true;lastBoardT=t;}
  }
  /* pen glow */
  if(lastHead&&boardOn&&t<40&&playing){pen.visible=true;pen.position.set((lastHead[0]-G.cx)*S,(lastHead[1]-G.cy)*S,0.05);var pz=.38+.06*Math.sin(windT*9);pen.scale.set(pz,pz,1);}else pen.visible=false;
  /* grids */
  var gA=ss(t,0.2,2.4)*(1-ss(t,40,42.5));
  floorGrid.material.opacity=.6*gA;backGrid.material.opacity=.28*gA;
  floorGrid.position.y=-(BH/2+0.12)*S-(1-ss(t,0.2,3.2))*1.4;
  floorGrid.visible=backGrid.visible=gA>0.002;
  /* cloth, pole, light */
  var clothOn=t>=39.9;cloth.visible=clothOn;pole.visible=t>=40.2;
  var amp=reduced?0.45:ss(t,40.3,45);
  if(clothOn){
    var op=ss(t,40,41.3);cmat.opacity=op;cmat.transparent=op<.999;
    updateCloth(reduced?2.2:windT,amp);
  }
  var slide=1-(1-Math.pow(1-ss(t,40.3,43.3),3));pole.position.y=-(1-ss(t,40.3,43.3))*6;
  var lk=ss(t,40,43.5);hemi.intensity=.15+.3*lk;key.intensity=.4+1.25*lk;rim.intensity=.2+.7*lk;
  wall.material.opacity=.5*ss(t,41.5,45);
  dust.material.opacity=.5*(1-.6*ss(t,40,44));
  placeCamera();
}

function frame(now){
  raf=0;
  if(!visible||document.hidden||!ready)return;
  var dt=Math.min(.1,(now-last)/1000);last=now;
  var moving=playing||(!reduced);
  if(playing){t+=dt*speed;if(t>=END){t=END;playing=false;syncUI();}dirty=true;updateUI();}
  if(!reduced){windT+=dt;
    var dp=dust.geometry.attributes.position;for(var k=0;k<dp.count;k++){var y=dp.array[3*k+1]+dt*.12;if(y>7)y=-7;dp.array[3*k+1]=y;}dp.needsUpdate=true;
    dirty=true;
  }
  if(dirty||(controls&&(userCam))){
    applyTime();
    if(controls&&userCam)controls.update();
    renderer.render(scene,camera);dirty=false;
    /* adaptive resolution: drop pixel ratio if the device is struggling */
    fpsAcc+=dt;fpsN++;
    if(fpsN===90){if(fpsAcc/fpsN>.03&&renderer.getPixelRatio()>1){renderer.setPixelRatio(1);resize();}fpsAcc=0;fpsN=1e9;}
  }
  if(moving||dirty||userCam)kick();else if(reduced)kick();
}
function kick(){if(!raf&&visible&&ready){last=performance.now();raf=requestAnimationFrame(frame);}}

/* =========================================================
   6. BOOT (lazy), FALLBACK
   ========================================================= */
function showFallback(msg){
  root.classList.add('nfc-nogl');
  var fc=document.getElementById('nfc-fbc');drawFlagCanvas(fc.getContext('2d'),fc.width,fc.height,false);
  if(msg)document.getElementById('nfc-fbmsg').textContent=msg;
  var d=document.getElementById('nfc-steps');if(d)d.open=true;
}
var booted=false;
function boot(){
  if(booted)return;booted=true;
  loadEl.textContent=tr('preparing','Preparing the 3D scene…');
  var p=window.THREE?Promise.resolve():loadScript('https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js');
  p.then(function(){return window.THREE.OrbitControls?null:loadScript('https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/controls/OrbitControls.js').catch(function(){return null;});})
   .then(function(){
     init3D();ready=true;loadEl.classList.add('nfc-off');
     scrub.max=END;syncUI();updateUI();dirty=true;
     if('ResizeObserver' in window){new ResizeObserver(resize).observe(stage);}else window.addEventListener('resize',resize);
     if(visible){autoStart();kick();}
   })
   .catch(function(err){showFallback(err&&err.message==='webgl'?null:tr('libFail','The 3D library could not be loaded. This is the flag, drawn flat to the same geometry. The 24 steps are written out below.'));});
}
function autoStart(){
  if(started)return;started=true;
  if(reduced){t=END;playing=false;}else{t=0;playing=true;}
  syncUI();updateUI();dirty=true;
}
if('IntersectionObserver' in window){
  new IntersectionObserver(function(en){
    visible=en[0].isIntersecting;
    if(visible){boot();if(ready){if(en[0].intersectionRatio>0.3)autoStart();kick();}}
  },{rootMargin:'300px 0px',threshold:[0,0.3]}).observe(stage);
}else{visible=true;boot();}
if(reduced){scrub.value=END;lastPhase=-1;}
syncUI();updateUI();
})();
