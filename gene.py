#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 21:40:58 2020

@author: halowin
"""

gene_lengths=[9410,3944141,4442,105338,19149,76779,126550,36296,842,15981]
gene_lengths.sort()
del(gene_lengths[0])
del(gene_lengths[8])
print(gene_lengths)

import numpy as np
import matplotlib.pyplot as plt
n=8
length = np.random.uniform(0,4000000,n)
plt.boxplot(length,
            vert = True,
            meanline = False,
            patch_artist=True)
          
            
            
plt.show()
            