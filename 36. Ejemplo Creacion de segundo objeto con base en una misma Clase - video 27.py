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
    
    def arrancar(self,arrancamos):
        self.enmarcha=arrancamos
        
        if(self.enmarcha):
            return 'El Carro esta en marcha'        
        else:
            return 'El Carro esta parado'
    
    def estado(self):        
        print('El coche tiene', self.ruedas, 'ruedas. Un ancho de ', self.anchoChasis, ' y un largo de ', self.largoChasis)  


miCarro = Carros()

print (miCarro.arrancar(True))
miCarro.estado()


print('------------------A continuación creamos el segundo Objeto ----------------')

miCarro2 = Carros()

print(miCarro2.arrancar(False))
miCarro2.estado()