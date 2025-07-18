import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,10,100)
print(x)

f = np.e **(-x / 10) * (np.sin(np.pi * x))
plt.plot(x,f)

g = x * np.e ** (-x / 3)
plt.plot(x, g)

plt.plot(x, f, label="x-axes", color="green")
plt.plot(x, g, label="y-axes", color="yellow")
plt.legend()
plt.savefig('Figure1.jpg')
plt.show()

