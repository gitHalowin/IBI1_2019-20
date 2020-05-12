#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 14:56:15 2020

@author: halowin
"""

f = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')
o = f.read()
script = open('mito_gene.fa','w')

import re
#extract mitochoria genes
mito = re.findall('(>.*?:Mito:[\d\D]+?gene:.*\n[\d\D]+?)>',o)
#replace the element in mito with only the name and its sequence
for gene in mito:
   M = re.sub(r'>.*?gene:?(.*? )gene.*?]',r'\1',gene)
   #split each string into gene name and sequence
   seq = M.split(' ')[1]
   seq = re.sub('\n','',seq)
   lengths = str(len(seq))
   names = M.split(' ')[0] 
  

   #recompile the string
   output = '>' + names + ' ' + lengths
   
   script.writelines(output+'\n')

script.close()
print(open('mito_gene.fa').read())
   