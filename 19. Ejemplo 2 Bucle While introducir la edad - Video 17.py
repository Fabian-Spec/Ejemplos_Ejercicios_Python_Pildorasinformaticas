# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 10:04:29 2020

@author: JARBY II
"""

edad=int(input('Introduce tu edad por favor: '))
while edad<5 or edad > 130:
    print('Has introducido una edad incorrecta. vuelve a intentarlo')
    edad=int(input('Introduce tu edad por favor: '))
    
print('Gracias por colaborar. Puedes pasar')
print('Edad del aspirante: ' + str(edad))