# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 11:30:43 2020

@author: JARBY II
"""

def devuelve_ciudades(*ciudades):
    # para el For se puede poner en el for cualquier nombre ejemlo elemento, para
    # este ejemplo se pone i
    for i in ciudades:
        #para este For igualmente se puede poner cualquier nombre en este ejemplo sub_i
        #lo ideal es que haga referencia a que se busca el sub elemento del primer bucle
        for sub_i in i:
            yield sub_i
        
ciudades_devueltas=devuelve_ciudades('Madrid', 'Barcelona', 'Bilbao', 'Valencia')

print(next(ciudades_devueltas))
print(next(ciudades_devueltas))