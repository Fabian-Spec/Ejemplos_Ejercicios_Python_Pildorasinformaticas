# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 11:47:35 2021

@author: JARBY II
"""

#Forma tradicional de invocar el modulo

import funciones_matematicas

funciones_matematicas.sumar(5,7)

funciones_matematicas.restar(5,7)

funciones_matematicas.multiplicar(5,7)


#1° forma abreviada de invocar el modulo, el inconveniente es que toca nombrar cada metodo que se vaya a usar

from funciones_matematicas import sumar
from funciones_matematicas import restar

sumar(5,7)
restar(5,7)


#2° forma abreviada de invocar el modulo, con el * se invocan todos los metodos, pero esto hace que el codigo
# se vuelva ineficiente cuando hay muchos metodos.

from funciones_matematicas import *

sumar(5,7)
restar(5,7)
multiplicar(5,7)

