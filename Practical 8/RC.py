#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 08:59:07 2020

@author: halowin
"""


import re
seq='ATGCGACTACGATCGAGGGCCAT'
#make original T 'disappear'
result = re.sub(r'T',' ',seq)
#replace A with T
result = re.sub(r'A','T',result)
#replace the space(original T) with A
result = re.sub(r' ','A',result)
#same to C to G and G to C
result = re.sub(r'G',' ',result)
result = re.sub(r'C','G',result)
result = re.sub(r' ','C',result)

  
    
    
print (result) 
        
    