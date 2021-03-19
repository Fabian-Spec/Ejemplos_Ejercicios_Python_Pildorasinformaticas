# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 16:52:49 2020

@author: JARBY II
"""

#función sin parametros

def suma():
    num1=5
    num2=7
    print(num1+num2)
    
suma()
suma()
suma()
suma()


#función con parametros, una función puede recibir muchos parametros
def suma(num1, num2):
    print(num1 + num2)
    
suma(5,7)
suma(2,3)
suma(35,358)

"""función con parametros y return, se asemeja a una maquina dispensadora, los parametros son los 
   los numeros que digitamos en la dispensadora, y el return es el producto que nos da la maquina
"""
def suma(num1, num2):
    resultado = num1+num2
    return resultado

print(suma(32,345))
print(suma(14,89))
print(suma(35,35))
