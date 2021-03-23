
from tkinter import *

root=Tk()

miFrame=Frame(root, width=500, height=400)

miFrame.pack()

miLabel=Label(miFrame, text="Trading Room", fg='red', font=('Montserrat ExtraBold', 35))

miLabel.place(x=100,y=200)

root.mainloop()