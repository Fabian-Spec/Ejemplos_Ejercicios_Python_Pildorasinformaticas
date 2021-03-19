# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 11:50:28 2020

@author: JARBY II
"""

#Mi Solución
print("Programa datos Personales")

Nombre = str(input("Por favor ngrese su Nombre: "))
Dirección = str(input("Por favor ngrese su Dirección: "))
Numero_telefono = int(input("Por favor ngrese su numero de Telefono: "))

Datos_personales=[Nombre,Dirección, Numero_telefono]

print("Los datos personales son: ",
      "Nombre: ", (Datos_personales[0]),
      "Dirección: ", (Datos_personales[1]),
      "Telefono: ", (Datos_personales[2]))

      
#La solución propuesta por pildoras informaticas (El resultado da igual aunque la presentación es distinta)
print("Programa datos Personales")

Nombre = input("Por favor ngrese su Nombre: ")
Dirección = input("Por favor ngrese su Dirección: ")
Numero_telefono = input("Por favor ngrese su numero de Telefono: ")

Datos_personales=[Nombre,Dirección, Numero_telefono]

print("Los datos personales son: "+ Datos_personales[0] + " " + (Datos_personales[1]) + " " + (Datos_personales[2]))
