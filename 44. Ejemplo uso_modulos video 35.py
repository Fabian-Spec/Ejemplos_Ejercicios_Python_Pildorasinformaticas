# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 16:16:21 2021

@author: JARBY II
"""

#Uso general para invocar el paquete y los modulos, (forma Extensa)

from paquete_calculos.calculos_generales import dividir

dividir(4,6)


from paquete_calculos.calculos_generales import potencia

potencia(4,6)


#Uso abreviado para invocar el paquete y los modulos, (forma corta pero menos eficiente cuando 
#los modulos tienen mucho codigo)


from paquete_calculos.calculos_generales import *

redondear(4.6)