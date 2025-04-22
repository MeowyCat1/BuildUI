from tkinter import *
from tkinter.ttk import *
window = Tk()
window.title("Weight Converter")

def convert():
    three = 1 + 1


Label(window, text= "Enter weight in KG").grid(column=0, row= 0)
inputkg = Entry(window).grid(column=1, row=0)
Button(window, text= "Convert", command= convert).grid(column=2, row=0)
Label(window, text= "Grams").grid(column=0,row=2)
Label(window, text= "Pounds").grid(column=1,row=2)
Label(window, text= "Ounce").grid(column=2,row=2)
outputgrams = Label(window, text= "Waiting for input...").grid(column=0,row=3)
outputpounds = Label(window, text= "Waiting for input...").grid(column=1,row=3)
outputounce = Label(window, text= "Waiting for input...").grid(column=2,row=3)
window.mainloop()