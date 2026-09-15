import tkinter
from tkinter import *

from numpy.ma.core import size
#
window=Tk()
window.geometry("820x820")
window.title("my first app")
window.config(background="#ebaeb8")
photo=PhotoImage(file='mom.png')

#relief=RAISED,bd=10,padx=20,pady=20,image=photo,compound="top"
label=Label(window,text="hello,welcome to our site",font=('Flux',40,'bold'),fg="white",background="#ebaeb8")
label.place(x=70,y=0)
window.mainloop()