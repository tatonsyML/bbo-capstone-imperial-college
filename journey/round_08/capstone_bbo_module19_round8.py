from pathlib import Path
import warnings
import numpy as np
from scipy.stats import rankdata
from sklearn.exceptions import ConvergenceWarning
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import ConstantKernel, RBF, Matern, WhiteKernel

BASE = Path(__file__).resolve().parent
INITIAL = BASE / "initial_data"
RANDOM_STATE = 20261008

ROUND_INPUTS = {
1: [[0.02,0.98],[0.7,0.5],[0.5,0.5,0.345],[0.5315,0.448817,0.362651,0.331977],[0.1,0.75,0.9,0.98],[0.440752,0.249118,0.839948,0.999999,0.000001],[0.034737,0.246867,0.265123,0.307852,0.362506,0.937209],[0.088526,0.03196,0.048494,0.063991,0.991333,0.224689,0.073759,0.537568]],
2: [[0.052001,0.865999],[0.672,0.999999],[0.993188,0.591985,0.000280],[0.415636,0.429159,0.368928,0.413098],[0.522156,0.922246,0.999259,0.99589],[0.436716,0.004631,0.398416,0.895113,0.03487],[0.074002,0.315323,0.247287,0.026732,0.35885,0.832838],[0.321822,0.045429,0.355724,0.015612,0.965914,0.090106,0.138377,0.028859]],
3: [[0.636406,0.206433],[0.7015,0.957999],[0.496377,0.564413,0.34369],[0.398136,0.414095,0.370552,0.440336],[0.508373,0.970147,0.999999,0.999999],[0.467823,0.254239,0.82281,0.999999,0.03819],[0.046316,0.36927,0.256273,0.262985,0.391467,0.834089],[0.099253,0.051531,0.055571,0.074437,0.985751,0.228722,0.118577,0.53735]],
4: [[0.999999,0.999999],[0.705,0.999999],[0.49,0.62,0.36],[0.425128,0.426376,0.368659,0.411895],[0.508373,0.999999,0.999999,0.999999],[0.481359,0.2568,0.814241,0.999999,0.057285],[0.015,0.36927,0.256273,0.262985,0.391467,0.834089],[0.104617,0.061316,0.05911,0.07966,0.98296,0.230739,0.140986,0.537241]],
5: [[0.75,0.75],[0.7015,0.959409],[0.483623,0.675587,0.37631],[0.420382,0.427768,0.368794,0.412497],[0.558373,0.999999,0.999999,0.999999],[0.494895,0.259361,0.805672,0.999999,0.07638],[0.06,0.36927,0.256273,0.262985,0.391467,0.834089],[0.109981,0.071101,0.062649,0.084883,0.980169,0.232756,0.163395,0.537132]],
6: [[0.732524,0.738900],[0.701500,0.959816],[0.487816,0.639038,0.365586],[0.420290,0.427795,0.368797,0.412509],[0.608373,0.999999,0.999999,0.999999],[0.480996,0.256731,0.814471,0.999999,0.056773],[0.100000,0.369270,0.256273,0.262985,0.391467,0.834089],[0.115345,0.080886,0.066188,0.090106,0.977378,0.234773,0.185804,0.537023]],
7: [[0.730874,0.731800],[0.701500,0.960223],[0.486949,0.646592,0.367803],[0.420383,0.427768,0.368794,0.412497],[0.658373,0.999999,0.999999,0.999999],[0.481360,0.256800,0.814241,0.999999,0.057285],[0.150000,0.369270,0.256273,0.262985,0.391467,0.834089],[0.128076,0.104109,0.074587,0.102502,0.970754,0.239560,0.238989,0.536764]]
}
ROUND_OUTPUTS = {
1:[0.0,0.379063270240082,-0.043777238484906444,-1.9105442369490215,1426.0897645116545,-0.6039806265819045,1.3605555033645358,9.8321123600691],
2:[-1.9632454298284602e-233,0.5860547049641637,-0.10649509777296216,0.6475542651940924,3722.27447382346,-0.7529878928551597,1.0204022790488059,9.4977489881389],
3:[2.69213108614911e-65,0.653867607133911,-0.042736572375282326,0.3148998621282755,4295.86773060836,-0.5697790503980307,1.6137963046751616,9.8634785625365],
4:[1.517648729565899e-192,0.5912856598404541,-0.03128159682344515,0.646639136105915,4694.317308235808,-0.5414478319707962,1.5516324818204725,9.8754707823449],
5:[1.3319145509281447e-22,0.6548498709022528,-0.03342310883527115,0.6589269585907762,4807.986076589498,-0.5729927758567235,1.6384401460325033,9.8850021313761],
6:[3.2554751168755075e-17,0.6913148663237587,-0.020856154529509317,0.6589225038891553,4957.571711515816,-0.6980295508727566,1.7006596900158717,9.8920726096301],
7:[1.3142529628112004e-15,0.5893476079120687,-0.027911148643077723,0.6589240028704428,5151.047725485012,-0.5903792900833394,1.7557182120997592,9.8990020095864]
}

def build(fn, rounds=7):
    X = np.load(INITIAL / f"function_{fn}" / "initial_inputs.npy")
    y = np.load(INITIAL / f"function_{fn}" / "initial_outputs.npy").reshape(-1)
    for r in range(1, rounds + 1):
        X = np.vstack([X, np.asarray(ROUND_INPUTS[r][fn-1], float)])
        y = np.append(y, ROUND_OUTPUTS[r][fn-1])
    return X, y

def kernel(name, d):
    ls = np.full(d, 0.2)
    if name == "RBF":
        base = RBF(ls, (1e-4, 3.0))
    elif name == "M15":
        base = Matern(ls, (1e-4, 3.0), nu=1.5)
    else:
        base = Matern(ls, (1e-4, 3.0), nu=2.5)
    return ConstantKernel(1.0, (1e-3, 1e3))*base + WhiteKernel(1e-6, (1e-10, 1e-1))

X1, y1 = build(1)
best1 = X1[np.argmax(y1)]
rank_y = (rankdata(y1, method="average") - 1) / (len(y1) - 1)
models1 = []
for i, name in enumerate(("RBF", "M15", "M25")):
    gp = GaussianProcessRegressor(kernel=kernel(name, 2), normalize_y=True,n_restarts_optimizer=8, random_state=RANDOM_STATE+i)
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", ConvergenceWarning)
        gp.fit(X1, rank_y)
    models1.append(gp)
g1 = np.linspace(best1[0]-0.005, best1[0]+0.005, 301)
g2 = np.linspace(best1[1]-0.005, best1[1]+0.005, 301)
grid1 = np.array([[a,b] for a in g1 for b in g2])
pred1 = np.column_stack([m.predict(grid1) for m in models1])
score1 = pred1.mean(axis=1) - 0.5*pred1.std(axis=1)
f1_point = grid1[np.argmax(score1)]

x2 = np.array([0.959409, 0.959816, 0.960223])
y2 = np.array([0.6548498709022528, 0.6913148663237587, 0.5893476079120687])
c2 = np.polyfit(x2, y2, 2)
f2_vertex = -c2[1] / (2*c2[0])

p4 = np.array(ROUND_INPUTS[4][2], float)
p5 = np.array(ROUND_INPUTS[5][2], float)
direction3 = p5 - p4
def path_t(p):
    return np.dot(np.asarray(p)-p4, direction3) / np.dot(direction3, direction3)
t3 = np.array([path_t(ROUND_INPUTS[r][2]) for r in [4,6,7]])
y3 = np.array([ROUND_OUTPUTS[r][2] for r in [4,6,7]])
c3 = np.polyfit(t3, y3, 2)
f3_t = -c3[1] / (2*c3[0])
f3_point = p4 + f3_t * direction3

x5 = np.array([0.508373,0.558373,0.608373,0.658373])
y5 = np.array([4694.317308235808,4807.986076589498,4957.571711515816,5151.047725485012])
c5 = np.polyfit(x5, y5, 2)
f5_point = np.array([0.758373,0.999999,0.999999,0.999999])
f5_local_prediction = np.polyval(c5, f5_point[0])

x7 = np.array([0.060000, 0.100000, 0.150000])
y7 = np.array([1.6384401460325033, 1.7006596900158717, 1.7557182120997592])
c7 = np.polyfit(x7, y7, 2)
f7_vertex = -c7[1] / (2*c7[0])

X8, y8 = build(8)
best8 = X8[np.argmax(y8)]
models8 = []
for i, name in enumerate(("RBF","M15","M25")):
    gp = GaussianProcessRegressor(kernel=kernel(name, 8), normalize_y=True,n_restarts_optimizer=8, random_state=RANDOM_STATE+20+i)
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", ConvergenceWarning)
        gp.fit(X8, y8)
    models8.append(gp)
f8_point = best8.copy()
f8_point[5] = 0.264560
f8_preds = [float(m.predict(f8_point.reshape(1,-1))[0]) for m in models8]

ROUND8_QUERIES = {
    1: np.array([0.735874,0.729467]),
    2: np.array([0.701500,0.959720]),
    3: np.array([0.488344,0.634434,0.364235]),
    4: np.array([0.420381,0.427768,0.368794,0.412497]),
    5: f5_point,
    6: np.array([0.481358,0.256800,0.814241,0.999999,0.057285]),
    7: np.array([0.234070,0.369270,0.256273,0.262985,0.391467,0.834089]),
    8: f8_point,
}

print("Recomputed diagnostic candidates")
print("F1 rank-GP candidate:", f1_point)
print("F2 quadratic vertex:", f2_vertex, "predicted:", np.polyval(c2,f2_vertex))
print("F3 path candidate:", f3_point, "predicted:", np.polyval(c3,f3_t))
print("F5 local quadratic prediction at x1=0.758373:", f5_local_prediction)
print("F7 quadratic vertex:", f7_vertex, "predicted:", np.polyval(c7,f7_vertex))
print("F8 GP committee predictions:", f8_preds)

print("\nPortal values")
for fn, q in ROUND8_QUERIES.items():
    X, _ = build(fn)
    q = np.asarray(q, float)
    duplicate = any(np.all(np.round(row,6)==np.round(q,6)) for row in X)
    print(f"Function {fn}: " + "-".join(f"{v:.6f}" for v in q) + f" | duplicate={duplicate}")
