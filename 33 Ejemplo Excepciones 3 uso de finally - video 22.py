# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 12:32:19 2021

@author: JARBY II
"""

#Uso de finally numero 1
def divide ():
    try:
        op1=(int(input('introduce el primer número: ')))
        op2=(int(input('introduce el segundo número: ')))    
        print('La division es: '+ str(op1/op2))
    except ValueError:
        print('El valor introducido es Erroneo')
    except ZeroDivisionError:
        print('No se puede dividir entre 0') 

    finally:
        print('calculo finalizado')

divide()


#Uso finally numero 2

def divide ():
    try:
        op1=(int(input('introduce el primer número: ')))
        op2=(int(input('introduce el segundo número: ')))    
        print('La division es: '+ str(op1/op2))


    finally:
        print('calculo finalizado')

divide()