# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:05:46 2021

@author: JARBY II
"""

class vehiculos():
    def __init__(self, marca, modelo):
        
        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False
        
    def arrancar(self):
        self.enmarcha=True
    
    def acelerar(self):
        self.acelera=True
        
    def frenar(self):
        self.frena=True
        
    def estado(self):
        print('Marca: ', self.marca, '\nModelo: ', self.modelo, '\nEn marcha: ', self.enmarcha,
              "\nAcelerando: ", self.acelera, "\nFrenado: ", self.frena)

class Moto(vehiculos):
    pass

miMoto=Moto("Honda","CBR")
            
miMoto.estado()
