# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 09:32:26 2020

@author: JARBY II
"""

#Generador para devolver o imprimir valor a valor con el uso del metodo Nex



def generapares(limite):
    num=1
    while num<limite:
        yield num*2
        num=num+1

devuelvepares= generapares(4)

print(next(devuelvepares))
print('Por ejemplo mas codigo')    
print(next(devuelvepares))
print('Por ejemplo mas codigo')    
print(next(devuelvepares))
print('Por ejemplo mas codigo')    
print(next(devuelvepares))
print('Por ejemplo mas codigo')    

