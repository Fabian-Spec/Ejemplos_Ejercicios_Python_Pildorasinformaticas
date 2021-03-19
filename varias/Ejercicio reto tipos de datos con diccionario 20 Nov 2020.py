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
    comprobar = historia_credito == 1
    if (comprobar == True):
        if ((i_c > 0 ) and (i_d/9 > c_p)):
            return{'id_prestamo': id_prestamo, 'aprobado': 'Verdadero'}
        else:
            if ((dependientes >2) and (independiente == 'Si')):
                return{'id_prestamo': id_prestamo, 'aprobado': i_c/12>c_p }
            else:
                return{'id_prestamo': id_prestamo, 'aprobado': c_p<200 }
  
                      
  #Historia de Cretido falso
    else:
        # Independiente verdadero
        if (independiente == 'Si' ):
            # (No Casado No dependiente) verdadero
            if ( (casado == 'No')and(dependientes >1)):
                # (No Casado No dependiente) verdadero, verdadero
                if ((i_d > c_p )or(i_c/10>c_p)):
                    return{'id_prestamo': id_prestamo, 'aprobado': cp<180}
                # (No Casado No dependiente) verdadero, falso
                else:
                    return{'id_prestamo': id_prestamo, 'aprobado': 'Falso'}
            # (No Casado No dependiente) falso
            else:
                return{'id_prestamo': id_prestamo, 'aprobado': 'Falso'}

       
        # Independiente Falso
        else:
            #(No semiurbano y dependientes no es menor que 2) verdadero  
            if ((tipo_propiedad != 'semiurbano')and(dependientes>2)):
                #(No semiurbano y dependientes no es menor que 2) graduado verdadero           
                if (educacion == 'Graduado'):
                    return {'id_prestamo': id_prestamo, 'aprobado': (i_d/11>c_p)and(i_c/11>c_p)}
                #(No semiurbano y dependientes no es menor que 2) graduado falso
                else:
                    return {'id_prestamo': id_prestamo, 'aprobado': 'Falso'}
            else:
                return {'id_prestamo': id_prestamo, 'aprobado': 'Falso'}


#return{'id_prestamo': id_prestamo, 'aprobado': 'Nelkahel' }




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
    'id_prestamo': 'RETOS2_002',
    'casado': 'Si',
    'dependientes': 5,
    'educacion': 'No Graduado',
    'independiente': 'No',
    'ingreso_deudor': 1830,
    'ingreso_codeudor': 0,
    'cantidad_prestamo': 100,
    'plazo_prestamo': 360,
    'historia_credito': 0,
    'tipo_propiedad': 'Urbano',
    }

print(prestamo(diccionario))
