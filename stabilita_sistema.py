import numpy as np
import matplotlib.pyplot as plt
from control.matlab import tf, step

# Dati gli autovalori
autovalore1 = 0
autovalore2 = -4

# Definisci la funzione di trasferimento
K = 1  # guadagno
num = [K]
den = [1, -(autovalore1 + autovalore2), autovalore1 * autovalore2]

# Crea il sistema
sys = tf(num, den)

# Simula la risposta al gradino
t, y = step(sys)

# Controlla la stabilità del sistema
if autovalore1 < 0 and autovalore2 < 0:
    stability = 'stabile'
else:
    stability = 'instabile'

# Traccia la risposta
plt.plot(t, y)
plt.xlabel('Tempo (s)')
plt.ylabel('Uscita')
plt.title('Risposta al gradino del sistema ({})'.format(stability))
plt.grid(True)
plt.show()