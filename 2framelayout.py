from tkinter import *


window = Tk()
window.title("The Fun Machine")
window.config(background= "black")

window.resizable(False, False)

def add():
    listbox.insert(END, entrybox.get())

def remove():
    listbox.delete(listbox.curselection())

def showselect():
   selectedlabel.config(text= f"Selected: {listbox.get(listbox.curselection())}")
    
def showoutput():
    output.config(text= f"Your choice:\nActivity: {activitychooser.get()}\nExcitement: {excitementbox.get()}\nTime spent: {timespentbox.get()}")


listboxframe = Frame(window, relief= "groove", bg= "pink", bd= 5)



Label(listboxframe, text= "Listbox Operations", foreground= "white", font= ("Times New Roman", 20), background= "pink").grid(column=0, row= 0, padx= 10, pady= 10)

listboxinnerframe = Frame(listboxframe)

scrollbar = Scrollbar(listboxinnerframe, orient= "vertical")

listbox = Listbox(listboxinnerframe, background= "lightpink", yscrollcommand= scrollbar.set, font= ("Comic Sans MS", 12))

scrollbar.config(command= listbox.yview)


listbox.grid(column= 0, row= 0)
scrollbar.grid(column=1, row= 0, sticky= "ns")

listboxinnerframe.grid(padx= 10, pady= 10)


listboxframe.grid(column= 0, row= 0, padx= 10, pady = 10)

entrybox = Entry(listboxframe, bg= "lightpink")

entrybox.grid(padx= 10, pady= 10)

addbutton = Button(listboxframe, text= "ADD", font= ("Comic Sans MS", 15), bg= "lightpink", command= add)

addbutton.grid(padx= 10, pady= 10)

removebutton = Button(listboxframe, text= "REMOVE", font= ("Comic Sans MS", 15), bg= "lightpink", command= remove)

removebutton.grid(padx= 10, pady= 10)

showbutton = Button(listboxframe, text= "SHOW SELECTED", font= ("Comic Sans MS", 15), bg= "lightpink", command= showselect)

showbutton.grid(padx= 10, pady= 10)

selectedlabel = Label(listboxframe, text= "Selected: ", font= ("Comic Sans MS", 15), bg= "lightpink")

selectedlabel.grid(padx= 10, pady= 10)

adventureplannerframe = Frame(window, relief= "groove", bg= "purple", bd= 5)


Label(adventureplannerframe, text= "Adventure Planner", foreground= "white", font= ("Times New Roman", 20), background= "purple").grid(column=0, row= 0, padx= 10, pady= 10)

adventureplannerframe.grid(row= 0, column= 1)

Label(adventureplannerframe, text= "Choose activity", foreground= "white", font= ("Comic Sans MS", 15), background= "purple").grid(padx= 10, pady= 10)

Label(adventureplannerframe, text= "Rate Excitement", foreground= "white", font= ("Comic Sans MS", 15), background= "purple").grid(padx= 10, pady= 10)

Label(adventureplannerframe, text= "Time spent (hours)", foreground= "white", font= ("Comic Sans MS", 15), background= "purple").grid(padx= 10, pady= 10)

activitychooser = Spinbox(adventureplannerframe, values= ["Gaming", "Go for walk", "Read"], font= ("Comic Sans MS", 12), background= "MediumOrchid3")
activitychooser.grid(padx= 10, pady= 10, column= 1, row= 1)

excitementbox = Spinbox(adventureplannerframe, font= ("Comic Sans MS", 12), background= "MediumOrchid3", from_= 0, to= 10, increment= 0.5)
excitementbox.grid(padx= 10, pady= 10, column= 1, row= 2)

timespentbox = Spinbox(adventureplannerframe, font= ("Comic Sans MS", 12), background= "MediumOrchid3", from_= 0, to= 12, increment= 1)
timespentbox.grid(padx= 10, pady= 10, column= 1, row= 3)

showplan = Button(adventureplannerframe, text= "Show plan", font= ("Comic Sans MS", 15), background= "MediumOrchid3", command= showoutput)
showplan.grid(padx= 10, pady= 10, columnspan= 2, sticky="ew")

output = Label(adventureplannerframe, text= "Waiting for output...", font= ("Comic Sans MS", 15), background= "MediumOrchid3")
output.grid(padx= 10, pady= 10,columnspan= 2, sticky= "ew")

window.mainloop()
