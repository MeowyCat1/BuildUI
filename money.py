from tkinter import *
from currency_converter import CurrencyConverter
window = Tk()
window.resizable(width= False, height= False)

def convert():
    pound = float(poundsinput.get())
    c = CurrencyConverter()
    dollar = c.convert(amount= pound, currency= "GBP", new_currency= "USD")
    dollar = round(dollar, 2)
    dollaroutput.config(text= dollar)
Label(window, text= "£-$ Conversion").grid(row= 0, column= 1)
Label(window, text= "Pounds Amount £").grid(row= 1, column= 0)

poundsinput = Entry(window)
poundsinput.grid(row= 1, column= 2)

Label(window, text= "Dollar Amount $").grid(row= 2, column= 0)

dollaroutput = Label(window, text= "Waiting for input...")
dollaroutput.grid(row=2, column=2)

Button(window, text= "Convert", command= convert).grid(row= 2, column= 1)
window.mainloop()