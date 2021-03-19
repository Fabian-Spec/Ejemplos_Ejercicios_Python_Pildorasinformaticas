# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 12:32:19 2021

@author: JARBY II
"""

def multiplica(num1, num2):
    return num1*num2


def divide(num1, num2):
    try:
        return num1/num2
    except ZeroDivisionError:
        print('No se puede dividir entre 0')
        return('operación erronea')
        
while True:
    try:
        numero_1 =(int(input('Introduce el primer número: ')))
        numero_2 =(int(input('Introduce el segundo número: '))) 
        break
    except ValueError:
        print('Los valores introducidos no son correctos intentalo de nuevo ')

operacion = input('Introduce la operación a realizar (multiplica, divide): ')

if operacion=='multiplica':
    print(multiplica(numero_1,numero_2))
    
elif operacion=='divide':
    print(divide(numero_1, numero_2))
    
else:
    print('Operación no contemplada')
    
print('Operación ejecutada, el programa sigue con la ejecución de mas codigo')


