import tkinter
from tkinter import *
from tkinter import messagebox

# from numpy.ma.core import size
#shalom
window=Tk()
window.geometry("820x820")
window.title("my first app")
window.config(background="#ebaeb8")
photo=PhotoImage(file='mom.png')
# button
#relief=RAISED,bd=10,padx=20,pady=20,image=photo,compound="top"
label=Label(window,text="hello,welcome to our site",font=('Flux',40,'bold'),fg="white",background="#ebaeb8")
label.place(x=70,y=0)

# def button_clicked():
#     def helloCallBack():
#        msg  = messagebox.showinfo( "arbeltry", "good")
#
#
#     B = Button(window, text ="Hello", command = helloCallBack, activebackground="blue", width=15, height=2)
#     B.place(x=200,y=200)

# def text_box_clicked():
#     my_entry = Entry(window, width=40)
#     my_entry.place(x=300,y=300)
#     my_entry.pack(pady=20)

import tkinter as tk
from tkinter import PhotoImage
from PIL import ImageTk, Image

img = Image.open("user1.png")
res_img = img.resize((400, 300))
res_img.save('user_resized.png')

img = ImageTk.PhotoImage(file='user_resized.png')
imgLabel = Label(window, image=img)
imgLabel.place(x=200, y=100)


img = Image.open("doctor1.png")
res_img = img.resize((400, 300))
res_img.save('user_resized.png')

img = ImageTk.PhotoImage(file='doctor_resized.png')
imgLabel = Label(window, image=img)
imgLabel.place(x=200, y=100)

# h

window.mainloop()