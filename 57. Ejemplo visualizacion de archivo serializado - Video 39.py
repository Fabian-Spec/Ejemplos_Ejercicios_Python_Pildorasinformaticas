# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 11:05:30 2021

@author: JARBY II
"""



import pickle

fichero=open('lista_nombres', 'rb')

lista=pickle.load(fichero)

print(lista)