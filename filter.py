import tkinter
from tkinter import *

# root = tkinter.Tk()
#
# var1 = tkinter.IntVar()
# var2 = tkinter.IntVar()
#
# tkinter.Checkbutton(root, text="Location", variable=var1).grid(row=0, sticky=tkinter.W)
# tkinter.Checkbutton(root, text="days", variable=var2).grid(row=1, sticky=tkinter.W)
#
#
# root.mainloop()


PERISHABLE_OPTIONS = {'Vegetables': 0, 'Fruits': 0, 'Bread': 0, 'Dairy': 0, 'Meat': 0, 'Other': 0}
NONPERISHABLE_OPTIONS = {'Books': 0, 'Clothes': 0, 'Dry Food': 0, 'Household': 0, 'Sanitary': 0, 'Other': 0}


class Frame(tkinter.Frame):
    """The frame that has all the checkbuttons."""

    def __init__(self, master):
        tkinter.Frame.__init__(self, master=master)

        # Create the label
        label = tkinter.Label(self, text="Choose your donations!")
        label.pack(side="top", fill="x", pady=10)

        # Create the radiobuttons
        category_of_donation = {"Perishable": "1", "Non-Perishable": "2"}
        var = tkinter.StringVar(value="1")
        for text, value in category_of_donation.items():
            r = tkinter.Radiobutton(self, text=text, variable=var, value=value, command=lambda: self.show_checkbox(var))
            r.pack(anchor="center", padx=5, pady=5)

        # Create the submit button (doesn't do anything here)
        tkinter.Button(self, text="Submit").pack()

        # Create the checkbuttons
        self.perishables = []
        for i in PERISHABLE_OPTIONS:
            PERISHABLE_OPTIONS[i] = tkinter.IntVar()
            checkbutton = tkinter.Checkbutton(self, text=i, variable=PERISHABLE_OPTIONS[i])
            self.perishables.append(checkbutton)

        # Create the checkbuttons
        self.nonperishables = []
        for i in NONPERISHABLE_OPTIONS:
            NONPERISHABLE_OPTIONS[i] = tkinter.IntVar()
            checkbutton = tkinter.Checkbutton(self, text=i, variable=NONPERISHABLE_OPTIONS[i])
            self.nonperishables.append(checkbutton)

        # Show the perishabe checkbuttons
        self.show_checkbox(var)

    def show_checkbox(self, v):
        """Show the checkboxes for selected radio button NUMBER."""

        # Show the perishables
        if v.get() == "1":
            for c in self.nonperishables:
                c.pack_forget()
            for c in self.perishables:
                c.pack(anchor="center", padx=5, pady=5)

        # Or show the non-perishables
        if v.get() == "2":
            for c in self.perishables:
                c.pack_forget()
            for c in self.nonperishables:
                c.pack(anchor="center", padx=5, pady=5)


if __name__ == "__main__":
    root = tkinter.Tk()
    root.geometry("440x640")
    frame = Frame(root)
    frame.pack(expand=True, fill="both")
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