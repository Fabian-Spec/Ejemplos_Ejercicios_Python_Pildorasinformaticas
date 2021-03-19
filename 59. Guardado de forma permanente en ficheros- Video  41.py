# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 16:13:34 2021

@author: JARBY II
"""
#para crear el fichero externo con codigo binario se importa la libreria libreria 
#o biblioteca pickle

import pickle

#se crea la clase persona con sus respectivos atributos o caracteristicas. tambien se utiliza
#el metodo constructor  __init__ para que los atributos queden con constructor y estos se puedan invocar
#de acuerdo a como se necesiten
class Persona:
    def __init__(self, nombre, genero, edad):
        self.nombre=nombre
        self.genero=genero
        self.edad=edad
        print('Se ha creado una persona nueva con el nombre de: ', self.nombre)
        
    #Se usa este metodo __str__(self):, para definir mediante '{}'.format(self.) como 
    #quiero que la información del objeto que se crea en esta clase, se vea y se retorne    
    def __str__(self):
        return '{} {} {}'.format(self.nombre, self.genero, self.edad)
    
#se crea la siguiente clase la cual crea: 
class ListaPersonas:

#1° una variable de lista para ir armando la lista con los nombres que se vayan cargando    
    personas=[]

#2° crear un archivo extraible (fichero extraible) en codigo binario, que contiene la lista personas
    def __init__(self):
        listaDePersonas=open('ficheroExterno','ab+')
        
#3° adicionalmente se agrega la instruccion .seek(0) para que el puntero del archivo o 
#fichero externo se ubique al inicio del archivo cada vez que se ejecuta el mismo               
        listaDePersonas.seek(0)
        
#4° funcion try, la cual trata de cargar la información guardada en el fichero externo
# de formma binaria, la información agregada a la lista de la variable de la función
# personas=[], he imprime el numero de personas que se cargaron en el fichero externo

        try:
            self.personas=pickle.load(listaDePersonas)
            print('Se cargaron {} personas del fichero externo'.format(len(self.personas)))


#5° se crea un except para indicar que el fichero esta vacio cuando efectivamente no 
#aya informacion adicionada en la lista            
        except:
            print('El fichero está vacio')

#6° Se crea esta funcion de finally, para cerrar el archivo y borrar los datos de la lista cargados
#temporalmente al cargarlos en el listado
        finally:
            listaDePersonas.close()
            del(listaDePersonas)
       
        
#7° Se crea la siguiente función para que se agregue informacion a la lista personas al 
#pasar informacion a travez de self,p y a suvez se enlaza con la siguiente función
#guardarPErsonasEnFichero para que esta efectivamente guarde de forma binaria la 
#información de la lista personas.
  
    def agregarPersonas(self,P):
        self.personas.append(P)
        self.guardarPersonasEnFicheroExterno()
        
#8° la siguiente función es activada por la anterior, y se encarga de abrir el archivo 
#binario y guardar la lista de personas con los ultimos datos adicionados
#finalmente cierra el archivo, y limpia los datos temporales de la lista en
#el programa          
    def guardarPersonasEnFicheroExterno(self):
        listaDePersonas=open('ficheroExterno','wb')
        pickle.dump(self.personas, listaDePersonas)
        listaDePersonas.close()
        del(listaDePersonas)

#9° la siguiente función se crea para poder imprimir el listado con todos los nombres
#agregados al mismo, se hace mediante un bluque for el cual mediante la variable p
#imprime cada uno de los elementos de la lista 


    def mostrarInfoFicheroExterno(self):
        print('La información del fichero externo es la siguiente: ')
        for p in self.personas:
            print(p)
       

#------------ingreso de información al programa y uso de los modulos del mismo---------


#se crea la sivariable miLista para poder usar la clase ListaPersonas de forma mas fluida
miLista=ListaPersonas()


#se crea la variable persona igualmente para usar la clase Persona de forma mas fluida
persona=Persona('Fabian','Masculino',35)


#se invoca la función agregar personas de la clase ListaPersonas, y se le pasa la 
#variable persona, la cual contiene la información de la persona que vamos creando
miLista.agregarPersonas(persona)


#Se invoca la función o el modulo mostrarInfoFicheroExterno() para visualizar mediante
#la impresión los datos de las peronas que hemo ido agregando en el archvivo binario 
#externo
miLista.mostrarInfoFicheroExterno()






