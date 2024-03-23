import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from scipy import signal

# PID Controller
def pidController(setpoint, actual, prev_error, integral, Kp, Ki, Kd, dt):
    error = setpoint - actual
    integral += error * dt
    derivative = (error - prev_error) / dt
    output = Kp * error + Ki * integral + Kd * derivative
    return output, error, integral

# System model
def systemModel(y, t, u):
    return (-y + u) / 5.0  # simple first order system

# Simulation parameters
dt = 0.01  # simulation time step
t = np.arange(0.0, 10.0, dt)  # time array
N = len(t)  # number of time steps
setpoint = 1.0  # desired setpoint
y = np.zeros(N)  # system output
u = np.zeros(N)  # control effort
prev_error = 0.0  # previous error
integral = 0.0  # integral term
Kp = 5.0  # proportional gain
Ki = 2.0  # integral gain
Kd = 0.1  # derivative gain

# Simulation loop
for i in range(1, N):
    u[i], prev_error, integral = pidController(setpoint, y[i-1], prev_error, integral, Kp, Ki, Kd, dt)
    y[i] = odeint(systemModel, y[i-1], [0, dt], args=(u[i],))[1]

# Plot results
plt.figure()
plt.subplot(2, 1, 1)
plt.plot(t, y, label='y')
plt.plot(t, np.ones(N)*setpoint, 'r--', label='setpoint')
plt.legend()
plt.subplot(2, 1, 2)
plt.plot(t, u, label='u')
plt.legend()
plt.show()