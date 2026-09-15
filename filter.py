import tkinter
from tkinter import *



root = tkinter.Tk()

var1 = tkinter.IntVar()
var2 = tkinter.IntVar()

tkinter.Checkbutton(root, text="Location", variable=var1).grid(row=0, sticky=tkinter.W)
tkinter.Checkbutton(root, text="Female", variable=var2).grid(row=1, sticky=tkinter.W)

root.mainloop()