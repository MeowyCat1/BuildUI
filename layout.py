from tkinter import *

window = Tk()

window.title("Layout")
window.resizable(width= False, height= False)

l1 = Label(window, text= "Label1", background= "green", foreground= "white", bd= 50)
l1.grid(row= 0, column= 0)
l2 = Label(window, text= "Label2", background= "yellow", foreground= "white", bd= 50)
l2.grid(row= 0, column= 1)
l3 = Label(window, text= "Label3", background= "turquoise", foreground= "white", bd = 50)
l3.grid(row= 0, column= 2)
l4 = Label(window, text= "Label4", background= "lightblue", foreground= "white", bd = 50)
l4.grid(row= 1, column= 0, columnspan= 2, sticky=E+W)
l5 = Label(window, text= "Label5", background= "magenta", foreground= "white", bd = 50)
l5.grid(row= 1, column= 2)
window.mainloop()