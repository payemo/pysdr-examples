import numpy as np
import matplotlib.pyplot as plt

fs = 1000 # Частота дискретизації в Гц.
t = np.arange(0, 1, 1/fs)

# Частота сигналу
f = 50 # 50Гц

# Генерація I-компоненти
I = np.cos(2 * np.pi * f * t)

# Генерація Q-компоненти
Q = np.sin(2 * np.pi * f * t)

# Візуалізація IQ сигналу
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(t, I, label='I-компонента (In-phase)')
plt.title('I-компонента')
plt.xlabel('Час [c]')
plt.ylabel('Амплітуда')
plt.grid(True)
plt.legend()

plt.subplot(2, 1, 1)
plt.plot(t, Q, label='Q-компонента (Quadrature)', color='orange')
plt.title('Q-компонента')
plt.xlabel('Час [c]')
plt.ylabel('Амплітуда')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()

# Розрахунок FFT для I-компоненти
fft_I = np.fft.fft(I)
fft_Q = np.fft.fft(Q)

# Амплітудний спектр
freqs = np.fft.fftfreq(len(t), 1/fs)

# Побудова амплітудного спектру
plt.figure(figsize=(12, 6))

plt.plot(freqs[:len(freqs)//2], np.abs(fft_I)[:len(freqs)//2], label='Спектр I-компоненти')
plt.plot(freqs[:len(freqs)//2], np.abs(fft_Q)[:len(freqs)//2], label='Спектр Q-компоненти', color='orange')

plt.title('Спектральний аналіз IQ-сигналу')
plt.xlabel('Частота [Гц]')
plt.ylabel('Амплітуда')
plt.grid(True)
plt.legend()
plt.show()