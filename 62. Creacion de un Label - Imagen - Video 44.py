
from tkinter import *

root=Tk()

miFrame=Frame(root, width=500, height=400)

miFrame.pack()

miImagen=PhotoImage(file='imagen_trading_things.png')

miLabel=Label(miFrame, image=miImagen)

miLabel.place(x=10,y=10)    

root.mainloop()