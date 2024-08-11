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

# Effektspekter filen
f, P_x = np.loadtxt('dBm_ExpdBAverage_100_tests.csv', 
                  unpack = True,
                  delimiter = ',')

# Fullt effektspekter P_x
plt.plot(f, P_x,label="Effektspekteret til x(t)")

#plt.title('Effektspekter på x(t)')
plt.ylabel('P_x(f) [dBm]', fontsize=16)
plt.xlabel('f [Hz]', fontsize=16)
plt.grid(True)
plt.show()


# Effektspekter zoomet in på f_1 og f_2 respektivt
# f_1
plt.plot(f, P_x,label="Effektspekter på x(t)")

#plt.title('Båndbredde for Båndpass 1')
plt.ylabel('P_x(f) [dBm]', fontsize=16)
plt.xlabel('f [Hz]', fontsize=16)
plt.grid(True)
plt.xlim(1555,1570)
plt.show()

# f_2
plt.plot(f, P_x,label="Effektspekter på x(t)")

#plt.title('Båndbredde for Båndpass 2')
plt.ylabel('P_x(f) [dBm]', fontsize=16)
plt.xlabel('f [Hz]', fontsize=16)
plt.grid(True)
plt.xlim(870,885)
plt.show()


# Scope
# f_1
# Effektspekter filen
t1, V1 = np.loadtxt('f1_scope.csv', 
                  unpack = True,
                  delimiter = ',')

t1 = t1 * 1000

# Fullt effektspekter P_x
plt.plot(t1, V1)

plt.title('Scope f_1')
plt.ylabel('x(t) [V]', fontsize=16)
plt.xlabel('t [ms]', fontsize=16)
plt.grid(True)
plt.xlim(0)
plt.ylim(-2,2)
plt.show()

# f_2
# Effektspekter filen
t2, V2 = np.loadtxt('f2_scope.csv', 
                  unpack = True,
                  delimiter = ',')
t2 = t2*1000
# Fullt effektspekter P_x
plt.plot(t2, V2,label="Effektspekteret til x(t)")

plt.title('')
plt.ylabel('x(t) [V]', fontsize=16)
plt.xlabel('t [ms]', fontsize=16)
plt.grid(True)
plt.xlim(0)
plt.ylim(-2,2)
plt.show()

# CLK
# Effektspekter filen
t_C, V3 = np.loadtxt('CLK_signal.csv', 
                  unpack = True,
                  delimiter = ',')

# Fullt effektspekter P_x
plt.plot(t_C, V3,label="Effektspekteret til x(t)")

plt.title('Klokkesignal')
plt.ylabel('v_T(t) [V]', fontsize=16)
plt.xlabel('t [s]', fontsize=16)
plt.grid(True)
plt.xlim(0, 4)
plt.ylim(-5, 5)
plt.show()

# Scope
# Frekvensskift høy til lav
t4, V4 = np.loadtxt('Frequency shift.csv', 
                  unpack = True,
                  delimiter = ',')
t4 = t4*1000
plt.plot(t4, V4,label="Effektspekteret til x(t)")

plt.title('')
plt.ylabel('x(t) [V]', fontsize=16)
plt.xlabel('t [ms]', fontsize=16)
plt.grid(True)
plt.xlim(70, 80)
plt.ylim(-2, 2)
plt.show()

# Frekvensskift høy til lav
t5, V5 = np.loadtxt('Frequency shift_low_to_high.csv', 
                  unpack = True,
                  delimiter = ',')
t5 = t5*1000
plt.plot(t5, V5,label="Effektspekteret til x(t)")

plt.title('')
plt.ylabel('x(t) [V]', fontsize=16)
plt.xlabel('t [ms]', fontsize=16)
plt.grid(True)
plt.xlim(61, 67)
plt.ylim(-2, 2)
plt.show()

# Signalnivå for R_L = 600ohm
t6, Last = np.loadtxt('600ohmScope.csv', 
                  unpack = True,
                  delimiter = ',')
t6 = t6*1000

dBLast = Last.size * [0]

for i in range(0, Last.size):
    if(Last[i] >= 0):
        dBLast[i] = 20*np.log10(Last[i])
    else:
        dBLast[i] = 20*np.log10(-Last[i])

#plt.plot(t7, dBUtenLast,label="Uten R_L")
plt.plot(t6, dBLast, label='Med R_L')
plt.title('')
plt.ylabel('x(t) [V]', fontsize=16)
plt.xlabel('t [ms]', fontsize=16)
plt.grid(True)
plt.show()






