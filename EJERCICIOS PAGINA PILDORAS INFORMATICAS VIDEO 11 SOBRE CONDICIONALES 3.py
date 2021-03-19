# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 11:50:28 2020

@author: JARBY II
"""

# Mi solución
print("Media Movil Aritmética de tres Números")

numero_1 = int(input("Ingrese el Primer Número: "))
numero_2 = int(input("Ingrese el Segundo Número: ")) 
numero_3 = int(input("Ingrese el Tercer Número: ")) 

def Media_Movil (numero_1,numero_2, numero_3):
    media_aritmética = "%.2f" %((numero_1 + numero_2 + numero_3)/3)
    return (media_aritmética)

print("La media movil de los tres numeros es: ", Media_Movil(numero_1, numero_2, numero_3))


   
#La solución propuesta por pildoras informaticas (El resultado da igual aunque la presentación es distinta)

num1 = int(input("Ingrese el Primer Número: "))
num2 = int(input("Ingrese el Segundo Número: ")) 
num3 = int(input("Ingrese el Tercer Número: ")) 

media= ((num1 + num2 + num3)/3)

print("La media movil de los tres numeros es: ")
print(media)