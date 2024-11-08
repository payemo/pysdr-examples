import numpy as np
import matplotlib.pyplot as plt

# Кількість точок сузір'я для QPSK
num_symbols = 4

# Визначення фазових точок для QPSK (0°, 90°, 180°, 270°)
angles = np.array([0, np.pi/2, np.pi, 3 * np.pi / 2])

qpsk_symbols = np.exp(1j * angles)

# Побудова графіка сузір'я
plt.figure(figsize=(8, 8))
plt.scatter(qpsk_symbols.real, qpsk_symbols.imag, color='blue', s=100)

for i, symbol in enumerate(qpsk_symbols):
    plt.text(symbol.real, symbol.imag, f'{i}', fontsize=12, ha='center', va='center')

plt.axhline(0, color='gray', linewidth=0.5, linestyle='--')
plt.axvline(0, color='gray', linewidth=0.5, linestyle='--')
plt.title('Графік сузір\'я для QPSK')
plt.xlabel('Реальна частина')
plt.ylabel('Уявна частина')
plt.grid(True)
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)
plt.show()