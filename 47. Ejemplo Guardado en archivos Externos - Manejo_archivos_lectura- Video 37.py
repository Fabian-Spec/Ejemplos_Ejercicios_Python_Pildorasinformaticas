# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 11:05:30 2021

@author: JARBY II
"""

from io import open 

archivo_texto=open('archivo.txt','r')

texto=archivo_texto.read()

archivo_texto.close()

print(texto)

