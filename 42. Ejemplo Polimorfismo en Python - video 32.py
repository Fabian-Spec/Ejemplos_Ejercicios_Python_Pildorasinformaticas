# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 10:34:22 2021

@author: JARBY II
"""

class Coche():
    def desplazamiento(self):
        print('Me desplazo utilizando cuatro ruedas')


class Moto():
    def desplazamiento(self):
        print('Me desplazo utilizando dos ruedas')
        
        
class Camion():
    def desplazamiento(self):
        print('Me desplazo utilizando seis ruedas')
        

def desplazamientoVehiculo(vehiculo):
    vehiculo.desplazamiento()
    
miVehiculo=Moto()

desplazamientoVehiculo(miVehiculo)
