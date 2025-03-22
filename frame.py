from tkinter import *

window = Tk()
window.config(background= "lightgreen")
window.geometry("600x400")

f1 = Frame(window, bd= 10, background= "blue")
f2 = Frame(window, bd= 10, background= "blue")
f3 = Frame(window, bd= 10, background= "blue")
f1.grid(row= 0, column= 0, padx = 5)
f2.grid(row= 0, column= 1, padx = 5)
f3.grid(row= 1, column= 0, padx= 5, pady= 5)
l1 = Label(f1, text= "Hello!", font= ("Comic Sans MS", 20), background= "green")
l2 = Label(f2, text= "I like frames!", font= ("Comic Sans MS", 20), background= "pink")
s1 = Spinbox(f3, from_= -10, to= 10)
s1.pack()
l1.pack()
l2.pack()
window.mainloop()