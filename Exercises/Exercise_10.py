import matplotlib.pyplot as plt
import numpy as np

theta = np.linspace(0, 2* np.pi, 100)
fig = plt.figure(figsize=(6,6), facecolor = "#b8e3bc")
rect = [0.1,0.1,0.8,0.8]
r0 = 0.8
ax_cartesian = fig.add_axes(rect)
ax2 = fig.add_axes(rect, polar=True, frameon=False)
ax2.plot(theta, r0 + np.cos(theta), color="red",
              linewidth=2, linestyle=":", label="r = 0.8: ")
r0 = 1
ax_cartesian = fig.add_axes(rect)
ax_polar = fig.add_axes(rect, polar=True, frameon=False)
ax_polar.plot(theta, r0 + np.cos(theta), color="green",
              linewidth=3, linestyle="-", label="r = 1: ")
r0 = 1.2
ax_cartesian = fig.add_axes(rect)
ax_polar = fig.add_axes(rect, polar=True, frameon=False)
ax_polar.plot(theta, r0 + np.cos(theta), color="blue",
              linewidth=2, linestyle=":", label="r = 1.2: ")
plt.legend(loc="upper center", ncol=3,
           bbox_to_anchor=(0.25, 0.5, 0.5, 0.5),
           edgecolor="inherit",facecolor="white",
           shadow=True, markerfirst=False)
                   
plt.title("Cardioid", loc = "center")

plt.show()


