# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 16:27:46 2020

@author: JARBY II
"""

"""
* Necesitamos calcular un promedio
* Son 5 notas
* De las 5 notas se elimina la peor y se calcula el promedio
* las notas se encuentran en una escala de 0 a 100
* debo convertir las notas de la escala de 0 a 5
- Hacer función que recibe un codigo alfanumerico
  y 5 notas en números
- "El promedio ajustado del estudiante(codigo es) es (promedio)"
- debo retornar una cadena de carácteres

"""
    

codigoestudiante = str(input("introduzca el el codigo del estudiante: "))
nota1 = int(input("introduzca el valor de la nota1: "))
nota2 = int(input("introduzca el valor de la nota2: "))
nota3 = int(input("introduzca el valor de la nota3: "))
nota4 = int(input("introduzca el valor de la nota4: "))
nota5 = int(input("introduzca el valor de la nota5: "))

def nota_quices(codigoestudiante, nota1, nota2, nota3, nota4, nota5):
    nota_bajita = min(nota1, nota2, nota3, nota4, nota5)
    promedio = (((nota1 + nota2 + nota3 + nota4 + nota5 - nota_bajita)/4)*0.005)
    return promedio

print(nota_quices("codigoesdutiante", nota1, nota2, nota3, nota4, nota5))

