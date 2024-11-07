import numpy as np
import matplotlib.pyplot as plt

Fs = 1 # 1Hz
N = 100 # кількість точок для моделювання та розмір нашого ШПФ

t = np.arange(N)
s = np.sin(0.15 * 2 * np.pi * t)
S = np.fft.fftshift(np.fft.fft(s))

S_mag = np.abs(S)
S_phase = np.angle(S)
f = np.arange(Fs/-2, Fs/2, Fs/N)

plt.figure(0)
plt.plot(f, S_mag, '.-')
plt.figure(1)
plt.plot(f, S_phase, '.-')
plt.show()