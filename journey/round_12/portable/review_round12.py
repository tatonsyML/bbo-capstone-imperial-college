import os, sys, warnings, json, csv, time
from pathlib import Path
import numpy as np
from scipy.optimize import minimize
from scipy.stats import norm, qmc, spearmanr
from sklearn.preprocessing import StandardScaler,PowerTransformer
from sklearn.decomposition import PCA, KernelPCA
from sklearn.pipeline import Pipeline
from sklearn.linear_model import Ridge, BayesianRidge
from sklearn.cross_decomposition import PLSRegression
from sklearn.ensemble import ExtraTreesRegressor, IsolationForest, RandomForestRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import Matern,RBF
from sklearn.cluster import KMeans
from sklearn.metrics import mean_absolute_error
warnings.filterwarnings('ignore')
P=Path(__file__).resolve().parent; rng=np.random.default_rng(12026)
W11={2:([.692,.366],.6953368270741286),3:([.4455,.593,.42],-.005709220275560069),4:([.415,.417,.3665,.413],.7304594213260924),6:([.457,.37,.642,.738,.02],-.12376148016289273)}
ORIG={2:[.696286,.488640],3:[.489838,.498896,.486446],4:[.418700,.415988,.363637,.413858],6:[.401093,.323286,.666764,.777577,.090679]}
PREV_BAD={2:[.683311,.366084],3:[.313581,.474345,.485191],4:[.376347,.414508,.41858,.417207],6:[.401093,.323286,.666764,.777577,.090679]}
F4_TXT='''O.896981,.725628,.175404,.701694,-22.108287785;O.889356,.499588,.539269,.508783,-14.601396632;O.250946,.033693,.145380,.494932,-11.699932464;O.346962,.006250,.760564,.613024,-16.053765111;O.124871,.129770,.384400,.287076,-10.069633426;O.801303,.500231,.706645,.195103,-15.487082538;O.247708,.060445,.042186,.441324,-12.681684977;O.746702,.757092,.369353,.206566,-16.026399769;O.400665,.072574,.886768,.243842,-17.049234648;O.626071,.586751,.438806,.778858,-12.741765988;O.957135,.597644,.766114,.776210,-27.316396356;O.732812,.145250,.476813,.133366,-13.527648872;O.655115,.072392,.687152,.081517,-16.679115197;O.219734,.832031,.482864,.082569,-16.507158564;O.488594,.211965,.939178,.376192,-17.817999339;O.167130,.876555,.217240,.959801,-26.561820830;O.216911,.166086,.241372,.770062,-12.758324217;O.387488,.804532,.751795,.723827,-19.441557624;O.985622,.666853,.156982,.856535,-28.903273674;O.037825,.664853,.161982,.253924,-13.702746938;O.683486,.902770,.335219,.999483,-29.427091402;O.170347,.756959,.276660,.531231,-11.565741990;O.859657,.919592,.206139,.097797,-26.857786438;O.282138,.505987,.530231,.096302,-7.966775351;O.326076,.472367,.453192,.105887,-6.702089255;O.948389,.894513,.851638,.552196,-32.625660216;O.664955,.046566,.116777,.793718,-19.989497927;O.577766,.428772,.425826,.249007,-4.025542282;O.738613,.482103,.709366,.503970,-13.122782332;O.854811,.493965,.735310,.808092,-23.139428398;O.531500,.448817,.362651,.331977,-1.910544237;O.415636,.429159,.368928,.413098,.647554265;O.398136,.414095,.370552,.440336,.314899862;O.425128,.426376,.368659,.411895,.646639136;O.420382,.427768,.368794,.412497,.658926959;O.420290,.427795,.368797,.412509,.658922504;O.420383,.427768,.368794,.412497,.658924003;O.420381,.427768,.368794,.412497,.658929913;O.420380,.427768,.368794,.412497,.658932867;O.420370,.427768,.368794,.412497,.658962354;E.440000,.420000,.370000,.400000,.365463807;E.410000,.380000,.305000,.350000,-.74722931;E.460000,.430000,.400000,.430000,-.237497565;E.435000,.415000,.365000,.400000,.501167114;E.426000,.406000,.356000,.400000,.596908028;E.417000,.397000,.347000,.407000,.541206093;E.396000,.389000,.383000,.398000,-.028133669;E.426000,.406000,.356000,.407000,.640141321;E.426000,.425300,.351700,.425900,.576667591;E.427000,.410000,.349000,.416000,.624818384;E.427000,.411200,.353300,.410100,.654867548;V.527370,.436077,.336338,.317217,-1.979354675;V.476940,.443354,.246876,.385434,-2.648138698;V.431000,.412700,.323700,.354900,.067770085;V.376347,.414508,.418580,.417207,.681621478;V.391000,.508000,.386700,.411900,-1.616150338;V.398621,.345798,.387083,.394624,.189107653;V.308696,.396405,.376468,.387884,-1.421886965;V.376000,.415000,.480000,.480000,-2.253656590;V.430200,.411700,.420000,.374800,.597690763;V.403000,.413000,.419500,.396000,.553131420;V.375000,.404200,.388900,.414900,.397415825;V.376000,.405000,.419000,.417000,.625826526;V.376347,.414508,.418580,.417207,.681621478;H.375000,.375000,.625000,.875000,-14.616446420;H.415040,.438250,.314630,.454846,-.772914556;H.772250,.388419,.626561,.531030,-11.937068150;H.427294,.410692,.305139,.362151,-.517297309;H.427294,.410692,.305139,.332151,-.712513388;H.427294,.410692,.305139,.372151,-.636899936;H.427294,.410692,.305139,.352151,-.472528901;H.427294,.410692,.305139,.342151,-.536124496;H.427294,.410692,.305139,.353020,-.472329137;H.427294,.410692,.305139,.354270,-.473488039;H.427294,.410692,.305139,.352760,-.472301853'''

def source_data(f, omit_week11=False):
 if f==4:
  rows=F4_TXT.split(';')
 else:
  rows=(P/f'bbo_verified_F{f}.txt').read_text().split(';')
 src=np.array([r[0] for r in rows]); z=np.array([list(map(float,r[1:].split(','))) for r in rows]);X=z[:,:-1];y=z[:,-1]
 if not omit_week11:
  xx,yy=W11[f];X=np.vstack([X,xx]);y=np.r_[y,yy];src=np.concatenate([src,np.array(['W'])])
 if f==2:
  # single outside peer maximum from independently listed source
  X=np.vstack([X,[.717528,.864773]]);y=np.r_[y,.7560218355559285];src=np.concatenate([src,np.array(['C'])])
 if f==4:
  X=np.vstack([X,[.410114,.432907,.358436,.425839]]);y=np.r_[y,.5702077009884445];src=np.concatenate([src,np.array(['C'])])
 if f==6:
  X=np.vstack([X,[.416400,.362244,.606464,.816435,.207588]]);y=np.r_[y,-.17200299465050722];src=np.concatenate([src,np.array(['C'])])
 return X,y,src

def unique(X,y):
 a,inv=np.unique(np.round(X,6),axis=0,return_inverse=True)
 y0=np.array([y[inv==k].mean() for k in range(len(a))]);return a,y0
class M:
 def __init__(self,name,**param):self.name=name;self.param=param
 def fit(self,X,y):
  X,y=unique(X,y);self.dim=X.shape[1];self.std=None;self.power=None;xx=X
  if self.name in ('gp','ard','warp','pca','kpca','mlp','pls','br'):
   self.std=StandardScaler().fit(X);xx=self.std.transform(X)
  if self.name in ('gp','ard','warp'):
   zz=y
   if self.name=='warp':
    self.power=PowerTransformer(method='yeo-johnson',standardize=False).fit(y[:,None]);zz=self.power.transform(y[:,None]).ravel()
   kname=self.param.get('kernel','m52');length=self.param.get('ls',1.0)
   if self.name=='ard':
    k=Matern(length_scale=np.full(self.dim,1.),length_scale_bounds=(.13,7),nu=2.5) if kname=='m52' else RBF(length_scale=np.full(self.dim,1.),length_scale_bounds=(.13,7))
   else:k=Matern(length_scale=length,nu=2.5) if kname=='m52' else RBF(length_scale=length)
   self.model=GaussianProcessRegressor(kernel=k,normalize_y=True,alpha=self.param.get('noise',.25)**2*np.var(zz)+1e-6,optimizer=None if self.name!='ard' else 'fmin_l_bfgs_b',random_state=22).fit(xx,zz)
  elif self.name=='tree': self.model=ExtraTreesRegressor(n_estimators=120,min_samples_leaf=self.param.get('leaf',2),n_jobs=1,random_state=12).fit(xx,y)
  elif self.name=='pca':self.model=Pipeline([('pca',PCA(n_components=min(self.param.get('k',2),self.dim))),('reg',Ridge(alpha=self.param.get('ridge',.1)))]).fit(xx,y)
  elif self.name=='kpca':self.model=Pipeline([('kpca',KernelPCA(n_components=min(self.param.get('k',8),len(X)-2),kernel='rbf',gamma=self.param.get('gamma',.2),eigen_solver='dense')),('reg',Ridge(alpha=self.param.get('ridge',.03)))]).fit(xx,y)
  elif self.name=='mlp':self.model=MLPRegressor(hidden_layer_sizes=(16,8),alpha=2,early_stopping=True,random_state=12,max_iter=500).fit(xx,y)
  elif self.name=='pls':self.model=PLSRegression(n_components=min(self.param.get('k',2),self.dim)).fit(xx,y)
  elif self.name=='br':self.model=BayesianRidge().fit(xx,y)
  return self
 def predict(self,X):
  xx=np.atleast_2d(X);xx=self.std.transform(xx) if self.std is not None else xx
  if self.name in ('gp','ard','warp'):
   m,s=self.model.predict(xx,return_std=True)
   if self.power is not None:
    z=self.power.inverse_transform(m[:,None]).ravel();nextz=self.power.inverse_transform((m+1e-4)[:,None]).ravel();s=np.clip(abs((nextz-z)/1e-4),.01,100)*s;m=z
   return m,s
  if self.name=='tree':
   z=np.stack([a.predict(xx) for a in self.model.estimators_]);return z.mean(axis=0),z.std(axis=0)
  m=np.asarray(self.model.predict(xx)).ravel();return m,np.zeros(len(m))

def variants(f):
 common=[M('gp',kernel='m52',ls=.6,noise=.2),M('gp',kernel='rbf',ls=1.,noise=.35),M('gp',kernel='m52',ls=1.5,noise=.4),M('ard',kernel='m52',noise=.25),M('warp',kernel='m52',ls=1.,noise=.3),M('tree',leaf=2),M('tree',leaf=4),M('kpca',k=8,gamma=.12,ridge=.03),M('kpca',k=12,gamma=.5,ridge=.02),M('pca',k=max(1, f-1 if f<4 else 3),ridge=.1),M('pls',k=max(1, f-1 if f<4 else 3)),M('mlp'),M('br')]
 if f==4: common += [M('gp',kernel='m52',ls=.12,noise=.01),M('gp',kernel='rbf',ls=.25,noise=.03)]
 if f==3:common += [M('gp',kernel='m52',ls=.5,noise=.12), M('gp',kernel='rbf',ls=.5,noise=.25)]
 if f==6:common += [M('gp',kernel='rbf',ls=2.4,noise=.2)]
 return common

def evaluate(f,models):
 X,y,s=source_data(f)
 out=[]
 for model in models:
  cv=[]
  # Shared cohort observations have overlapping initial points; use only external cohorts for checks, keeping our Week11 in train.
  for held in ['V','N','E','H']:
   te=s==held;tr=(s!=held)&(s!='C')
   if f==4 and held=='N':continue
   if te.sum()==0:continue
   try:
    mm=M(model.name,**model.param).fit(X[tr],y[tr]);v,_=mm.predict(X[te]);e=np.abs(v-y[te]);weight=1+2*(y[te]>=np.quantile(y[te],.65))
    # restrict validation to points with plausibly high outcomes using a fixed floor per function, avoid remote regions dominating
    floor={2:.35,3:-.17,4:-1.5,6:-.6}[f];mask=y[te]>=floor
    if mask.sum()>=2:
     ev=float(np.average(e[mask],weights=weight[mask]))
     cv.append((held,ev,int(mask.sum())))
   except Exception as ex:print('err',f,model.name,model.param,held,str(ex)[:50]);
  # one-step prospective audit of submitted Week 11: must not be included in model train
  try:
   train=s!='W';mm=M(model.name,**model.param).fit(X[train],y[train]);audit=float(mm.predict(W11[f][0])[0][0]);err=abs(audit-W11[f][1])
  except Exception as ex: audit=err=float('nan')
  # use arithmetic mean of held cohort weighted errors
  score=float(np.mean([r[1] for r in cv])) if cv else 999
  out.append(dict(name=model.name,params=model.param,cv=score,audit_pred=audit,audit_error=err,folds=cv))
 return sorted(out,key=lambda r:r['cv'])

def pool(f,X,y):
 d=X.shape[1];XX,YY=unique(X,y);best=XX[np.argmax(YY)]
 cands=[np.array(ORIG[f]),np.array(PREV_BAD[f]),np.array(W11[f][0]),best]
 if f==2:cands.extend([[.717528,.864773],[.692,.366],[.708638,.510785],[.692,.95]])
 if f==3:cands.extend([[.313581,.474345,.485191],[.4455,.593,.42],[.489838,.498896,.486446]])
 if f==4:cands.extend([[.415,.417,.3665,.413],[.42037,.427768,.368794,.412497],[.376347,.414508,.41858,.417207]])
 if f==6:cands.extend([[.379808,.287508,.660125,.776426,.078124],[.415955,.337725,.658778,.80673,.026973]])
 centres=np.asarray(cands+[list(x) for x in XX[np.argsort(YY)[-6:]]]);
 z=[]
 for rad in ([.01,.025,.05] if f!=6 else [.025,.05,.09]):
  for c in centres: z.append(np.clip(rng.normal(c,rad,size=(160,d)),0,.999999))
 sob=qmc.Sobol(d,scramble=True,seed=62+f).random_base2(m=11)
 p=np.round(np.clip(np.vstack([*z,sob,centres]),0,.999999),6)
 return np.unique(p,axis=0)

def select(f,ranking):
 X,y,src=source_data(f);cv=ranking; candidates=pool(f,X,y)
 # avoid overrepresentation of GP in committee. At most one of each GP/kernel family for main ranking
 picks=[];famset=set()
 for r in cv:
  if not np.isfinite(r['cv']): continue
  name=r['name']; family='GP' if name in ('gp','ard') else name
  if family in famset:continue
  if name in ('pca','pls','mlp','br') and r['cv']>cv[0]['cv']*1.35:continue
  if len(picks)>=5:break
  famset.add(family);picks.append((r,M(name,**r['params']).fit(X,y)))
 preds=[]; std=[]
 for r,m in picks:
  mu,sd=m.predict(candidates);preds.append(mu);std.append(sd)
 pred=np.array(preds);std=np.array(std);w=np.array([1/max(r['cv'],.015) for r,m in picks]);w=w/w.sum()
 ens=w@pred; disag=np.sqrt(np.sum(w[:,None]*(pred-ens)**2,axis=0)); robust=ens-.25*disag
 uniqueX,uy=unique(X,y)
 # Local trust region about top observed points, restrict candidate pool to center x +/- 0.04 (f4) or 0.06 (f3), 0.10 (f6)
 leaders=uniqueX[np.argsort(uy)[-4:]]; rad={2:.075,3:.10,4:.04,6:.11}[f]
 tr=np.any(np.all(np.abs(candidates[:,None,:]-leaders[None,:,:])<=rad,axis=2),axis=1)
 # Expected improvement on selected GP with model uncertainty, baseline empirical best penalized for noise via upper quantile surrogate
 gpix=next((i for i,(_,m) in enumerate(picks) if m.name in ('gp','ard')),None)
 if gpix is not None:
  mu=pred[gpix];sd=np.maximum(std[gpix],1e-7); ref=np.quantile(ens,.997);zz=(mu-ref)/sd;EI=(mu-ref)*norm.cdf(zz)+sd*norm.pdf(zz);UCB=mu+.8*sd
 else:EI=robust;UCB=robust
 # Candidate distinct from all observed inputs
 dist=np.min(np.linalg.norm(candidates[:,None,:]-uniqueX[None,:,:],axis=2),axis=1)
 mask=dist>0.0002
 # incumbent, robust, EI, trust, UCB, originally proposed, 2 Nov proposal, peer best
 proposals={}
 def add(kind,x):
  x=np.round(np.asarray(x,dtype=float),6)
  pp=np.array([m.predict(x)[0][0] for _,m in picks]);mm=float(w@pp);ds=float(np.sqrt(np.sum(w*(pp-mm)**2)));proposals[kind]=dict(x=x.tolist(),mean=mm,disagreement=ds,min=round(float(pp.min()),5),max=round(float(pp.max()),5),preds={p[0]['name']:round(float(v),5) for p,v in zip(picks,pp)})
 add('previous_round12',ORIG[f]); add('Week11_observed',W11[f][0]);add('Nov2_proposal',PREV_BAD[f]);add('best_observed_shared',uniqueX[np.argmax(uy)])
 for name,score,valid in [('robust',robust,mask),('EI',EI,mask),('UCB',UCB,mask),('TuRBO_style',robust,mask&tr)]:
  id=np.flatnonzero(valid)[np.argmax(score[valid])];add(name,candidates[id])
 # model parameter sensitivity on best candidates
 return proposals,[dict(name=z[0]['name'],params=z[0]['params'],cv=z[0]['cv'],weight=round(float(ww),3)) for z,ww in zip(picks,w)],len(candidates)

def unsup(f):
 X,y,src=source_data(f);z=StandardScaler().fit_transform(X)
 p=PCA().fit(z);var=p.explained_variance_ratio_
 if f==2:return dict(explained=np.round(var,4).tolist())
 # high output region may be line along narrow manifold of adaptively queried points, not necessarily intrinsic dimension
 good=y>=np.quantile(y,.75);coef=PCA().fit(StandardScaler().fit_transform(X[good])).explained_variance_ratio_
 iso=IsolationForest(random_state=24,contamination=.12).fit(X);p=X[np.argmax(y)];v=iso.decision_function([p])[0]
 return dict(explained=np.round(var,4).tolist(),top_quartile_explained=np.round(coef,4).tolist(),best_observed_iso_score=float(v))

if __name__=='__main__':
 reports={}
 for f in [2,3,4,6]:
  t=time.time();print('RUN',f,flush=True);X,y,s=source_data(f);print('n',len(y),'observed max',float(y.max()),'own W11',W11[f][1],flush=True)
  ranks=evaluate(f,variants(f));print('CV',[(r['name'],r['params'],round(r['cv'],4),round(r['audit_pred'],4)) for r in ranks[:8]],flush=True)
  proposals,picks,count=select(f,ranks)
  print('COMMITTEE',picks,flush=True)
  print('PROPOSALS',json.dumps(proposals,indent=1),flush=True)
  u=unsup(f);reports[f]=dict(n=len(y),unique=len(unique(X,y)[1]),ranking=ranks,committee=picks,pool_n=count,proposals=proposals,unsupervised=u,own_week11=dict(x=W11[f][0],y=W11[f][1]));print('UNSUP',u,'ELAPSED',round(time.time()-t,1),flush=True)
  (P/'round12_new_benchmark.json').write_text(json.dumps(reports,indent=2,allow_nan=True))
 print('DONE')
