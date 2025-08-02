from tkinter import *
from tkinter import messagebox


def add():
    addresslistbox.insert(END, f"Name: {nimput.get()} Email: {einput.get()} Phone: {pinput.get()}")

def delete():
    addresslistbox.delete(addresslistbox.curselection())
    

window = Tk()
window.title("Address Book")

addresslistbox = Listbox(window, width= 80)
addresslistbox.grid(rowspan= 3)

Label(window, text= "Name:").grid(row=0, column=1)
Label(window, text= "Email:").grid(row = 1, column= 1)
Label(window, text= "Phone:").grid(row= 2, column=1)

nimput = Entry(window)
nimput.grid(row= 0, column= 2)
einput = Entry(window)
einput.grid(row= 1, column=2)
pinput = Entry(window)
pinput.grid(row= 2, column= 2)

addbutton = Button(text= "Add", command = add)
addbutton.grid(columnspan= 3, sticky= "ew", )
deletebutton = Button(text= "Delete", command = delete)
deletebutton.grid(columnspan= 3, sticky= "ew")



window.mainloop()