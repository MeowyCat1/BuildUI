from tkinter import *
import tkinter.font as font


window = Tk()

gamefont = font.Font(size= 12)

gametitle = Label(window, text= "Rock, Paper, Scissors 🪨📃✂️", font = font.Font(size= 20, family= "Arial"), foreground= "grey")
gametitle.pack()

winnerlabel = Label(window, text="GO!", foreground= "green")
winnerlabel.pack()

optionsframe = Frame(window)
optionsframe.pack()
optionslabel = Label(optionsframe, text= "Your options:")
optionslabel.grid(row= 0, column= 0, pady= 8)
rockbutton = Button(optionsframe, text= "Rock", background= "pink")
rockbutton.grid(row=1, column= 1, padx= 8)
paperbutton = Button(optionsframe, text= "Paper", background= "light grey")
paperbutton.grid(row=1, column= 2, padx= 8)
scissorsbutton = Button(optionsframe, text= "Scissors", background= "light blue")
scissorsbutton.grid(row= 1, column= 3, padx= 8)
scoreframe = Frame(window)
scoreframe.pack()
scorelabel = Label(scoreframe, text= "Score:")
scorelabel.grid(row= 0, column= 0)
playerchoice = Label(scoreframe, text= "Your selection: ---")
playerchoice.grid(row= 1, column= 1)
playerscore = Label(scoreframe, text="Your score: ---")
playerscore.grid(row= 1, column= 2)
aichoice = Label(scoreframe, text= "Computer selected: ---")
aichoice.grid(row= 2, column= 1)
aiscore = Label(scoreframe, text= "Computer Score: ---")
aiscore.grid(row= 2, column= 2)
window.mainloop()