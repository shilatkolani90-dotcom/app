# Importing tkinter
import tkinter as tk
def filter1(self):
    loc={"north":0,"south":0,"center":0}
    def choice():
        # Checkbutton is checked.
        if choiceNum.get()==1:
            loc["north"]= 1
        if choiceNum2.get() == 1:
            loc["south"] = 1
        if choiceNum3.get() == 1:
            loc["center"] = 1
    choiceNum = tk.IntVar()
    choiceNum2 = tk.IntVar()
    choiceNum3 = tk.IntVar()
    label1 = tk.Label(self,text="pick the Location",font=("Arial",13),
                      bg="pink",fg="white")

    label1.pack()
    # Checkbutton
    chkbtnnorth = tk.Checkbutton(self,text="north",
                            command=choice,onvalue=1,
                            offvalue=0,variable=choiceNum)
    chkbtnsouth = tk.Checkbutton(self, text="south",
                                 command=choice, onvalue=1,
                                 offvalue=0, variable=choiceNum2)
    chkbtncenter = tk.Checkbutton(self, text="center",
                                 command=choice, onvalue=1,
                                 offvalue=0, variable=choiceNum3)
    chkbtnnorth.pack()
    chkbtnsouth.pack()
    chkbtncenter.pack()
    return loc
