# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 18:36:30 2020

@author: JARBY II
"""

#Ejemplo de Bucle utilizando una variable que aumente 

contador=0
miEmail=input("Escribe tu Email: ")


for i in miEmail:
    if ( i=='@' or i=="."):
        contador=contador+1

if contador==2:
    print('El email es correcto')
else:
    print('El email no es correcto')
    
    



