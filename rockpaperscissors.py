from tkinter import *
import tkinter.font as font
import random

playerscorecount = 0
computerscorecount = 0

options = [("rock", 0),("paper", 1),("scissors", 2)]

window = Tk()

def computerwin():
    global computerscorecount
    global playerscorecount
    computerscorecount += 1
    winnerlabel.configure(text= "Computer won this round")
    aiscore.config(text= f"Computer Score: {str(computerscorecount)}")
    playerscore.config(text= f"Your Score: {str(playerscorecount)}")

def playerwin():
    global computerscorecount
    global playerscorecount
    playerscorecount += 1
    winnerlabel.configure(text= "You won this round")
    aiscore.config(text= f"Computer Score: {str(computerscorecount)}")
    playerscore.config(text= f"Your Score: {str(playerscorecount)}")

def tie():
    global computerscorecount
    global playerscorecount
    winnerlabel.configure(text ="There was a tie this round")
    aiscore.config(text= f"Computer Score: {str(computerscorecount)}")
    playerscore.config(text= f"Player Score: {str(playerscorecount)}")

def player_choice(choice):
    global computerscorecount
    global playerscorecount
    print(choice[0])

    computerinput = computerchoice()
    print(computerinput[0])
    playerchoice.config(text= f"Your selection: {choice[0]}")
    aichoice.config(text= f"Computer selection: {computerinput[0]}")

    if choice == computerinput:
        tie()
    
    #If player has selected rock
    if choice[1] == 0:
        if computerinput[1] == 1:
            computerwin()
        elif computerinput[1] == 2:
            playerwin()
    #If player has selected paper
    elif choice[1] == 1:
        if computerinput[1] == 0:
            playerwin()
        elif computerinput[1] == 2:
            computerwin()
    #If player has selected scissors
    elif choice[1] == 2:
        if computerinput[1] == 0:
            computerwin()
        elif computerinput[1] == 1:
            playerwin()

def computerchoice():
    return random.choice(options)

gamefont = font.Font(size= 20)

gametitle = Label(window, text= "Rock, Paper, Scissors 🪨📃✂️", font = font.Font(size= 20, family= "Arial"), foreground= "grey")
gametitle.pack()

winnerlabel = Label(window, text="GO!", foreground= "green")
winnerlabel.pack()

optionsframe = Frame(window)
optionsframe.pack()
optionslabel = Label(optionsframe, text= "Your options:")
optionslabel.grid(row= 0, column= 0, pady= 8)
rockbutton = Button(optionsframe, text= "Rock", background= "pink", font= gamefont, command= lambda: player_choice(options[0]))
rockbutton.grid(row=1, column= 1, padx= 8, sticky= "nesw")
paperbutton = Button(optionsframe, text= "Paper", background= "light grey", font= gamefont, command= lambda: player_choice(options[1]))
paperbutton.grid(row=1, column= 2, padx= 8, sticky= "nsew")
scissorsbutton = Button(optionsframe, text= "Scissors", background= "light blue", font= gamefont, command= lambda: player_choice(options[2]))
scissorsbutton.grid(row= 1, column= 3, padx= 8, sticky= "nsew")
optionsframe.columnconfigure(index= [1, 2, 3], minsize= 170)
scoreframe = Frame(window)
scoreframe.pack()
scorelabel = Label(scoreframe, text= "Score:")
scorelabel.grid(row= 0, column= 0)
playerchoice = Label(scoreframe, text= "Your selection: ---")
playerchoice.grid(row= 1, column= 1)
playerscore = Label(scoreframe, text="Your score: ---")
playerscore.grid(row= 1, column= 2)
aichoice = Label(scoreframe, text= "Computer selection: ---")
aichoice.grid(row= 2, column= 1)
aiscore = Label(scoreframe, text= "Computer Score: ---")
aiscore.grid(row= 2, column= 2)
window.mainloop()