import numpy as np

import matplotlib.pyplot as plt

def nonlinear_system(x):
    return x**2 - 2*x + 1


function = input("Enter the function (e.g., x**2 - 2*x + 1): ")
nonlinear_system = lambda x: eval(function)

x = np.linspace(-10, 10, 100)
y = nonlinear_system(x)

equilibrium_points = np.roots([1, -2, 1])
equilibrium_points += np.random.uniform(-0.5, 0.5, size=equilibrium_points.shape)

plt.plot(x, y, linestyle='-', color='blue', marker='o', markevery=10, label=f'y = {function}')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Nonlinear System')
plt.grid(True)
plt.legend()

min_y = np.min(y)
max_y = np.max(y)
plt.text(x[np.argmin(y)], min_y, f'Min: ({x[np.argmin(y)]}, {min_y})', ha='center', va='bottom')
plt.text(x[np.argmax(y)], max_y, f'Max: ({x[np.argmax(y)]}, {max_y})', ha='center', va='top')

plt.scatter(equilibrium_points, nonlinear_system(equilibrium_points), color='red', label='Equilibrium Points')

plt.show()
