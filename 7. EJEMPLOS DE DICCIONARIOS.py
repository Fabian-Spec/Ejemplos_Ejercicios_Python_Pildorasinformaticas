# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 12:46:56 2020

@author: JARBY II
"""

#Imprimier un elemento de un diccionario mediante la lave
midiccionario={'Alemania':'Berlin', 'Francia':'Paris', 'Reino Unido': 'Londres','España':'Madrid'}
print(midiccionario['Francia'])

#Agregar un elemento al diccionario 
midiccionario['Italia']= 'Lisboa'
print(midiccionario)

#Cambiar o corregir el valor en un diccionario, (Se sobreescribe el diccionario)
midiccionario['Italia']= 'Roma'
print(midiccionario)

#Eliminar un elemento de un Diccionario
del midiccionario['Reino Unido']
print(midiccionario)

#Diccionario con Clave y valor de distintas clases
midiccionario = {'Alemania':'Berlin', 23:'Jordan','Mosqueteros':3}
print(midiccionario)

#Utilizando la tupla como clave en un diccionario
mitupla=('España','Francia','Reino unido','Alemania')
midiccionario={mitupla[0]:'Madrid', mitupla[1]:'Paris', mitupla[2]:'Londres', mitupla[3]:'Berlin'}
print(midiccionario['Francia'])

#una tupla como valor dentro de un diccionario
midiccionario={23:'Jordan','Nombre':'Michael', 'Equipo': 'Chicago', 'Anillos':(1991,1992,1993,1996,1997,1998)}
print(midiccionario['Equipo'])
print(midiccionario['Anillos'])

#Un diccionario con tupla dentro de otro diccionario
midiccionario={23:'Jordan','Nombre':'Michael', 'Equipo': 'Chicago', 'Anillos':{'Temporadas':(1991,1992,1993,1996,1997,1998)}}
print(midiccionario)

#print de las claves (keys)
print(midiccionario.keys())

#print de valores (values)
print(midiccionario.values())

#Imprimer la longitud del diccionario
print(len(midiccionario))

