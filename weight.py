from tkinter import *
window = Tk()
window.title("Weight Converter")

def convert():
    gram = float(inputkgstr.get()) * 1000
    pound = float(inputkgstr.get()) * 2.20462
    ounce = float(inputkgstr.get()) * 35.27
    outputgrams.config(state= NORMAL)
    outputgrams.delete("1.0", END)
    outputgrams.insert(END, gram)
    outputgrams.config(state= DISABLED)

    outputpounds.config(state= NORMAL)
    outputpounds.delete("1.0", END)
    outputpounds.insert(END, pound)
    outputpounds.config(state= DISABLED)

    outputounce.config(state= NORMAL)
    outputounce.delete("1.0", END)
    outputounce.insert(END, ounce)
    outputounce.config(state= DISABLED)    

outputgrams = Text(window, width = 15, height= 1, state= DISABLED)
outputgrams.grid(column=0,row=3)
outputpounds = Text(window, width = 15, height= 1, state= DISABLED)
outputpounds.grid(column=1,row=3)
outputounce = Text(window, width = 15, height= 1, state= DISABLED)
outputounce.grid(column=2,row=3)
Label(window, text= "Enter weight in KG").grid(column=0, row= 0)
inputkgstr = StringVar()
inputkg = Entry(window, textvariable= inputkgstr)
inputkg.grid(column=1, row=0)
Button(window, text= "Convert", command= convert).grid(column=2, row=0)
Label(window, text= "Grams").grid(column=0,row=2)
Label(window, text= "Pounds").grid(column=1,row=2)
Label(window, text= "Ounce").grid(column=2,row=2)



window.mainloop()