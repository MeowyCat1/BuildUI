from tkinter import *

window = Tk()

window.title("My Tkinter Window")
window.geometry("400x400")
window.configure(bg= "blue")

window.resizable(width= True, height= False)

l1 = Label(window, text= "Hello, this is a random window with lots of random words in it.", font= ("Gigi"), background= "lightyellow", foreground= "magenta", justify= "left", wraplength= 100, padx= 10, pady = 20)
l1.pack()

e1 = Entry(window)
e1.pack()

b1 = Button(window, text= "Hi There")
b1.pack()

window.mainloop()