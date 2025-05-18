from tkinter import *
from tkinter.ttk import *

window = Tk()
window.resizable(False, False)

def convert():
    distance = float(inputspeed.get()) * float(inputdistance.get())
    outputstr = f"{distance} miles"
    output.config(text= outputstr)

title = Label(window, text= "Speed and Time to Distance calculator")
title.grid(row= 0, column= 0)
Label(window, text= "Speed (mph)").grid(row=1, column= 0)
inputspeed = Entry(window)
inputspeed.grid(column= 1, row= 1)
Label(window, text="Time (Hours)").grid(column= 0, row= 2)
inputdistance = Entry(window)
inputdistance.grid(column= 1, row= 2)
Button(window, text= "Convert", command= convert).grid(column=0, row= 3)
output = Label(window, text= "Waiting for output...")
output.grid(column= 1, row= 3)
window.mainloop()