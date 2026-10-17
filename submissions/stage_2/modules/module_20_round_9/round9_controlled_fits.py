from pathlib import Path
import numpy as np

# This script reproduces the simple, controlled local fits used for Round 9.
# It deliberately keeps observed values separate from prospective forecasts.

# F2: symmetric point around the Week 6 best.
x2 = np.array([0.959720, 0.959816, 0.960223])
y2 = np.array([0.6130861312279376, 0.6913148663237587, 0.5893476079120687])
c2 = np.polyfit(x2, y2, 2)
q2 = 0.959912
print("F2 forecast:", np.polyval(c2, q2))

# F3: local path defined by Week 4 -> Week 5, then refit with Week 8/6/7.
p4 = np.array([0.490000,0.620000,0.360000])
p5 = np.array([0.483623,0.675587,0.376310])
direction = p5-p4
def path_t(p):
    return np.dot(np.asarray(p)-p4, direction)/np.dot(direction,direction)
points = {
    8: np.array([0.488344,0.634434,0.364235]),
    6: np.array([0.487816,0.639038,0.365586]),
    7: np.array([0.486949,0.646592,0.367803]),
}
ys = {8:-0.029663277388799626,6:-0.020856154529509317,7:-0.027911148643077723}
t = np.array([path_t(points[r]) for r in [8,6,7]])
y = np.array([ys[r] for r in [8,6,7]])
c3 = np.polyfit(t,y,2)
tv = -c3[1]/(2*c3[0])
q3 = p4 + tv*direction
print("F3 candidate:", q3, "forecast:", np.polyval(c3,tv))

# F4: linear extrapolation across three one-microstep x1 probes.
x4=np.array([0.420383,0.420382,0.420381])
y4=np.array([0.6589240028704428,0.6589269585907762,0.6589299133743123])
c4=np.polyfit(x4,y4,1)
print("F4 forecast:", np.polyval(c4,0.420380))

# F5: controlled x1 series with x2-x4 fixed at 0.999999.
x5=np.array([0.508373,0.558373,0.608373,0.658373,0.758373])
y5=np.array([4694.317308235808,4807.986076589498,4957.571711515816,5151.047725485012,5709.3613198927205])
c5=np.polyfit(x5,y5,2)
print("F5 quadratic forecast:", np.polyval(c5,0.858373))

# F7: updated controlled x1 quadratic.
x7=np.array([0.046316,0.015000,0.060000,0.100000,0.150000,0.234070])
y7=np.array([1.6137963046751616,1.5516324818204725,1.6384401460325033,1.7006596900158717,1.7557182120997592,1.785862549726479])
c7=np.polyfit(x7,y7,2)
v7=-c7[1]/(2*c7[0])
print("F7 vertex:",v7,"forecast:",np.polyval(c7,v7))
