import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,2*np.pi,50)
y = np.sin(x)
z = np.cos(x)
"""
plt.figure()
plt.plot(y)

plt.figure()
plt.plot(z)

plt.show()
"""
"""
plt.subplot(2,2,1)
plt.plot(y)
plt.subplot(2,2,2)
plt.plot(z)

plt.show()
"""
plt.plot(y)
plt.plot(z)
plt.legend(['sin','cos'])
plt.xlabel('x ha')
plt.ylabel(' meghdar tabe')
plt.title('mosalasat')
plt.grid()

plt.show()




