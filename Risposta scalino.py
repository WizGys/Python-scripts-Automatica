import numpy as np
import matplotlib.pyplot as plt

# Funzione di trasferimento
def G(s, K):
  return K / (s + 1)

# Simulazione della risposta al gradino
t = np.linspace(0, 10, 100)

# Plot della risposta per diversi valori di guadagno
for K in [1, 2, 5]:
  y = np.array([G(1j*w, K) for w in t])
  plt.plot(t, y, label='K={}'.format(K))

plt.xlabel('Tempo (t)')
plt.ylabel('Uscita (y)')
plt.legend()
plt.show()