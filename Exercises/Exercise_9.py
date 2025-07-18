import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d
from scipy.optimize import bisect

data ='''0   0
0.1 0.1
0.2 0.2
0.3 0.3
0.4 0.31
0.5 0.32
0.6 0.35'''
data = [line.split() for line in data.split('\n')]
data = np.array(data, dtype = 'float')

strain = data[:,0]
stress = data[:,1]

E = 1 
y = [0, 0.5]
x = 0.2, ((y[1] - y[0])/E+0.2)

y = interp1d(x, y)
stress = interp1d(strain, stress)
x1 = max(x[0], strain[0])
x2 = min(x[-1], strain[-1])
max_err = .01

f = lambda x : stress(x) - y(x)
x1 = bisect(f, x1, x2, xtol = .001)
y1 = stress(x1)

plt.figure(num=None, figsize=(6,4), dpi=100, facecolor='lightgreen')
plt.plot(strain, stress(strain))
plt.plot(x, y(x))
plt.scatter(x1, y1, color = "red")
plt.show()