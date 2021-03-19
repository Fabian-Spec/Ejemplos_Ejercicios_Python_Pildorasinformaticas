# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 15:50:05 2020

@author: JARBY II
"""

#Uso de Range y de la función print(f'texto {variable}')
for i in range(5):
    print(f"valor de la variable {i}")


#Uso de Range y de la función print(f'texto {variable}'), dentro de un rango de la lista del range
for i in range (5,50,3):
     print(f"valor de la variable {i}")
     
#Uso de el Lend para que el range haga una lista con base en el numero de elementos que identifica el lend

valido =False
email=input('Introduce tu email: ')

for i in range(len(email)):
    if email[i]=='@':
        valido=True

if valido:
    print('El email es correcto')
    
else:
    print('El email es incorrecto')

