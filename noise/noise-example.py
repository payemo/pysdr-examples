import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq

# Guassian noise parameters
fs = 1000 # Sampling frequency in Hz
duration = 1 # in seconds
n_samples = fs * duration

# Generate Gaussian nose
gaussian_noise = np.random.normal(0, 1, n_samples)
time = np.linspace(0, duration, n_samples, endpoint=False)

# FFt to convert to frequency domain
fft_values = fft(gaussian_noise)
freqs = fftfreq(n_samples, 1/fs)
power_spectrum = np.abs(fft_values) ** 2

# Plot time-domain representation
plt.figure(figsize=(18, 5))
plt.subplot(1, 3, 1)
plt.plot(time, gaussian_noise, color='blue')
plt.title('Gaussian noise in Time Domain')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')

# Plot frequency-domain representation
plt.subplot(1, 3, 2)
plt.plot(freqs[:n_samples//2], np.abs(fft_values[:n_samples//2]), color='green')
plt.title('Gaussian Noise in Frequency Domain')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Amplitude')

# Plot power spectral density
plt.subplot(1, 3, 3)
plt.plot(freqs[:n_samples//2], power_spectrum[:n_samples//2], color='red')
plt.title('Power Spectral Density of Gaussian Noise')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Power')

plt.tight_layout()
plt.show()