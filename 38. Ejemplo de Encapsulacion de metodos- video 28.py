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
            chequeo=self.__chequeo_interno()
        
        if(self.__enmarcha and chequeo):
            return 'El Coche esta en marcha'  
        
        elif(self.__enmarcha and chequeo == False):
            return 'El chequeo identifico problemas para arrancar, no se puede arrancar'
        
        else:
            return 'El Coche esta parado'
    
    def estado(self):        
        print('El coche tiene', self.__ruedas, 'ruedas. Un ancho de ', self.__anchoChasis, ' y un largo de ', self.__largoChasis)  


    def __chequeo_interno(self):
        print('Realizando el chequeo interno')
        self.gasolina='Ok'
        self.aceite='Ok'
        self.puertas='Ok'
        
        if(self.gasolina=='Ok' and self.aceite =='Ok' and self.aceite=='Ok' and self.puertas=='Ok'):
            return True
        
        else:
            return False
        

miCoche = Coche()

print (miCoche.arrancar(True))

miCoche.estado()


print('------------------A continuación creamos el segundo Objeto ----------------')

miCoche2 = Coche()

print(miCoche2.arrancar(False))

miCoche.estado()








