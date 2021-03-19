# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 09:32:26 2020

@author: JARBY II
"""

def generapares (limite):
    num=1
    while num <limite:
        yield num*2
        num=num+1

devuelvepares= generapares(10)

for i in devuelvepares:
    print(i)
    