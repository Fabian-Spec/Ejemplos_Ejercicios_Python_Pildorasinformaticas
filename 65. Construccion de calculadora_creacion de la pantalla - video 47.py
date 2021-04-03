
from tkinter import *


raiz=Tk()#Creacion de la Raiz

miFrame=Frame(raiz) #Creacion del Frame

miFrame.pack()#Empaquetado del Frame

pantalla=Entry(miFrame)# Creacion del cuadro de texto de las operaciones
pantalla.grid(row=1,column=1, padx=10, pady=10)#Cubicacion del cadro de texto dentro de la cuadricula, la cuadricula ya esta creada unicamente se ban agregando elementos a la misma
pantalla.config(background='Black', fg='#03f943', justify='right')


raiz.mainloop()

