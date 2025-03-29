from tkinter import *

window = Tk()
def display_text():
    entry = e1.get()
    l1.config(text= f"You entered: {entry}")
e1 = Entry(window, width= 200)
e1.pack()
b1 = Button(window, text= "Enter", command= display_text)
b1.pack()
l1 = Label(window, text= "")
l1.pack(padx= 10)

window.mainloop()