# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 11:25:10 2021

@author: JARBY II
"""

class Coche():
    
    def __init__(self):
        
        self.__largoChasis=250
        self.__anchoChasis=120
        self.__ruedas=4
        self.__enmarcha=False
    
    def arrancar(self,arrancamos):
        self.__enmarcha=arrancamos
        
        if(self.__enmarcha):
            return 'El Coche esta en marcha'        
        else:
            return 'El Coche esta parado'
    
    def estado(self):        
        print('El coche tiene', self.__ruedas, 'ruedas. Un ancho de ', self.__anchoChasis, ' y un largo de ', self.__largoChasis)  


miCoche = Coche()

print (miCoche.arrancar(True))
miCoche.estado()


print('------------------A continuación creamos el segundo Objeto ----------------')

miCoche2 = Coche()

#En la siguiente linea de codigo se intenta modificar la propiedad de chasis utilizando los __ pero no funciona porque ya esta encapsulada y no se puede modificar desde fuera de la clase
miCoche.__largoChasis = 6

print(miCoche2.arrancar(False))
miCoche.estado()






