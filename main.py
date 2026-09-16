import tkinter as tk
from PIL import ImageTk, Image
import os

import constants
import filter

# Lucida Handwriting
# Centaur
class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()
#
class Page1(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="Welcome to our site",font=('Lucida Handwriting',20,'bold'),background="pink")
       label.pack(side="top")

       self.config(bg="pink")

class Page2(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       self.config(bg="pink")
       name_var = tk.StringVar()
       passw_var = tk.StringVar()
       Pname_ver=  tk.StringVar()
       loction_var = tk.StringVar()
       date_var = tk.StringVar()
       #
       def submit():
           name = name_var.get()
           password = passw_var.get()
           Pname=Pname_ver.get()
           loction = loction_var.get()
           date = date_var.get()

           dict_temp =  {"name": Pname,"place":loction,'date':date,"hour":password,"sub":name}
           constants.PSYCHOLOGIST.append(dict_temp)
           print(constants.PSYCHOLOGIST)

           name_var.set("")
           passw_var.set("")
           Pname_ver.set("")
           loction_var.set("")
           date_var.set("")


       name_label = tk.Label(self, text='class theme', font=('calibre', 10, 'bold'))
       name_label.pack(side="top")
       name_entry = tk.Entry(self, textvariable=name_var, font=('calibre', 10, 'normal'))
       name_entry.pack(side="top")
       passw_label = tk.Label(self, text='time', font=('calibre', 10, 'bold'))
       passw_label.pack(side="top")
       passw_entry = tk.Entry(self, textvariable=passw_var, font=('calibre', 10, 'normal'))
       passw_entry.pack(side="top")
       loc_label = tk.Label(self, text='loction', font=('calibre', 10, 'bold'))
       loc_label.pack(side="top")
       loc_entry = tk.Entry(self, textvariable=loction_var, font=('calibre', 10, 'normal'))
       loc_entry.pack(side="top")
       date_label = tk.Label(self, text='date', font=('calibre', 10, 'bold'))
       date_label.pack(side="top")
       date_entry = tk.Entry(self, textvariable=date_var, font=('calibre', 10, 'normal'))
       date_entry.pack(side="top")
       Pname_label = tk.Label(self, text='your name', font=('calibre', 10, 'bold'))
       Pname_label.pack(side="top")
       Pname_entry = tk.Entry(self, textvariable=Pname_ver, font=('calibre', 10, 'normal'))
       Pname_entry.pack(side="top")
       sub_btn = tk.Button(self, text='Submit', command=submit)
       sub_btn.pack(side="top")



class Page3(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       self.config(bg="pink")
       list_of_loc={}
       list_of_loc=filter.filter1(self)


class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = Page1(self)
        p2 = Page2(self)
        p3 = Page3(self)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = tk.Button(p2, text="Home page",font=('Centaur',14,'bold'), command=p1.show)
        b4= tk.Button(p3, text="Home page",font=('Centaur',14,'bold'), command=p1.show)
        b2 = tk.Button(p1, text="doctor",font=('Centaur',25,'bold'), command=p2.show,background="pink")
        b3 = tk.Button(p1, text="patient",font=('Centaur',25,'bold'), command=p3.show,background="pink")

        b1.pack(side="bottom")
        b2.pack(side="bottom", fill="both",expand=True)
        b3.pack(side="bottom", fill="both",expand=True)
        b4.pack(side="bottom")

        p1.show()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("my app")
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("440x640")
    root.mainloop()