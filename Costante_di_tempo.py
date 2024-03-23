import numpy as np
import matplotlib.pyplot as plt

def G(s):
  return 1 / (s + 1)

# Simulazione della risposta al gradino
t = np.linspace(0, 10, 100)
y = np.array([G(1j*w) for w in t])

plt.plot(t, y)
plt.xlabel('Tempo (t)')
plt.ylabel('Uscita (y)')
plt.show()