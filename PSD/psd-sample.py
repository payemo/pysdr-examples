import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import periodogram

# Генеруємо тестовий сигнал
Fs = 1000
t = np.linspace(0, 1, Fs, endpoint=False)
# Сигнал, що складається з двох синусоїдальних хвиль
sig = 0.5 * np.sin(2 * np.pi * 50 * t) + 0.3 * np.sin(2 * np.pi * 120 * t)

# Обчислення PSD за допомогою періодограми
freqs, power_density = periodogram(sig, Fs)

plt.figure(figsize=(10, 6))
plt.semilogy(freqs, power_density)
plt.title('Спектральна щільність потужності (PSD)')
plt.xlabel('Частота [Гц]')
plt.ylabel('PSD (Вт/Гц)')
plt.grid(True)
plt.show()