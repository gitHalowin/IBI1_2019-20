#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 12 21:51:41 2020

@author: halowin
"""

import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
#list the initial values
N = 10000
S = 9999
I = 1
R = 0
beta = 0.3


gamma =0.05

susceptible = []
infected = []
recovered = []
count = 0
#set 1000 times of loop
while count != 1000:
    count += 1
    p_inf = 0.3 * I / N
    #random choose infected from susceptible
    s_inf = np.random.choice([1,2],S,p=[1-p_inf,p_inf])
    #adjust population
    S = S - Counter(s_inf)[2]
    I = I + Counter(s_inf)[2]
    #random choos recovered from infected
    i_rec = np.random.choice([1,2],I,p=[1-gamma,gamma])
    I = I - Counter(i_rec)[2]
    R = R + Counter(i_rec)[2]
    susceptible.append(S)
    infected.append(I)
    recovered.append(R)
   
    
plt.plot(susceptible,'-b',label="susceptible")
plt.plot(infected,color="orange",label="infected")
plt.plot(recovered,'-g',label="revovered")
plt.legend()
plt.xlabel("time")
plt.ylabel("number of people")
plt.title("SIR model")
plt.show()
    
   
    
        