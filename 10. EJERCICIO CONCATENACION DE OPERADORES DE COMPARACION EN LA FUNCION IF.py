# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 17:04:16 2020

@author: JARBY II
"""

salario_presidente=int(input('Introduce el salario del presidente '))
print('El salario del presidente es: ' + str(salario_presidente))

salario_director=int(input('Introduce el salario del director '))
print('El salario del director es: ' + str(salario_director))

salario_jefe_area=int(input('Introduce el salario del jefe de area '))
print('El salario del jefe de area es: ' + str(salario_jefe_area))

salario_administrativo=int(input('Introduce salario del Administrativo '))
print('El salario del administrativo es: '+ str(salario_administrativo))

if salario_administrativo<salario_jefe_area<salario_director<salario_presidente:
    print('Todo funciona correctamente')
else:
    print('Algo falla en esta empresa')
        
