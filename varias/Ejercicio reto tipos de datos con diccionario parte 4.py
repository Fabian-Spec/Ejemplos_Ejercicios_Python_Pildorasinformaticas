# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 15:57:40 2020

@author: JARBY II
"""

"""
Tipos de documentos vistos en Python hasta ahora:
int: numero entero
float: numero con decimales
str: cadena de caracteres (números y letras)
dict: directorio (estructura de distintas clases de datos ejem: número enteros caracteres etc, etc)

"""


def prestamo(informacion: dict) -> dict:
    id_prestamo = informacion['id_prestamo']
    casado = informacion['casado']
    dependiente = informacion['dependiente']
    educacion = informacion['educacion']
    independiente = informacion['independiente']
    i_d = informacion['ingreso_deudor']         
    i_c = informacion['ingreso_codeudor']
    c_p = informacion['cantidad_prestamo']
    p_p = informacion['plazo_prestamo']
    historia_credito = informacion['historia_credito']
    tipo_propiedad = informacion['tipo_propiedad']


    #Casado Si
    comprobar = casado == 'Si'
    if (comprobar == True):
        return{'id_prestamo': id_prestamo, 'aprobado': True}
    # cuando casado = No
    else:
        # dependiente0,1
        if (dependiente == 0 or dependiente == 1):
            return {'id_prestamo': id_prestamo, 'aprobado': False}    
        # depenndiente 2, '3+'
        elif( dependiente == 2 or dependiente == '3+'):
            comprobar = i_c / 5 < i_d
            return {'id_prestamo': id_prestamo, 'aprobado': comprobar}
        
    



diccionario = {
    'id_prestamo': 'Ah54654',
    'casado': 'Si',
    'dependiente': 1,
    'educacion': 'Graduado',
    'independiente': 'No',
    'ingreso_deudor': 45612.5,
    'ingreso_codeudor': 459689.,
    'cantidad_prestamo': 4808880,
    'plazo_prestamo': 5,
    'historia_credito': 1,
    'tipo_propiedad': 'Rural'
    }

print(prestamo(diccionario))
