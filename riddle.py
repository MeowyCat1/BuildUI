from tkinter import *
import random

attempts = 0
correct = 0

def showscore():
    score.config(text=f"Score: {correct}/{attempts}")

def newriddle():
    global riddle
    riddledoc = open("riddles.txt")
    riddlestr = random.choice(riddledoc.readlines())
    riddleandans = riddlestr.split(sep= ":")
    riddle = riddleandans
    riddledoc.close()

def updateriddle():
    global riddle, output
    newriddle()
    output.config(text= riddle[0])
    

def checkans():
    global correct, attempts
    playeranswer = inputbox.get()
    if playeranswer.title() == riddle[1].rstrip():
        updateriddle()
        correct +=1
        attempts +=1
        showscore()
    else:
        attempts +=1
        showscore()
    

window = Tk()

window.title("Riddler")

Label(window, font= ("Comic Sans MS", 15), text= "Riddler").pack()

inputbox = Entry(window, font= ("Comic Sans MS", 12))
inputbox.pack()

Button(window, text= "Check", font= ("Comic Sans MS", 12), command= checkans).pack()
Button(window, text= "Skip", font= ("Comic Sans MS", 12), command= updateriddle).pack()
output = Label(font= ("Comic Sans MS", 12))
output.pack()
score = Label(font= ("Comic Sans MS", 12), text= "Score: 0/0")
score.pack()

updateriddle()

window.mainloop()