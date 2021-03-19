# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 16:54:09 2021

@author: JARBY II
"""

def evaluaEdad (edad):
    if edad <0:
        raise TypeError ('No se puede introducir edades negativas')
    if edad<20:
        return 'Eres muy joven'
    elif edad<40:
        return'Eres joven'
    elif edad<65:
        return'Eres maduro'
    elif edad<100:
        return'Cuidate'
        
print(evaluaEdad(-15))
    
    
    
        
    
    