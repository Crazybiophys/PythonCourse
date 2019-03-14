# -*- coding: utf-8 -*-
with open('C:\\rosalind_rna.txt') as dna:
    f=dna.read()
t='rna: '
for i in f:
    if i=='T':
        t+='U'
    else:
        t+=i
print t