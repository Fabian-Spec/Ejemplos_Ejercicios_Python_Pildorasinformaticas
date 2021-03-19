# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 11:50:28 2020

@author: JARBY II
"""

#Mi solución
print("Cual numero es el mas alto?")

numero_1 = int(input("Introduce el primer numero a comparar: "))

numero_2 = int(input("Introduce el segundo numero a comparar: "))

def DevuelveMax (numero_1, numero_2):
    if numero_1 > numero_2:
        return("El primero")
    elif numero_2 > numero_1:
        return("El Segundo")
    else:
        return("Los dos numeros son iguales")

print("El numero mas alto es: ", DevuelveMax(numero_1, numero_2))   



#La solución propuesta por pildoras informaticas (El resultado da igual aunque la presentación es distinta)
print("Cual numero es el mas alto?")

numero_1 = int(input("Introduce el primer numero a comparar: "))

numero_2 = int(input("Introduce el segundo numero a comparar: "))

def DevuelveMax (n_1, n_2):
    if n_1 > n_2:
        print("El primero")
    elif n_2 > n_1:
        print("El Segundo")
    else:
        print("Los dos numeros son iguales")

print("El numero mas alto es: " )
DevuelveMax(numero_1, numero_2)   