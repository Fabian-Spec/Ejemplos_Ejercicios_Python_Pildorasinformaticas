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
    id_prestamo = informacion.get('id_prestamo')
    print(id_prestamo)
    casado = informacion.get('casado')
    print(casado)
    dependientes = informacion.get('dependientes')
    print(dependientes)
    educacion = informacion.get('educacion')
    print(educacion)
    independiente = informacion.get('independiente')
    print(independiente)
    ingreso_deudor = informacion.get('ingreso_deudor')         
    print(ingreso_deudor)
    ingreso_codeudor = informacion.get('ingreso_codeudor')
    print(ingreso_codeudor)
    cantidad_prestamo = informacion.get('cantidad_prestamo')
    print(cantidad_prestamo) 
    historia_credito = informacion.get('historia_credito')
    print(historia_credito)
    tipo_propiedad = informacion.get('tipo_propiedad') 
    print(tipo_propiedad)
    
    
diccionario = {
    'id_prestamo': 'Ah54654',
    'casado': 'Si',
    'dependientes': 1,
    'educacion': 'Graduado',
    'independiente': 'No',
    'ingreso_deudor': 45612.5,
    'ingreso_codeudor': 459689.,
    'cantidad_prestamo': 4808880,
    'plazo_prestamo': 5,
    'historia_credito': 1,
    'ipo_propiedad': 'Rural'
    }

prestamo(diccionario)