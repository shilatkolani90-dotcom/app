import tkinter
from tkinter import *

photo=PhotoImage(file='mom.png')
window=Tk()
window.geometry("820x820")
window.title("my first app")
window.config(background="#ebaeb8")
#relief=RAISED,bd=10,padx=20,pady=20
label=Label(window,text="hello",font=('Flux',40,'bold'),fg="green",image=photo)
label.place(x=350,y=350)
window.mainloop()