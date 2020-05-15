#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 14 21:59:29 2020

@author: halowin
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from collections import Counter

#set 1000 times of loop
plt.figure(figsize=(6,4),dpi = 150)
plt.title('SIR model with different vaccination rates')
plt.xlabel('time')
plt.ylabel('number of people')
for i in [0,10,20,30,40,50,60,70,80,90,100]:
    N = 10000
    I = 1
    gamma = 0.05
    R = int(i * N / 100)
    S = 9999 - R
    infected = []
    count = 0
    while count != 1000:
        count += 1
        p_inf = 0.3 * I / N
        s_inf = np.random.choice([1,2],S,p=[1-p_inf,p_inf])
        S = S - Counter(s_inf)[2]
        I = I + Counter(s_inf)[2]
        i_rec = np.random.choice([1,2],I,p=[1-gamma,gamma])
        I = I - Counter(i_rec)[2]
        R = R + Counter(i_rec)[2]
        infected.append(I)
    plt.plot(infected,color=cm.viridis(i*4),label=str(i)+"%")
    
legend = plt.legend(loc='upper right')
plt.show()




