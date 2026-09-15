import tkinter
from tkinter import *

window=Tk()
window.geometry("820x820")
window.title("my first app")
window.config(background="#ebaeb8")
photo=PhotoImage(file='mom.png')

#relief=RAISED,bd=10,padx=20,pady=20
label=Label(window,text="hello",font=('Flux',40,'bold'),fg="green",relief=RAISED,bd=10,padx=20,pady=20,image=photo,compound="top")
label.place(x=0,y=0)
window.mainloop()