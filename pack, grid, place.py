from tkinter import *

window = Tk()

window.title("My Tkinter Window")
window.geometry("400x400")
window.configure(bg= "blue")

window.resizable(width= True, height= False)
# Pack method
l1 = Label(window, text= "Hello, this is a random window with lots of random words in it.", font= ("Gigi"), background= "lightyellow", foreground= "magenta", justify= "left", wraplength= 180, padx= 10, pady = 20)
#l1.pack()

e1 = Entry(window)
#e1.pack()

b1 = Button(window, text= "Boom!", command= window.destroy)
#b1.pack()
#Grid Method
'''l1.grid(row= 0, column= 0, pady= 10)
e1.grid(row = 0, column= 1, pady= 10)
b1.grid(row= 1, column= 0, pady= 10)'''

#Place Method
l1.place(x= 0, y= 0)
e1.place(x=100, y=100)
b1.place(x=200, y= 200)

window.mainloop()