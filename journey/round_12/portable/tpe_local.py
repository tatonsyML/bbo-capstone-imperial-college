import numpy as np, json, optuna, sys
from scipy.optimize import minimize
from pathlib import Path
from review_round12 import source_data, unique, W11, ORIG, M
P=Path(__file__).resolve().parent
optuna.logging.set_verbosity(optuna.logging.ERROR)
res={}
for f in [2,3,4,6]:
 X,y,src=source_data(f);X,y=unique(X,y);n,d=X.shape
 dis={f'x{j+1}':optuna.distributions.FloatDistribution(0,.999999) for j in range(d)}
 a=[]
 for mv in [False,True]:
  st=optuna.create_study(direction='maximize',sampler=optuna.samplers.TPESampler(multivariate=mv,n_startup_trials=10,n_ei_candidates=96,seed=42))
  for xx,yy in zip(X,y):
   st.add_trial(optuna.trial.create_trial(params={f'x{j+1}':float(xx[j]) for j in range(d)},distributions=dis,value=float(yy)))
  asks=[]
  for k in range(16):
   trial=st.ask();x=np.array([trial.suggest_float(f'x{j+1}',0,.999999) for j in range(d)])
   asks.append(x.tolist())
   # no outcomes supplied; no tell() until user portal evaluation
  a.append({'name':'TPE_'+('multivariate' if mv else 'independent'), 'first':np.round(asks[0],6).tolist(),'suggestions':np.round(asks,6).tolist()})
 res[f]={'n':n,'suggestions':a}
 print('F',f,'TPE', [(q['name'],q['first']) for q in a],flush=True)
 if f==4:
  # near-maximum quadratic fit in local coordinates to test local curvature (diagnostic, NOT black-box oracle)
  close=np.linalg.norm(X-np.asarray(W11[4][0]),axis=1)<.135
  XX=X[close];YY=y[close];center=np.array(W11[4][0]);dev=XX-center
  def mapz(D):
   return np.stack([np.ones(len(D)),*(D[:,j] for j in range(d)),*(D[:,j]*D[:,k] for j in range(d) for k in range(j,d))],axis=1)
  A=mapz(dev)
  # regularize quadratic curvature, not intercept/gradient; fit on all regional points
  for lam in [.001,.05,.5,2.]:
   J=np.diag([0]*5+[lam]*10)
   try:params=np.linalg.solve(A.T@A+J+1e-8*np.eye(15),A.T@YY)
   except Exception as e:print(e);continue
   def pred(z):return float(mapz(np.atleast_2d(z-center))@params)
   opt=minimize(lambda z:-pred(z),center,bounds=[(max(0,v-.05),min(.999999,v+.05)) for v in center],method='L-BFGS-B')
   print('F4_quadratic',lam,'n_local',len(YY),'opt',np.round(opt.x,6).tolist(),'pred',round(pred(opt.x),6),'pred_W11',round(pred(center),6),flush=True)
   res[f][f'quadratic_lambda_{lam}']=dict(n_local=len(YY),x=np.round(opt.x,6).tolist(),pred=pred(opt.x),incumbent_model=pred(center))
(P/'round12_tpe_and_local.json').write_text(json.dumps(res,indent=2))
