# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 13:02:32 2020

@author: JARBY II
"""

import math

print('Programa de cálculo de raiz cuadrada')
numero=int(input('Introduce un numero por favor: '))

intentos=0


while numero <0:
    print('No se puede hallar la raiz de un número negativo')
    if intentos ==2:
        print('Has consumido demasiados intentos. EL programa ha finalizado')
        break;
        
    numero=int(input('Introduce un numero por favor: '))
    if numero <0:
        intentos=intentos+1

if intentos<2:
    solucion=math.sqrt(numero)
    print('La raiz cuadrada de ' + str(numero) + ' es: ' + str(solucion))        