#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  9 17:55:33 2020

@author: halowin
"""

import os
os.chdir('/Users/halowin/Desktop/py file')           
f1 = open('SOD2_human.fa','r')
f2 = open('RandomSeq.fa','r')
seq1 = f1.read()
seq2 = f2.read()

import re
x = re.findall(r'\S+Q\S+',seq1)
y = re.findall(r'\S+Q\S+',seq2)
x = str(x)
y = str(y)


distance = 0
i = 0
s = min(len(x),len(y))
for i in range(s):
    if x[i] != y[i]:
        distance += 1
        i += 1
    else:
        i += 1
 
print (str(distance))

