import numpy as np
import matplotlib.pyplot as plt

x = 16
print("Sqrt", x, "is: ", np.sqrt(x))
print("Cube", x, "is: ", np.cbrt(x))

theta = 30
print("Radian", theta, "is: ", np.radians(theta))
print("Sin", theta, "is: ", np.sin(theta), "rad")
print("Cos", theta, "is: ", np.cos(theta), "rad")

meshPoints = np.linspace(-1, 1, 500)
print(meshPoints)

meshPoints = meshPoints[53]
print(meshPoints)

meshPoints = np.linspace(-1, 1, 500)
plt.plot(meshPoints, np.sin(2*np.pi*meshPoints))
plt.savefig('Figure1.png')
plt.show()


