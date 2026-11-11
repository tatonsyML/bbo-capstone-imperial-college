import json,warnings
import numpy as np
from pathlib import Path
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import Matern,DotProduct,ConstantKernel
from sklearn.preprocessing import PowerTransformer
from review_round12 import source_data, unique, M, W11, ORIG, PREV_BAD
warnings.filterwarnings('ignore')
P=Path('/mnt/data/bbo_week12_deep_review')
points={
2:{'round12_old':[.696286,.48864],'new_robust':[.684399,.368552],'week11':[.692,.366],'nearby':[.683311,.366084],'peer_C':[.717528,.864773]},
3:{'round12_old':[.489838,.498896,.486446],'peer_best':[.313581,.474345,.485191],'week11':[.4455,.593,.42],'new_local':[.331989,.413022,.437884]},
4:{'round12_old':[.4187,.415988,.363637,.413858],'week11':[.415,.417,.3665,.413],'optimistic':[.425035,.415028,.387701,.40263],'peer_V':[.376347,.414508,.41858,.417207]},
6:{'round12_old':[.401093,.323286,.666764,.777577,.090679],'new_robust':[.41508,.344119,.644062,.776818,.076258],'week11':[.457,.37,.642,.738,.02],'peer_N':[.379808,.287508,.660125,.776426,.078124]}}
class WarpInputGP:
 def __init__(self,a,b):self.a=a;self.b=b
 def xform(self,X):
  z=np.clip(np.asarray(X),1e-8,1-1e-8);return 1-np.power(1-np.power(z,self.a),self.b)
 def fit(self,X,y):
  X,y=unique(X,y);self.power=PowerTransformer(method='yeo-johnson',standardize=False).fit(y[:,None]);z=self.power.transform(y[:,None]).ravel()
  k=.7*Matern(length_scale=.35,nu=1.5)+.3*DotProduct(sigma_0=.1)
  self.model=GaussianProcessRegressor(kernel=k,alpha=.15**2*np.var(z)+1e-6,normalize_y=True,optimizer=None).fit(self.xform(X),z)
  return self
 def predict(self,X):
  z,s=self.model.predict(self.xform(np.atleast_2d(X)),return_std=True);m=self.power.inverse_transform(z[:,None]).ravel();return m,s
allres={}
for f in [2,3,4,6]:
 X,y,src=source_data(f);print('F',f,flush=True)
 xs=np.array(list(points[f].values()))
 # comparisons per exclusion for leading stationary models and one best nonlinear alternative
 models=[('GP',lambda:M('gp',kernel='m52',ls=.5 if f==3 else 1.5,noise=.2 if f==3 else .4)),('TREE',lambda:M('tree',leaf=2)),('KPCA',lambda:M('kpca',k=8,gamma=.12,ridge=.03)),('WARP',lambda:M('warp',kernel='m52',ls=1.,noise=.3))]
 folds={};wide={}
 for held in ['none','E','V','N','H','W']:
  train=src!=held if held!='none' else np.ones(len(y),bool)
  fold={}
  for name,ctor in models:
   try:
    p=M(ctor().name,**ctor().param).fit(X[train],y[train]).predict(xs)[0]
    fold[name]=np.round(p,5).tolist()
   except Exception as e:fold[name]={'error':str(e)[:90]}
  folds[held]=fold
  for name,vec in fold.items():
   if isinstance(vec,list):print(' ',held,name,list(zip(points[f].keys(),vec)),flush=True)
 for a,b in [(1,1),(.6,2),(2,.6),(.7,1.6),(1.6,.7)]:
  cv=[]
  for held in ['E','V','N','H']:
   te=src==held;tr=src!=held
   if te.sum()==0:continue
   try:
    mm=WarpInputGP(a,b).fit(X[tr],y[tr]);pred,_=mm.predict(X[te]);
    floor={2:.35,3:-.17,4:-1.5,6:-.6}[f];sel=y[te]>=floor
    if sel.sum():cv.append(float(np.abs(pred[sel]-y[te][sel]).mean()))
   except Exception as e: print('ERRWARP',f,a,b,held,str(e)[:60])
  if cv:
   model=WarpInputGP(a,b).fit(X,y);m,s=model.predict(xs)
   wide[f'{a},{b}']={'cv':round(float(np.mean(cv)),6),'candidate_predictions':np.round(m,6).tolist()}
 print('HEBO_INPUT_WARP',wide,flush=True)
 allres[f]={'candidates':points[f],'fold_predictions':folds,'input_output_warp':wide}
 (P/'round12_robustness_warp.json').write_text(json.dumps(allres,indent=2))
