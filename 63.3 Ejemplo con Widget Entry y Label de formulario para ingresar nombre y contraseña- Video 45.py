
from tkinter import *

root=Tk()
miFrame=Frame(root, width=1200, height=600)
miFrame.pack()

cuadroNombre=Entry(miFrame)
cuadroNombre.grid(row=0, column=1, padx=10, pady=10)
cuadroNombre.config(fg='blue',justify='center')

cuadroPass=Entry(miFrame)
cuadroPass.grid(row=1, column=1, padx=10, pady=10)
cuadroPass.config(show='*')

cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=2, column=1, padx=10, pady=10)
cuadroApellido.config(fg='blue',justify='center')

cuadroDireccion=Entry(miFrame)
cuadroDireccion.grid(row=3, column=1, padx=10, pady=10)
cuadroDireccion.config(fg='blue',justify='center')

nombreLabel=Label(miFrame, text='Nombre:')
nombreLabel.grid(row=0, column=0, sticky = 'e', padx=10, pady=10)

passLabel=Label(miFrame, text='Password')
passLabel.grid(row=1, column=0, sticky = 'e', padx=10, pady=10)

apellidoLabel=Label(miFrame, text='Apellido:')
apellidoLabel.grid(row=2, column=0, sticky = 'e', padx=10, pady=10)

direccionLabel=Label(miFrame, text='Direccion de casa')
direccionLabel.grid(row=3, column=0, sticky = 'e', padx=10, pady=10)



root.mainloop()