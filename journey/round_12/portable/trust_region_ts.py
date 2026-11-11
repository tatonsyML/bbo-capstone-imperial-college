import numpy as np,json,warnings
from pathlib import Path
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import Matern
from review_round12 import source_data, unique, W11
from scipy.stats import qmc
warnings.filterwarnings('ignore')
P=Path(__file__).resolve().parent
res={}
for f in [2,3,4,6]:
 X,y,src=source_data(f);xx,yy=unique(X,y);owned=np.isin(src,['O','W']);ownx=X[owned];owny=y[owned]
 # sequential state update reflecting TuRBO-1 concept; start with initial sample set
 start=10; ix=np.argmax(owny[:start]);inc=ownx[ix].copy();best=owny[ix];length=.8;success=fail=0
 hist=[]
 for v,score in zip(ownx[start:],owny[start:]):
  if score>best+max(.00001,.0002*abs(best)):
   best=score;inc=v.copy();success+=1;fail=0
  else:fail+=1;success=0
  if success>=3:length=min(length*2,1.6);success=0
  if fail>=max(4,f):length=max(length/2,.04);fail=0
  hist.append((best,length))
 # floor length for testing: old f2 has repeated noisy observations near x2=.96; which center wins depends raw noisy score
 lo=np.maximum(0,inc-.5*length);hi=np.minimum(.999999,inc+.5*length)
 # at least a .04 window each dimension to permit local search within a small trust region
 lo=np.maximum(0,np.minimum(lo,inc-.02));hi=np.minimum(.999999,np.maximum(hi,inc+.02))
 samp=qmc.Sobol(X.shape[1],scramble=True,seed=600+f).random_base2(m=9)
 cs=lo+(hi-lo)*samp
 # Fitted Matérn posterior on pooled data (single GP as TuRBO one-step surrogate; true TuRBO has more mechanics)
 mdl=GaussianProcessRegressor(kernel=Matern(length_scale=.25,nu=2.5),alpha=.03**2*np.var(yy)+1e-6,normalize_y=True,optimizer=None).fit(xx,yy)
 mean,cov=mdl.predict(cs,return_cov=True); cov=(cov+cov.T)/2 + 1e-7*np.eye(len(cs))
 try: L=np.linalg.cholesky(cov)
 except Exception: L=np.linalg.cholesky(cov+1e-5*np.eye(len(cs)))
 rng=np.random.default_rng(701+f);cho=[]
 for i in range(30):
  v=mean+L@rng.standard_normal(len(cs));id=int(np.argmax(v));cho.append(cs[id])
 cho=np.array(cho);m=mdl.predict(cho);ids=np.argsort(m)[-5:]
 res[f]={'center':np.round(inc,6).tolist(),'own_incumbent_y':float(best),'trust_length':length,'low':np.round(lo,5).tolist(),'high':np.round(hi,5).tolist(),'ts_median':np.round(np.median(cho,axis=0),6).tolist(),'top_posterior_sample':np.round(cho[ids[-1]],6).tolist(),'top_gp_pred':float(m[ids[-1]]),'spread_suggestions':np.round(np.std(cho,axis=0),4).tolist()}
 print('F',f,res[f],flush=True)
(P/'round12_turbo_ts.json').write_text(json.dumps(res,indent=2))
