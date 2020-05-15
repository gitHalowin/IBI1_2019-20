#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 14 23:51:27 2020

@author: halowin
"""

import numpy as np
import matplotlib.pyplot as plt
time = 100
beta = 0.3
gamma = 0.05
population = np.zeros((100,100))
outbreak = np.random.choice(range(100), 2)
#0=S 1=I 2=R
population[outbreak[0], outbreak[1]] = 1
plt.figure(figsize =(6,4) , dpi =150)
plt.imshow(population, cmap='viridis', interpolation= 'nearest')
plt.show()

count = 0
while count != 100:
    infectedIndex = np.where(population == 1)
    for i in range(len(infectedIndex[0])):
        x = infectedIndex[0][i]
        y = infectedIndex[1][i]
        for xNeighbour in (x - 1, x + 1):
            for yNeighbour in (y - 1, y + 1):
                if xNeighbour != -1 and yNeighbour != -1 and xNeighbour != 100 and yNeighbour != 100 and  population[xNeighbour, yNeighbour] == 0:
                    population[xNeighbour, yNeighbour] = np.random.choice(range(2), 1, p=[1 - beta, beta])[0]
        population[x, y] = np.random.choice((1,2), 1, p=[1-gamma,gamma])[0]
    plt.imshow(population, cmap='viridis', interpolation='nearest')
    plt.show()
    plt.close()