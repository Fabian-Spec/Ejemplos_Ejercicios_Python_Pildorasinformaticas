# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 16:54:14 2021

@author: JARBY II
"""

from io import open 

archivo_texto=open('archivo.txt','w')

frase='Estupendo dia para estudiar Python \n el miercoles'

archivo_texto.write(frase)

archivo_texto.close()

