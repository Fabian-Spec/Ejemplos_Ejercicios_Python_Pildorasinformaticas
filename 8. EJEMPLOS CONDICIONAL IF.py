# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 09:34:17 2020

@author: JARBY II
"""

print ('Programa de evaluación de notas de alumnos')


nota_alumno=input('Introduce la nota del Alumno: ')


def evaluacion (nota):
    valoracion='aprobado'
    if nota<5:
        valoracion='suspenso'
    return valoracion

print(evaluacion(int(nota_alumno)))
    