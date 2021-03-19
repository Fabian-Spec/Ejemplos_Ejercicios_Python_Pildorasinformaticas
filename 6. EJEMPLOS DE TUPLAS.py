# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 11:18:08 2020

@author: JARBY II
"""

#Acceder al elemento de una Tupla
mitupla = ('Juan',13,1, 1995)
print (mitupla[2])

#Convertir una tupla en lista
mitupla = ('Juan',13,1, 1995)
milista = list(mitupla)
print(milista)
print(mitupla)


#Pasar unas lista a Tupla
milista = ['Juan',13,1, 1995,13]
mitupla=tuple(milista)
print(mitupla)
print(milista)

#Ejecutar Metodo in para confirmar si un elemento se encuentra en la Tupla
print('Juan' in mitupla)

#Metodo Count para saber cuantes veces se encuetra un elemento dentro de una Tupla
print(mitupla.count(13))

#MEtodo Len para saver el numero de documentos con los que cuenta la tupla, la longitud de numeros de elementos
print(len(mitupla))


#Ejemplo Tupla Unitaria
mitupla=('Juan',)
print(len(mitupla))

#Hacer tupla sin parentesis se llama empaquetamiento de Tupla, sin emvargo es necesario los parentesis cuando se usen funciones con parametros por tal motivo siempres se recomienda usa parentesis
mitupla = 'Juan',13,1,1995
print(mitupla)

#Desempaquetado de tuplas
mitupla=('Juan',13,1,1995)
nombre, dia, mes, agno = mitupla
print(nombre)
print(dia)
print(agno)
print(mes)






