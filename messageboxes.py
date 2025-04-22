from tkinter import *
from tkinter import messagebox

def info():
    messagebox.showinfo("Information", "Your computer has sucessfully duplicated itself.")

def askq():
    response = messagebox.askquestion("Question", "Would you like to enable self-destruct mode?")
    if response == "yes":
        messagebox.showinfo("Response", "Self destruct engaged sucessfully.")
    else:
        messagebox.showinfo("Response", "Phew, that was close!")

def warn():
    messagebox.showwarning("Warning","Very angry hamster detected in your vicinity. Please take cover.")

def error():
    messagebox.showerror("Error", "No error found.")
    
def askokcancel():
    response = messagebox.askokcancel("Windows Simulation System", "The universe is a simulation. Continue running simulation?")
    if response == False:
        messagebox.showinfo("Windows Simulation System", "Simulation Cancelled.")

def askyn():
    messagebox.askyesno("Question Asker", "Do you like answering pointless questions that do nothing for no reason?")

def askretrycancel():
    messagebox.askretrycancel("Alien Finder", "Aliens not found")


window = Tk()
window.title("Message Box Generating Machine")
window.geometry("600x600")

Button(window, text = "Information", command= info).pack()
Button(window, text = "Warning", command= warn).pack()
Button(window, text= "Error", command= error).pack()
Button(window, text= "Question", command= askq).pack()
Button(window, text= "OK / Cancel", command= askokcancel).pack()
Button(window, text= "Yes / No", command= askyn).pack()
Button(window, text= "Retry / Cancel", command= askretrycancel).pack()

window.mainloop()