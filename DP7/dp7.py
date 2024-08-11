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

# Mest stabile fasediagrammet, som har mindre SNR
f, ch1, ch2 = np.loadtxt('dp7.csv', 
                  unpack = True,
                  delimiter = ',')

# Fasediagram størst SNR
plt.plot(f, ch1,label="Channel 1 (v_1)")
plt.ylabel('dB')
plt.xlabel('f [Hz]')

# Fasediagram mindre SNR
plt.plot(f, ch2, label="Channel 2 (v_2)")
plt.title('')
plt.ylabel('dB', fontsize=16)
plt.xlabel('f [Hz]', fontsize=16)
plt.ylim((-15, 5))
plt.yticks(np.arange(-15, 5, 2.0))
plt.grid(True)
plt.hlines(-10, 0, 2850, colors="black", zorder=10)
plt.vlines(2850, -15, -10, colors="black")
plt.vlines(2850, -10, 0, colors="grey", linestyle="dotted")
plt.hlines(0, 0, 3800, colors="black", zorder=10, label="Borders")
plt.legend()
plt.vlines(3800, 0, -10, colors="black")
plt.hlines(-10, 3800, 5000, colors="black")
plt.vlines(3800, -15, -10, colors="grey", linestyle="dotted")
plt.hlines(-3, 0, 3800, colors="grey", linestyle="dotted")

plt.show()
