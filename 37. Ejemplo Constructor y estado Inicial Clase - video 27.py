# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 11:25:10 2021

@author: JARBY II
"""

class Coche():
    
    def __init__(self):
        
        self.largoChasis=250
        self.anchoChasis=120
        self.ruedas=4
        self.enmarcha=False
    
    def arrancar(self,arrancamos):
        self.enmarcha=arrancamos
        
        if(self.enmarcha):
            return 'El Coche esta en marcha'        
        else:
            return 'El Coche esta parado'
    
    def estado(self):        
        print('El coche tiene', self.ruedas, 'ruedas. Un ancho de ', self.anchoChasis, ' y un largo de ', self.largoChasis)  


miCoche = Coche()

print (miCoche.arrancar(True))
miCoche.estado()


print('------------------A continuación creamos el segundo Objeto ----------------')

miCoche2 = Coche()

print(miCoche2.arrancar(False))
miCoche.estado()