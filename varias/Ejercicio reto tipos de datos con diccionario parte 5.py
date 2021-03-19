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
    dependientes = informacion['dependientes']
    educacion = informacion['educacion']
    independiente = informacion['independiente']
    i_d = informacion['ingreso_deudor']         
    i_c = informacion['ingreso_codeudor']
    c_p = informacion['cantidad_prestamo']
    p_p = informacion['plazo_prestamo']
    historia_credito = informacion['historia_credito']
    tipo_propiedad = informacion['tipo_propiedad']


  #Historia de Cretido verdadero
    comprobar = historia_credito == 0
    if (comprobar == True):
        return{'id_prestamo': id_prestamo, 'aprobado': True}
  #Historia de Cretido falso
    else:
        # dependiente0,1
        if (dependientes == 0 or dependientes == 1):
            return {'id_prestamo': id_prestamo, 'aprobado': False}    
        # depenndiente 2, '3+'
        elif( dependientes == 2 or dependientes == '3+'):
            comprobar = i_c / 5 < i_d
            return {'id_prestamo': id_prestamo, 'aprobado': comprobar}







"""
    #Historia de Cretido verdadero
    comprobar = historia_credito = 0:
    if (comprobar == True):
        comprobar = i_c > 0 ^ i_d / 9 > c_p
        if (comprobar == True):
            #Historia de credito, verdadero, verdadero
            return {'id_prestamo': id_prestamo, 'aprobado': comprobar}
            #Histoira de credito, verdadero, falso
            elif (comprobar == dependientes >2 ^ independiente):
                #Histoira de credito, verdadero, falso, verdadero
                comprobar = i_c / 12 > c_p
                return {'id_prestamo': id_prestamo, 'aprobado': comprobar}
            else:
                return {'id_prestamo': id_prestamo, 'aprobado': c_p < 200}
    else:
                
"""            
        

diccionario = {
    'id_prestamo': 'Ah54654',
    'casado': 'No',
    'dependientes': 1,
    'educacion': 'Graduado',
    'independiente': 'No',
    'ingreso_deudor': 45612.5,
    'ingreso_codeudor': 459689.,
    'cantidad_prestamo': 4808880,
    'plazo_prestamo': 5,
    'historia_credito': 0,
    'tipo_propiedad': 'Rural'
    }

print(prestamo(diccionario))
