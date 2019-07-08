import numpy as np
import matplotlib.pyplot as plt

x = np.linsace(0,4*np.pi, 1000)
y = np.sin(x)

plt.xlabel("$x$")
plt.ylabel("$sin(x)$")
plt.plot(x,y)
plt.show()