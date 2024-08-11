#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 17:47:39 2021

@author: sid
"""

import matplotlib.pyplot as plt
import matplotlib.style as style
import numpy as np

style.use('ggplot')

# Fasediagram med størst SNR
x1, y1 = 1000 * np.loadtxt('CSV/fasedg SNR STØRST.csv', 
                  unpack = True,
                  delimiter = ',')

# Oscilloskopet ved største SNR
t, x2, y2 = np.loadtxt('CSV/oscilloscop SNR STØRST-kopi.csv', 
                  unpack = True,
                  delimiter = ',')

# Mest stabile fasediagrammet, som har mindre SNR
x3, y3 = 1000 * np.loadtxt('CSV/fasedg SNR mindre.csv', 
                  unpack = True,
                  delimiter = ',')

# Oscilloskopet for fasediagrammet med mindre SNR
t4, x4, y4 = np.loadtxt('CSV/oscilloscop SNR mindre-kopi.csv', 
                  unpack = True,
                  delimiter = ',')


# Fasediagram størst SNR
plt.plot(x1, y1)
plt.title('Fasediagram for R = 3.96k ohm.')
plt.ylabel('v_L(t) [mV]')
plt.xlabel('y(t) [mV]')
plt.show()

# Oscilloscope størst SNR
plt.plot(10**3 * t, x2*1000, label="y (t)")
plt.plot(10**3 * t, y2*1000, label="v_L (t)")
plt.title('Signal gjennom y(t) og spolen v_L(t)')
plt.ylabel('Spenning [mV]')
plt.xlabel('Tid (ms)')
plt.legend()
plt.show()

# Fasediagram mindre SNR
plt.plot(x3, y3)
plt.title('Fasediagram for R = 1.3k ohm.')
plt.ylabel('v_L(t) [mV]')
plt.xlabel('y(t) [mV]')
plt.show()

# Oscilloscope mindre SNR
plt.plot(10**3 * t4, 1000 * x4, label="y (t)")
plt.plot(10**3 * t4, 1000 * y4, label="v_L (t)")
plt.title('Signal gjennom y(t) og spolen v_L(t)')
plt.ylabel('Spenning [mV]')
plt.xlabel('Tid (ms)')
plt.legend()
plt.show()


