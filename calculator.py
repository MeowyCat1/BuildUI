from tkinter import *
from tkinter.ttk import *

calcstring = ""
resetonpress = False

window = Tk()
window.title("Calculator")

window.resizable(False, False)

def addtostring(item):
    global resetonpress, calcstring, calculationview
    if resetonpress == True:
        calcstring = ""
        resetonpress = False
    calcstring = calcstring + item
    calculationview.config(text= calcstring)

def calculate():
    global calcstring, resetonpress, calculationview
    resetonpress = True
    calculationview.config(text= eval(calcstring))

def clear():
    global calcstring, resetonpress, calculationview
    resetonpress = False
    calcstring = ""
    calculationview.config(text= calcstring)
    
    

def one():
    addtostring("1")

def two():
    addtostring("2")

def three():
    addtostring("3")

def four():
    addtostring("4")

def five():
    addtostring("5")

def six():
    addtostring("6")

def seven():
    addtostring("7")

def eight():
    addtostring("8")

def nine():
    addtostring("9")


def zero():
    addtostring("0")

def add():
    addtostring("+")

def subtract():
    addtostring("-")

def multiply():
    addtostring("*")

def divide():
    addtostring("/")

def decimal():
    addtostring(".")

calculationview = Label(window)

calculationview.grid(row=0, column= 0, columnspan= 4, sticky= "nsew")

onebutton = Button(text= "1", command= one)
onebutton.grid(row= 1, column= 0)

twobutton = Button(text= "2",command= two)
twobutton.grid(row=1, column= 1)

threebutton = Button(window, text= "3", command= three)
threebutton.grid(row= 1, column= 2)

fourbutton = Button(window, text= "4", command= four)
fourbutton.grid(row= 2, column= 0)

fivebutton = Button(window, text= "5", command= five)
fivebutton.grid(row= 2, column= 1)

sixbutton = Button(window, text= "6", command= six)
sixbutton.grid(row= 2, column= 2)

sevenbutton = Button(window, text= "7", command= seven)
sevenbutton.grid(row= 3, column= 0)

eightbutton = Button(window, text= "8", command= eight)
eightbutton.grid(row= 3, column= 1)

ninebutton = Button(window, text= "9", command= nine)
ninebutton.grid(row= 3, column= 2)

zerobutton = Button(window, text= "0", command= zero)
zerobutton.grid(row= 4, column= 1)

addbutton = Button(window, text= "+", command= add)
addbutton.grid(row= 5, column= 0)

subtractbutton = Button(window, text= "-", command= subtract)
subtractbutton.grid(row= 5, column= 1)

multiplybutton = Button(window, text= "x", command= multiply)
multiplybutton.grid(row= 5, column= 2)

dividebutton = Button(window, text= "÷", command= divide)
dividebutton.grid(row= 5, column= 3)

decimalbutton = Button(text= ".", command= decimal)
decimalbutton.grid(row= 4, column= 0)

calulatebutton = Button(text= "=", command= calculate)
calulatebutton.grid(row=1, column= 3, rowspan= 4, sticky= NSEW)

clearbutton = Button(window, text= "AC", command= clear)
clearbutton.grid(row= 6, columnspan= 4, sticky= NSEW)

window.mainloop()