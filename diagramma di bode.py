import control as ctrl
import matplotlib.pyplot as plt
import numpy as np

def get_coefficients(prompt):
    while True:
        try:
            return list(map(float, input(prompt).split()))
        except ValueError:
            print("Per favore, inserisci solo numeri separati da spazi.")

# Chiedi all'utente di inserire i coefficienti del numeratore e del denominatore
numerator = get_coefficients("Inserisci i coefficienti del numeratore separati da spazi: ")
denominator = get_coefficients("Inserisci i coefficienti del denominatore separati da spazi: ")

# Chiedi all'utente di inserire la frequenza di inizio e di fine
while True:
    try:
        start_freq = float(input("Inserisci la frequenza di inizio: "))
        end_freq = float(input("Inserisci la frequenza di fine: "))
        break
    except ValueError:
        print("Per favore, inserisci un numero.")

# Crea il sistema di controllo
system = ctrl.TransferFunction(numerator, denominator)

# Crea il diagramma di Bode
plt.figure()
mag, phase, omega = ctrl.bode(system, dB=True, plot=True, omega_limits=(start_freq, end_freq))

# Aggiungi titoli e etichette
plt.suptitle('Diagramma di Bode')
plt.subplot(2, 1, 1)
plt.title('Magnitude')
plt.subplot(2, 1, 2)
plt.title('Phase')
plt.xlabel('Frequency [rad/s]')

# Mostra il grafico
plt.show()