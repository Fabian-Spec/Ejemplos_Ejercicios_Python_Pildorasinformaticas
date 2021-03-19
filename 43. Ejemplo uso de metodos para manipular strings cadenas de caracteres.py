# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 11:44:42 2021

@author: JARBY II
"""

nombre_usuario=input('Introduce tu nombre aqui: ')

print('El nombre es: ', nombre_usuario)

print('Uso metodo upper, para pasar el string a mayuscula: ', nombre_usuario.upper())

print('Uso metodo lower, para pasar el string a minuscula: ', nombre_usuario.lower())

print('Uso metodo capitalize, para pasar el string a nombre propio: ', nombre_usuario.capitalize())

print('Uso metodo count, para contar cuantas veces esta la letra a en el nombre: ', nombre_usuario.count('a'))

print('Uso metodo find, indicar la posicion de un elemento dentro del nombre en este caso la letra n: ', nombre_usuario.find('n'))
      
print('Uso metodo isdigit, para indicar si el nombre es un elemento numero o int: ', nombre_usuario.isdigit())

print('Uso metodo isalnum, para indicar si todos los caracteres de la cadena son alfanuméricos y hay al menos un carácter. En caso contrario, devuelve falso: ', nombre_usuario.isalnum())

print('Uso metodo split, para separar los elementos del string con espacios entre los mismos: ', nombre_usuario.split())

print('Uso metodo strip, para borrar la primera y la ultima letra entro del nombre : ', nombre_usuario.strip('f.o'))

print('Uso metodo replace, para pasar la x por la f: ', nombre_usuario.replace('f','x'))

print('Uso metodo rfind, para indicar la posición en este caso de la letra z dentro del string: ', nombre_usuario.rfind('z'))
      