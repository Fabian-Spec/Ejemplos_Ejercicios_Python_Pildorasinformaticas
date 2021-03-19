# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 11:05:30 2021

@author: JARBY II
"""

import pickle

lista_nombres=['Pedro', 'Ana', 'Maria', 'Isable']

fichero_binario=open('lista_nombres', 'wb')

pickle.dump(lista_nombres, fichero_binario)

fichero_binario.close()

del (fichero_binario)



