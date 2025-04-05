from tkinter import *
from tkinter.ttk import *

window = Tk()

menubar = Menu(window)
filemenu = Menu(menubar, tearoff= 0)
menubar.add_cascade(label= "File", menu= filemenu)
newfilemenu = Menu(filemenu, tearoff= 0)
filemenu.add_cascade(menu= newfilemenu, label= "New File")
newfilemenu.add_command(label= "Text File", command= None)
newfilemenu.add_command(label= "Python File", command= None)
filemenu.add_separator()
filemenu.add_command(label= "Exit", command= window.destroy)

window.config(menu= menubar)
window.mainloop()