from tkinter import *
window = Tk()
window.config(background= "red")
title = Label(window, text= "Food Ordering")
title.grid(column=0, row= 0, padx = 2, pady= 10)
l1 = Label(window, text= "Enter your meal and quantity. Our Magic Machine will make any food in the world!")
l1.grid(column= 0, row= 1,padx= 2, pady= 10,)
e1 = Entry()
e1.grid(column= 0, row= 2, padx= 2, pady= 10, sticky= E+W)
s1 = Spinbox(from_=0, to= 20)
s1.grid(column = 1, row= 2, padx= 2, pady= 10,)
l2 = Label(window, text= "Enter your drink and quantity. Our Magic Machine will make any food in the world!")
l2.grid(column= 0, row= 3,padx= 2, pady= 10,)
e2 = Entry()
e2.grid(column= 0, row= 4, padx= 2, pady= 10, sticky= E+W)
s2 = Spinbox(from_=0, to= 20)
s2.grid(column = 1, row= 4, padx= 2, pady= 10,)
window.mainloop()