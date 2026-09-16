# Importing tkinter
import tkinter as tk
list1={"class":0,"time":0}
# Function to get the value from the checkbutton on checking or unchecking it.
def choice():
    # Checkbutton is checked.
    if choiceNum.get()==1:
        list1["class"]="mom d"
        list1["time"] = "9:00"
# GUI2
window = tk.Tk()
window.title("Geeksforgeeks")
window.geometry("300x200")
window.config(bg="green")
# variable to listen to checkbutton
choiceNum = tk.IntVar()
label1 = tk.Label(window,text="Want Pizza?",font=("Arial",13),
                  bg="green",fg="white")
label1.pack()
# Checkbutton
chkbtn = tk.Checkbutton(window,text="Click to Order",
                        command=choice,onvalue=1,
                        offvalue=0,variable=choiceNum)
chkbtn.pack()
# Label to display the result.
result_label = tk.Label(window,fg="white",bg="green",font=("Arial",15))
result_label.pack()
window.mainloop()
print(list1)
