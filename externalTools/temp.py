import pygame.midi
import numpy as np
import IPython

""" T = 2.0    # seconds
sr = 22050 # sample rate
t = np.linspace(0, T, int(T*sr), endpoint=False) # time variable
x = 0.5*np.sin(2*np.pi*440*t)                # pure sine wave at 440 Hz
IPython.display.Audio(x, rate=sr) """

pygame.midi.init()

for i in range(pygame.midi.get_count()):
    print(pygame.midi.get_device_info(i))


