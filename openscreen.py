import tkinter
from tkinter import *
from tkinter import messagebox


def text_list():
    temp_text = ""
    for i in range(len(constants.PSYCHOLOGIST)):
        for key in constants.PSYCHOLOGIST[i].keys():
            temp_text += constants.PSYCHOLOGIST[i][key] + " "
        temp_text += "\n"
    print(temp_text)
    return temp_text


text1 = text_list()
meet = tk.Label(self, text=text1, font=('calibre', 10, 'bold'), background="pink")
meet.pack(side="top")
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

def button_clicked():
    def helloCallBack():
       msg  = messagebox.showinfo( "arbeltry", "good")


    B = Button(window, text ="Hello", command = helloCallBack, activebackground="blue", width=15, height=2)
    B.place(x=200,y=200)

def text_box_clicked():
    my_entry = Entry(window, width=40)
    my_entry.place(x=300,y=300)
    my_entry.pack(pady=20)
# a

button_clicked()
window.mainloop()