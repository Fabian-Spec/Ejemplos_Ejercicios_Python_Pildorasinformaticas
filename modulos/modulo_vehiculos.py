# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 15:10:20 2021

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

class Furgoneta(vehiculos):
    def carga(self,cargar):
        self.cargado=cargar
        if(self.cargado):
            return 'La furgoneta esta cargada'
        else:
            return 'La furgoneta no está cargada'
            
class Moto(vehiculos):
    hcaballito=""
    def caballito(self):
        self.hcaballito='Voy haciendo el caballito'
        
    def estado(self):
        print('Marca: ', self.marca, '\nModelo: ', self.modelo, '\nEn marcha: ', self.enmarcha,
              "\nAcelerando: ", self.acelera, "\nFrenado: ", self.frena, '\nhcaballito', self.hcaballito)


class VElectricos(vehiculos):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
        self.autonomia=100
    def cargaEnergia(self):
        self.cargando=True



