from tkinter import *

window = Tk()
window.title("CALENDER")
l1 = Label(window, text= "CALENDER", font= ("Times New Roman", 30), background= "grey")
l1.pack()
l2 = Label(window, text= "Enter Year", background= "lightgreen")
l2.pack()
e1 = Entry()
e1.pack()
b1 = Button(window, text= "Show Calender", background= "red")
b1.pack()
b2 = Button(window, text= "Exit", background= "red", command= window.destroy)
b2.pack()
window.mainloop()