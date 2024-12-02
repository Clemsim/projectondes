import numpy as np
import matplotlib.pyplot as plt

def main() -> int:
    # Paramètres
    L = 10  # Longueur de propagation
    dz = 0.1  # Pas d'espace
    dt = 0.01  # Pas de temps
    n2 = 1e-16  # Coefficient de Kerr
    omega = 2*np.pi  # Pulsation

# Initialisation
    z = np.arange(0, L+dz, dz)
    t = np.arange(0, 10, dt)
    E = np.zeros((len(z), len(t)), dtype=complex)
    E[0, :] = np.exp(1j*omega*t)  # Condition initiale

# Boucle de propagation
    for i in range(1, len(z)):
        E[i, :] = E[i-1, :] + 1j*dz/2*(np.fft.fft(np.abs(E[i-1, :])**2*E[i-1, :]))

# Visualisation
    plt.plot(t, np.abs(E[-1, :])**2)
    plt.xlabel('Temps')
    plt.ylabel('Intensité')
    plt.show()

    return 0
