from tkinter import *
from tkinter.messagebox import *
import random
window = Tk()
window.config(background= "lightblue", pady= 30, padx= 10)
window.resizable(False,False)
window.geometry("500x180")

number = random.randint(1,20)

def setname():
    if nameentry.get() != "":
        showinfo("Welcome",f"Welcome, {nameentry.get().title()}, pick a number between 1 and 20")
    else:
        showerror("Error","Name not entered")

def checkanswer():
    if int(guessentry.get()) < number:
        showinfo("Result","Too low!")
    elif int(guessentry.get()) > number:
        showinfo("Result","Too high!")
    else:
        showinfo("Result",f"Correct! The answer was {number}.")
    

window.title("Guess The Number")

Label(window, text= "Welcome to the Number-Guessing Game!", font= ("Old English Text MT", 20)).grid(row= 0, column= 0, columnspan= 3, pady= 10)

Label(window, text= "Name:").grid(row= 1, column= 0)
nameentry = Entry(window)
nameentry.grid(row=1,column=1)
Button(window, text= "OK", command= setname, width= 20).grid(row=1, column= 2)
Label(window, text= "Take a guess:").grid(row=2, column= 0)
guessentry = Entry(window)
guessentry.grid(row= 2, column= 1)
Button(window, text= "Check", command= checkanswer, width= 20).grid(row=2, column= 2)


window.mainloop()