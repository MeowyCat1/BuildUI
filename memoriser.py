from tkinter import *
from tkinter.filedialog import *

window = Tk()
window.title("Memoriser")

def openfile():
    pass

def additem():
    listbox.insert(END, entrybox.get())
    entrybox.delete(0, END)

def savefile():
    pass

def deleteitem():
    listbox.delete(listbox.curselection())

openbutton = Button(window, text= "Open", command= openfile, width= 10)
openbutton.pack(side= LEFT, padx= 5, pady = 5)

addbutton = Button(window, text= "Add", command= additem, width= 10)
addbutton.pack(side= LEFT, padx= 5, pady = 5)

savebutton = Button(window, text= "Save", command= savefile, width= 10)
savebutton.pack(side= LEFT, padx= 5, pady = 5)

deletebutton = Button(window, text= "Delete", command= deleteitem, width= 10)
deletebutton.pack(side= LEFT, padx= 5, pady = 5)

listboxframe = Frame(window)
listboxframe.pack(padx = 5, pady= 5)

entrybox = Entry(listboxframe)
entrybox.pack(padx= 5, pady= 5)

scrollbar = Scrollbar(listboxframe, orient= VERTICAL)
scrollbar.pack(side= RIGHT, fill= Y)

listbox = Listbox(listboxframe, yscrollcommand= scrollbar.set, width= 50, bg= "light blue")
listbox.pack(side= LEFT)

scrollbar.config(command= listbox.yview)

list = ["1","2","3","Hello","Meow😺"]

for item in list:
    listbox.insert(END, item)

window.mainloop()