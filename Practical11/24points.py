#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 09:38:20 2020

@author: halowin
"""

import random
from itertools import product
#define a function for a two-element list
def op_per_group(a,b):
    h = []
    for i in ["+","-","*","/"]:
        #combine the numbers and operations into a string
        string = "str(a) + i + str(b)"
        #turn the string into a computable formula
        result = eval(string)
        r = eval(result)
        #save the results
        h.append(r)
    return h
    
Input = [1,2,3,4]
#randomly select 2 numbers from Input
g1 = random.sample(Input,2)
#make the rest 2 another list
g2 = [x for x in Input if x not in g1]
#put the groups in the function
result1 = op_per_group(*g1)
result2 = op_per_group(*g2)
#combine one of the numbers from result1 and one from result2 iterably
merge = product(result1,result2)
point = []
points = []
#put all the final results in the function
for i in list(merge):
    point.append(op_per_group(*list(i)))
#change to an entire list
for i in point:
    points.extend(i)
if 24 in points:
    print ("Yes")
    #Since I merge massively, the recursion times was set as where 24 first appears in the points list
    print ("Recursion times: " + str(points.index(24)))
else:
    print ("No")
   
   

            
     
    

     



    


    
    
    
    