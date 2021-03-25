
from tkinter import *

root=Tk()
miFrame=Frame(root, width=1200, height=600)
miFrame.pack()

cuadroTexto=Entry(miFrame)
cuadroTexto.place(x=100, y=100)

nombreLabel=Label(miFrame, text='Nombre:')
nombreLabel.place(x=100, y=100)

root.mainloop()