from tkinter import *
from tkinter.filedialog import *

window = Tk()
window.title("The Magic Colour Changing Window!")


def additem():
    listbox.insert(END, entrybox.get())
    entrybox.delete(0, END)

def deleteitem():
    listbox.delete(listbox.curselection())

def changecolour():
    colour = listbox.selection_get()
    window.config(background= colour)


addbutton = Button(window, text= "Add", command= additem, width= 15)
addbutton.pack(side= LEFT, padx= 5, pady = 5)


deletebutton = Button(window, text= "Delete", command= deleteitem, width= 15)
deletebutton.pack(side= LEFT, padx= 5, pady = 5)

colourbutton = Button(window, text= "Change Colour", command= changecolour, width= 15)
colourbutton.pack(side= LEFT, padx= 5, pady = 5)

listboxframe = Frame(window)
listboxframe.pack(padx = 5, pady= 5)

entrybox = Entry(listboxframe)
entrybox.pack(padx= 5, pady= 5)

scrollbar = Scrollbar(listboxframe, orient= VERTICAL)
scrollbar.pack(side= RIGHT, fill= Y)

listbox = Listbox(listboxframe, yscrollcommand= scrollbar.set, width= 50)
listbox.pack(side= LEFT)

scrollbar.config(command= listbox.yview)

list = ["Red", "Orange", "Yellow", "Pink"]

for item in list:
    listbox.insert(END, item)

window.mainloop()