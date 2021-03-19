# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 11:30:43 2020

@author: JARBY II
"""

def devuelve_ciudades(*ciudades):
    for i in ciudades:
        yield from i
#yield from se puede leer como: hacer un yield desde el primer elemento del for i in
ciudades_devueltas=devuelve_ciudades('Madrid', 'Barcelona', 'Bilbao', 'Valencia')

print(next(ciudades_devueltas))
print(next(ciudades_devueltas))