# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 15:47:47 2020

@author: JARBY II
"""

lista = [1,2 ,3, "erqwer", 20.0]
for contador in lista:
    print(contador)

diccionario = {
    "nombre": "Fabian",
    "edad": 12313,
    "nacionalidad": "Colombiano"
    }

clave = diccionario.keys

print(clave)

valor = diccionario.values()

print(valor)

dato = diccionario.items()

for clave, valor in dato:
    print(clave + " -> " + str(valor))
    






