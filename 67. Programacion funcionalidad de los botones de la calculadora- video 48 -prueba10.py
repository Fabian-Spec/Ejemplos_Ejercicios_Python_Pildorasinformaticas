
from tkinter import *


raiz=Tk()#Creacion de la Raiz

miFrame=Frame(raiz) #Creacion del Framew

miFrame.pack()#Empaquetado del Frame

#---------------------------------------------Pantalla------------------------------------------



numeroPantalla=StringVar()

pantalla=Entry(miFrame, textvariable=numeroPantalla)# Creacion del cuadro de texto de las operaciones
pantalla.grid(row=1,column=1, padx=10, pady=10, columnspan=4)#Cubicacion del cadro de texto dentro de la cuadricula, la cuadricula ya esta creada unicamente se ban agregando elementos a la misma
pantalla.config(background='Black', fg='#03f943', justify='right')
pantalla.insert(0,'0')

#--------------------------------------LISTAS DE HISTORICOS --------------------------------------

listaHistoricoTransacciones = [0]
listaNumeros = [0]


#--------------------------------------PULSACIONES DE TECLADO ----------------------------------------------------

#----------------------------Operaciones de pulsaciones de teclado Iniciales--------------------


def numeroPulsado(num):
    if len(listaHistoricoTransacciones) < 2:
        if numeroPantalla.get() == '0':
            numeroPantalla.set(num)
            #listaHistoricoTransacciones.append(numeroPantalla.get())
            print('listaHistoricoTransacciones:', listaHistoricoTransacciones)
        
        else:
            numeroPantalla.set(numeroPantalla.get() + num)
            #numeroPantalla.set(num)



#--------------------------------OPeraciones Pulsaciones de teclado Posteriores-----------------------


    else:
        pantalla.delete(0,END)
        if len(listaNumeros) < 2:
            listaNumeros.append(num)
            numeroPantalla.set(num)
            print('lista de numeros: ',listaNumeros)
        
        else:
            listaNumeros.append(num)
            print('lista de numeros mayor nuevo numero', listaNumeros)
            concaNumeros = (''.join([str(n) for n in listaNumeros[-2:]]))
            listaNumeros.append(concaNumeros)
            numeroPantalla.set(listaNumeros[-1])
            print('lista de numeros mayor a 9', listaNumeros)


            #numeroPantalla.set(num)



#----------------------------------------------FUNCION SUMA ----------------------------------------------------------------------



#-------------------------------------------Funcion suma Inicial----------------------------------------------

def suma():
    if len(listaHistoricoTransacciones) < 2:
        try:
            listaHistoricoTransacciones.append(numeroPantalla.get())
            pantalla.delete(0,END)
            #print(listHistoricoTransacciones)
            print('Suma historico de transacciones: ',int(listaHistoricoTransacciones[-1]) + int(listaHistoricoTransacciones[-2]))
            listaHistoricoTransacciones.append(int(listaHistoricoTransacciones[-1]) + int(listaHistoricoTransacciones[-2]))
            print('listaHistorico de transacciones: ',listaHistoricoTransacciones)
            numeroPantalla.set(int(listaHistoricoTransacciones[-1]))
        except ValueError:
            print(int(0))

#--------------------------------------Funcion Suma posterior ----------------------------------------------

    else:
        if len(listaNumeros) <2:
            del listaHistoricoTransacciones[1:]
        try:
            listaHistoricoTransacciones.append(listaNumeros[-1])
            pantalla.delete(0,END)
            #print(listHistoricoTransacciones)
            print(int(listaHistoricoTransacciones[-1]) + int(listaHistoricoTransacciones[-2]))
            listaHistoricoTransacciones.append(int(listaHistoricoTransacciones[-1]) + int(listaHistoricoTransacciones[-2]))
            print('resultadoHistoricodeTransacciones: ',listaHistoricoTransacciones)
            numeroPantalla.set(int(listaHistoricoTransacciones[-1]))
            del listaNumeros [1:]
            print('listanumeros: ', listaNumeros)
        except ValueError:
            print(int(0))



#-------------------------------------------FUNCIÓN DE RESTA ---------------------------------------
#----------------------------------------Funcion resta Inicial----------------------------------------------

def resta():
    if len(listaHistoricoTransacciones) < 2:
        try:
            listaHistoricoTransacciones.append(numeroPantalla.get())
            pantalla.delete(0,END)
            #print('resta historico de transacciones: ',int(listaHistoricoTransacciones[-2]) - int(listaHistoricoTransacciones[-1]))
            #listaHistoricoTransacciones.append(int(listaHistoricoTransacciones[-2]) - int(listaHistoricoTransacciones[-1]))
            print('listaHistorico de transacciones: ',listaHistoricoTransacciones)
            numeroPantalla.set(int(listaHistoricoTransacciones[-1]))
        except ValueError:
            print(int(0))

#--------------------------------------Funcion resta posterior ----------------------------------------------

    else:
        if len(listaNumeros) <2:
            del listaHistoricoTransacciones[1:]
        try:
            listaHistoricoTransacciones.append(listaNumeros[-1])
            pantalla.delete(0,END)
            print(int(listaHistoricoTransacciones[-2]) - int(listaHistoricoTransacciones[-1]))
            listaHistoricoTransacciones.append(int(listaHistoricoTransacciones[-2]) - int(listaHistoricoTransacciones[-1]))
            print('resultadoHistoricodeTransacciones: ',listaHistoricoTransacciones)
            numeroPantalla.set(int(listaHistoricoTransacciones[-1]))
            del listaNumeros [1:]
            print('listanumeros: ', listaNumeros)
        except ValueError:
            print(int(0))







#---------------------------Creación de los Botones Fila 1------------------------------------------

                                 #Ancho del Boton =3             
Boton7=Button(miFrame, text='7', width=3, command=lambda:numeroPulsado('7'))
Boton7.grid(row=2, column=1)
Boton8=Button(miFrame, text='8', width=3, command=lambda:numeroPulsado('8'))
Boton8.grid(row=2, column=2)
Boton9=Button(miFrame, text='9', width=3, command=lambda:numeroPulsado('9'))
Boton9.grid(row=2, column=3)
BotonDividir=Button(miFrame, text='/', width=3,)
BotonDividir.grid(row=2, column=4)


#---------------------------Creación de los Botones Fila 2------------------------------------------

                                 #Ancho del Boton =3             
Boton4=Button(miFrame, text='4', width=3, command=lambda:numeroPulsado('4'))
Boton4.grid(row=3, column=1)
Boton5=Button(miFrame, text='5', width=3, command=lambda:numeroPulsado('5'))
Boton5.grid(row=3, column=2)
Boton6=Button(miFrame, text='6', width=3, command=lambda:numeroPulsado('6'))
Boton6.grid(row=3, column=3)
BotonDividir=Button(miFrame, text='*', width=3)
BotonDividir.grid(row=3, column=4)

#---------------------------Creación de los Botones Fila 3------------------------------------------

                                 #Ancho del Boton =3             
Boton1=Button(miFrame, text='1', width=3, command=lambda:numeroPulsado('1'))
Boton1.grid(row=4, column=1)
Boton2=Button(miFrame, text='2', width=3, command=lambda:numeroPulsado('2'))
Boton2.grid(row=4, column=2)
Boton3=Button(miFrame, text='3', width=3, command=lambda:numeroPulsado('3'))
Boton3.grid(row=4, column=3)
BotonRestar=Button(miFrame, text='-', width=3, command=lambda:resta())
BotonRestar.grid(row=4, column=4)

#---------------------------Creación de los Botones Fila 4------------------------------------------

                                 #Ancho del Boton =3             
Boton0=Button(miFrame, text='0', width=3, command=lambda:numeroPulsado('0'))
Boton0.grid(row=5, column=1)
BotonComa=Button(miFrame, text=',', width=3)
BotonComa.grid(row=5, column=2)
BotonIgual=Button(miFrame, text='=', width=3)
BotonIgual.grid(row=5, column=3)
BotonSumar=Button(miFrame, text='+', width=3, command=lambda:suma() )
BotonSumar.grid(row=5, column=4)




raiz.mainloop()

