import math

signal_power = input('Enter a signal power :')
noise_power = input('Enter a noise power :')

signal_power = float(signal_power)
noise_power = float(noise_power)

ratio = signal_power / noise_power
decibels = 10 * math.log10(ratio)

print(decibels)
