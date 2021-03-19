# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 15:57:40 2020

@author: JARBY II
"""

"""
Tipos de documentos vistos en Python hasta ahora:
int: numero entero
float: numero con decimales
str: cadena de caracteres (números y letras)
dict: directorio (estructura de distintas clases de datos ejem: número enteros caracteres etc, etc)

"""

diccionario = {'nombre': 'Carlos', 
               'apellido': 'girales', 
               'edad': 25,
               'dinero': 5000.25}

print(diccionario['nombre'])
print(diccionario['edad'])

#tambien se puede utilizar el siguiente metodo para llamar un dato del diccionario
print(diccionario.get('dinero'))