#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 10:38:49 2020

@author: halowin
"""


dna = 'ATGCTTCAGAAAGGTCTTACG'
count = {}
for i in dna:
    if i not in count:
        count[i] = 1
    else:
        count[i] += 1
print(count)
     
labels = []
times = []

for k,v in count.items():
    labels.append(k)
    times.append(v)


import matplotlib.pyplot as plt
colors=['lemonchiffon','paleturquoise','lavenderblush','honeydew']
plt.pie(times,explode=None,labels=labels,colors=colors,autopct='%1.1f%%',shadow=False,startangle=90)
plt.title('pie of the four DNA nucleotides')
plt.axis('equal')



plt.show()

