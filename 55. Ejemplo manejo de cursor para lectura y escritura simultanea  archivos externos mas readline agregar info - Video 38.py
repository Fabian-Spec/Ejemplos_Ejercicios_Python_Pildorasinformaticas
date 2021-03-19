# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 11:05:30 2021

@author: JARBY II
"""

from io import open 

archivo_texto=open('archivo.txt','r+') #lectura y escritura simultanea r+

#print(archivo_texto.readlines())

lista_texto=archivo_texto.readlines();

lista_texto[1]='Esta linea ha sido incluida desde el exterior \n'

archivo_texto.seek(0)

archivo_texto.writelines(lista_texto)

archivo_texto.close()


