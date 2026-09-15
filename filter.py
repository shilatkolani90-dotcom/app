import tkinter
from tkinter import *

root = tkinter.Tk()

var1 = tkinter.IntVar()
var2 = tkinter.IntVar()

tkinter.Checkbutton(root, text="Location", variable=var1).grid(row=0, sticky=tkinter.W)
tkinter.Checkbutton(root, text="days", variable=var2).grid(row=1, sticky=tkinter.W)


root.mainloop()


# import tkinter as tk


# def toggle_options() -> None:
#     if var1.get():
#         frame_c.pack()  # show the frame
#     else:
#         frame_c.pack_forget()  # hide the frame

#
# window = tk.Tk()
# frame_a = tk.Frame(window)
# frame_b = tk.Frame(window)
# frame_c = tk.Frame(window)
#
# frame_a.pack()
# frame_b.pack()
#
# entry1 = tk.Entry(frame_a, width=10)
# entry1.pack()
# entry2 = tk.Entry(frame_c, width=10)
# entry2.pack()
#
# var1 = tk.BooleanVar()
# checkbtn = tk.Checkbutton(
#     frame_b,
#     text="more options?",
#     variable=var1,
#     command=toggle_options,  # set the callback function here
# )
# checkbtn.pack()
#
# window.mainloop()