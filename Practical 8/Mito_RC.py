#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 11 22:26:23 2020

@author: halowin
"""

f = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')
o = f.read()
r = open('rc_mito.fa','w')

import re
mito = re.findall('(>.*?:Mito:[\d\D]+?gene:.*\n[\d\D]+?)>',o)
for gene in mito:
   M = re.sub(r'>.*?gene:?(.*? )gene.*?]',r'\1',gene)
   seq = M.split(' ')[1]
   name = M.split(' ')[0]
   seq = re.sub('\n','',seq)
   length = len(str(seq))
   result = re.sub(r'T',' ',seq)
   result = re.sub(r'A','T',result)
   result = re.sub(r' ','A',result)
   result = re.sub(r'G',' ',result)
   result = re.sub(r'C','G',result)
   result = re.sub(r' ','C',result)
     
      
   output = '>' + name + ' ' + str(length) + '\n' + result
   r.writelines(output + '\n')
r.close()
print (open('rc_mito.fa').read())
