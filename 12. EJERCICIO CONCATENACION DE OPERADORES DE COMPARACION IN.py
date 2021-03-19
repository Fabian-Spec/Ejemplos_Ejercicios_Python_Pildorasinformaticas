# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 17:04:31 2020

@author: JARBY II
"""


print('Asignaturasoptativas Año 2020')

print('Asignaturas optativas: Informática gráfica - Pruebas de software - Usabilidad y accesibilidad')

opcion = input('Escribe la asignatura escogida: ')

asignatura = opcion.lower()

if asignatura in ('informática gráfica', 'pruebas de software', 'usabilidad y accesibilidad'):
   print('la asignatura elegida es: ' + asignatura)
else:
    print('la asignatura escogida no esta contemplada')
 


#Otra forma de Usar el Lower mas abreviada    
print('Asignaturasoptativas Año 2020')

print('Asignaturas optativas: Informática gráfica - Pruebas de software - Usabilidad y accesibilidad')

asignatura = (input('Escribe la asignatura escogida: ')).lower()


if asignatura in ('informática gráfica', 'pruebas de software', 'usabilidad y accesibilidad'):
   print('la asignatura elegida es: ' + asignatura)
else:
    print('la asignatura escogida no esta contemplada')