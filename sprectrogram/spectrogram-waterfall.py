import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from rtlsdr import RtlSdr

# Initialize the SDR
sdr = RtlSdr()

# Configure SDR settings
sdr.sample_rate = 2.4e6  # 2.4 MHz sample rate
sdr.center_freq = 100e6  # 100 MHz center frequency
sdr.gain = 'auto'  # Automatic gain control

# Define FFT parameters
fft_size = 1024
sdr.rx_buffer_size = fft_size
num_rows = 100  # Number of rows to display in the spectrogram

# Initialize a 2D array to hold FFT results
waterfall_2darray = np.zeros((num_rows, fft_size))

# Function to get a single FFT result
def get_fft():
    samples = sdr.read_samples(fft_size)
    fft_result = np.fft.fftshift(np.abs(np.fft.fft(samples)))
    return 10 * np.log10(fft_result + 1e-6)  # Convert to dB scale and prevent log(0)

# Populate the 2D array with initial FFT results
for i in range(num_rows):
    waterfall_2darray[i, :] = get_fft()

# Plot setup
fig, ax = plt.subplots()
cax = ax.imshow(waterfall_2darray, aspect='auto', cmap='viridis', origin='lower')
plt.colorbar(cax, ax=ax, label='Power (dB)')
ax.set_title('Spectrogram/Waterfall Plot')
ax.set_xlabel('Frequency Bins')
ax.set_ylabel('Time (Frames)')

# Function to update the plot
def update_frame(frame):
    new_fft = get_fft()
    global waterfall_2darray
    waterfall_2darray = np.roll(waterfall_2darray, -1, axis=0)
    waterfall_2darray[-1, :] = new_fft
    cax.set_array(waterfall_2darray)
    return cax,

# Animate the plot for live updating
ani = animation.FuncAnimation(fig, update_frame, interval=50, blit=False)

plt.show()

# Close the SDR when done
sdr.close()
