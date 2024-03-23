import numpy as np

import matplotlib.pyplot as plt

lambda1 = float(input("Enter the first eigenvalue: "))
lambda2 = float(input("Enter the second eigenvalue: "))

t = np.linspace(0, 10, 100)

initial_conditions = [(x0, y0) for x0 in np.linspace(-1, 1, 7) for y0 in np.linspace(-1, 1, 7)]

for x0, y0 in initial_conditions:
    x = x0 * np.exp(lambda1 * t)
    y = y0 * np.exp(lambda2 * t)

    if x0 != 0 or y0 != 0:
        plt.plot(x, y, color='blue')

        if len(x) > 1:
            plt.quiver(x[:-1], y[:-1], x[1:]-x[:-1], y[1:]-y[:-1], scale_units='xy', angles='xy', scale=1, color='blue')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Traiettorie libere del sistema')
plt.grid(True)
plt.show()