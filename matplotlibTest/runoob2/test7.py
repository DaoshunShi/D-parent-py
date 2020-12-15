import numpy as np
import matplotlib.pyplot as plt


def f(x,y): return (1-x/2+x**5+y**3)*np.exp(-x**2-y**2)

n = 10
x = np.linspace(-3,3,4*n)
y = np.linspace(-3,3,3*n)
X,Y = np.meshgrid(x,y)
Z = f(X, Y)

plt.axes([0.025, 0.025, 0.95, 0.95])

plt.imshow(Z, interpolation='bicubic', cmap='bone', origin='lower')
plt.colorbar(shrink=.8)

plt.xticks([]), plt.yticks([])

plt.show()