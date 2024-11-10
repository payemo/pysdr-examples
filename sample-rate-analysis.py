import numpy as np
import adi
import time

# Initial configurations
sample_rate = 5e6  # Adjusted sample rate (Hz)
center_freq = 100e6  # Hz
buffer_size = 8192  # Increased buffer size

# Configure the Pluto SDR
sdr = adi.Pluto("ip:192.168.2.1")
sdr.sample_rate = int(sample_rate)
sdr.rx_rf_bandwidth = int(sample_rate)  # Set filter cutoff
sdr.rx_lo = int(center_freq)
sdr.rx_buffer_size = buffer_size

# Variables to track samples and time
total_samples_received = 0
iterations = 100
start_time = time.time()

# Receive samples in a loop
for _ in range(iterations):
    samples = sdr.rx()  # Receive samples from Pluto
    total_samples_received += len(samples)  # Count the samples received

end_time = time.time()

# Calculate elapsed time and sample rate achieved
elapsed_time = end_time - start_time
samples_per_second = total_samples_received / elapsed_time

print(f"Total samples received: {total_samples_received}")
print(f"Elapsed time: {elapsed_time:.2f} seconds")
print(f"Samples per second achieved: {samples_per_second:.2f} samples/second")

# Analysis and instructions for experimentation:
# 1. Increasing the buffer_size may reduce the frequency of data drops by allowing more data to be collected in each cycle, improving sample capture efficiency.
# 2. Decreasing the sample_rate can help ensure all samples are received without drops, as a lower sample rate demands less bandwidth and processing power.
# 3. If the achieved samples per second is consistently lower than the set sample_rate, data loss is occurring, indicating the need to either reduce the sample_rate or increase buffer_size.
# 4. Monitor CPU usage and USB bandwidth when running tests at high sample_rate values. USB 2.0 limitations can lead to data bottlenecks, causing packet loss.
# 5. Test different combinations of buffer_size and sample_rate to determine the configuration that maximizes sample retention while minimizing data loss.
