# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 16:05:23 2020

@author: JARBY II
"""

def calcular_iva(precio_producto):
    resultado = precio_producto*1.19
    print(resultado)
    return resultado

precio = int(input("Ingrese el precio del producto: ")) 
print("El valor total a pagar es: ", calcular_iva(precio))


   
    