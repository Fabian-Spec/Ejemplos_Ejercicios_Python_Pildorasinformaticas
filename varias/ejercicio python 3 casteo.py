# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 13:51:57 2020

@author: JARBY II
"""

#ejemplo de casteo, concatenación y input precio como numero entero


num = 21341
print(type(num))

casteo = num
print(type(casteo))

casteo = str(num)
print(type(casteo))

print("mi numero es: " + str(num) + " hola mundo")

precio = int(input("introduzca el precio del articulo: "))

print(precio)

