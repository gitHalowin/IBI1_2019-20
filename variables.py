#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 15:06:19 2020

@author: halowin
"""

a=527
b=527527
b%7==0
c=b/7
d=c/11
e=d/13
e>a

X=True;
Y=False;
Z=(X and not Y) or (Y and not X);
if Z is True:
    print(1);
else:
    print(0);
W= X!=Y
if W==Z is True:
    print(1)