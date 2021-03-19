# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 16:17:59 2020

@author: JARBY II
"""

"""
Ejercicio de udo de if y else:
- EL uruario debe ingresar el número de horas trbajds
  y el valor de cada hora
- Sobre el total va a haber un descuento del 8% por seguridad social
- Vamos a recibir un 2% si la multiplicación de las horas trabajadas y el valor por horas    
  es menor  medio salario minimo $877,803
"""



def calcular_sueldo(n_horas_trabajadas, valor_hora):
    if (n_horas_trabajadas <= 0 or valor_hora <= 0 ):
        return ("Introduzca numeros correctos")
    
    sueldo_total = n_horas_trabajadas * valor_hora
    sueldo_menos_seguridad_social = sueldo_total * 0.92
    
    if (sueldo_total < (877803/2)):
        aumento = sueldo_total * 0.02
        sueldo_menos_seguridad_social = sueldo_menos_seguridad_social + aumento
        return "Susueldo es de: ", sueldo_menos_seguridad_social

# Else se refiere a lo que pasa si el suldo no cumple el if    
    
    else:
        return "Su sueldo es de: ", sueldo_menos_seguridad_social


n_horas_trabajadas = int(input("Ingrese número de horas trabajadas: ")) 
valor_hora = int(input("Ingrese el valor por hora: ")) 
     
print(calcular_sueldo(n_horas_trabajadas, valor_hora))


    
     

    
    
    