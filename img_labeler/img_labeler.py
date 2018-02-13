#!/bin/python

from tkinter import *

root = Tk()

label_1 = Label(root, text = "Hier kommen die Bilder")
label_2 = Label(root, text = "Hier kommen die Labels")

canvas = Canvas(root,width=900, height=700)
img = PhotoImage(file="/home/ivanna/no-image.png")
canvas.create_image(20,20, anchor=NW, image=img)	

label_1.grid(row=0, column=0, sticky=N)
label_2.grid(row=0, column = 1, sticky=N)
canvas.grid(row=1,column =0 )

root.mainloop()
