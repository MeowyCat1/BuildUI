from tkinter import *

def makebox():
    name = nameentry.get().title()
    catprofile = Tk()
    catprofile.title(f"{name}'s cat profile")
    catprofile.config(background= "lightpink")
    Label(catprofile, text= f"Meet {name}", font= ("Comic Sans MS", 20), background= "lightpink").pack()
    Label(catprofile, text= f"{name} is {ageentry.get()} years old.\n Did you know that {name} {funfactentry.get().lower()}?", font= ("Ink Free", 15), background= "lightpink").pack()

window = Tk()

title = Label(window, text= "Welcome to the Cat Machine!")
title.grid(row= 0, column= 0)

Label(window, text= "Name").grid(row= 1, column= 0)
Label(window, text= "Age").grid(row= 2, column= 0)
Label(window, text= "Fun Fact").grid(row= 3, column= 0)

nameentry = Entry(window)
nameentry.grid(row= 1, column= 1)
ageentry = Entry(window)
ageentry.grid(row= 2, column= 1)
funfactentry = Entry(window)
funfactentry.grid(row=3, column= 1)


Button(window, text= "Make Window", command= makebox).grid(row= 4, column= 0, columnspan= 2)

window.mainloop()