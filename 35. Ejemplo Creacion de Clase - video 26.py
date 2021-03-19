# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 11:25:10 2021

@author: JARBY II
"""

class Carros():
    largoChasis=250
    anchoChasis=120
    ruedas=4
    enmarcha=False
    
    def arrancar(self):
        self.enmarcha=True
    
    def estadoDeMiCarro(self):
        if(self.enmarcha):
            return 'El carro esta en marcha'
        else:
            return 'El coche esta parado'
        
        
        

miCarro = Carros()

print('El Largo del Carro es de: ' + str( miCarro.largoChasis))
print('Carro tiene el siguiente numero de ruedas: ' + str(miCarro.ruedas))
miCarro.arrancar()

print(miCarro.estadoDeMiCarro())
