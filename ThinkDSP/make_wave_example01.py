import thinkdsp
import matplotlib.pyplot as plt

# Create a sine signal with a frequency of 440 Hz (A4 note)
signal = thinkdsp.CosSignal(freq=440, amp=1.0, offset=0)

# Generate a wave from the signal with a duration of 1 second and a framerate of 44,100 Hz
wave = signal.make_wave(duration=1.0, framerate=44100)

# Plot the wave
wave.plot()
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('440 Hz Sine Wave')
plt.show()

# Play the wave (optional if you have an audio player configured)
wave.play()
