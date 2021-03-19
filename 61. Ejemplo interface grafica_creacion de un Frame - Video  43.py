from tkinter import *

#Configuracion de la Raiz
raiz =Tk()
raiz.title('Trading Things')
raiz.resizable(1,1)
raiz.iconbitmap("logo_tgs.ico")
raiz.geometry('650x350')
raiz.config(bg='#7e1e8f')  #Con el # se coloca el codigo del color
raiz.config(cursor='hand2')

#Configuracion del Frame "Cuadro u objeto dentro de la raiz"
miFrame=Frame()
miFrame.pack( side='right', anchor='n')
miFrame.config(width='650', height='350')
miFrame.config(bg='#f7b80f')
miFrame.config(bd=13)
miFrame.config(relief='flat')
miFrame.config(cursor='arrow')
raiz.mainloop()