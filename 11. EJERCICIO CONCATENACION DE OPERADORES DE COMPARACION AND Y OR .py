# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 15:54:25 2020

@author: JARBY II
"""

print('Programa de becas Año 2020')

distancia_escuela=int(input('Introduce la distancia a la escuela en km '))
print(distancia_escuela)

numero_hermanos=int(input('Introduce el numero de hermanos '))
print(numero_hermanos)

salario_familiar=int(input('Introduce el salario familiar anual '))
print(salario_familiar)

if distancia_escuela > 40 and numero_hermanos >2 or salario_familiar <= 20000:
    print('Tienes derecho a una Beca')
    
else:
    print('no tienes derecho a una Beca')
    
