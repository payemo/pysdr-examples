import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import spectrogram

fs = 1000 # Частота дискретизації (Гц)
T = 2 # Тривалість сигналу (с)
t = np.linspace(0, T, T * fs, endpoint=False)

# Створення комбінованого сигналу
signal = np.sin(2 * np.pi * 50 * t) + 0.5 * np.sin(2 * np.pi * 120 * t)

# Додавання шуму
noise = 0.2 * np.random.normal(size=t.shape)
signal += noise

# Будуємо спектрограму
frequencies, times, Sxx = spectrogram(signal, fs)

plt.figure(figsize=(10, 6))
plt.pcolormesh(times, frequencies, 10 * np.log10(Sxx), shading='gouraud')
plt.colorbar(label='Потужність (дБ)')
plt.ylabel('Частота (Гц)')
plt.xlabel('Час (с)')
plt.title('Спектрограма сигналу')
plt.show()