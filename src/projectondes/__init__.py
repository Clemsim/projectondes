import numpy as np
import matplotlib.pyplot as plt

def main() -> int:
    print("Hello from projectondes!")
    plt.plot(np.sin(np.linspace(0, 2*np.pi, 100)))
    plt.show()
    return 0
