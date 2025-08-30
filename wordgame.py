from tkinter import *
import random
from tkinter import messagebox

window = Tk()
window.title("WordJumble")
window.config(bg= "lightblue")
window.geometry("550x250")
window.resizable(False,False)

wordlist = ["animal","banana","chicken","donkey","egg","fireworks","gigantic","helicopter","indigo","jaguar","logo"]
jumbledlist = ["minala", "bnaaan","kcihcne","kdnoey","geg","rifokwrse","ggniacit", "cliehtpero","dniogi", "gajrua","lgoo"]

index = random.randrange(0, len(jumbledlist), 1)
correct_answers = 0
total_attempts = 0

score = ""

def checkanswer():
    global index, jumbledlist, wordlist, correct_answers, total_attempts, score
    total_attempts += 1
    playeranswer = entrybox.get()
    if playeranswer == wordlist[index]:
        messagebox.showinfo("Correct", "Your answer was correct")
        correct_answers += 1
        resetword()
    else:
        messagebox.showerror("Incorrect", "Your answer was incorrect")
    score = f"Score: {correct_answers} / {total_attempts}"
    scorelabel.config(text= score)

def resetword():
    global index, jumbledlist, wordlist
    index = random.randrange(0, len(jumbledlist), 1)
    outputlabel.config(text= jumbledlist[index])
    entrybox.delete(0, END)

def default():
    global index, jumbledlist, wordlist
    outputlabel.config(text= jumbledlist[index])

Label(window, text= "WordJumble - The Jumbled Word Game", font= ("Comic Sans MS", 20), fg= "darkblue", bg= "lightblue").pack()
outputlabel = Label(window, text= "jumbled word", font= ("Comic Sans MS", 15), fg= "darkblue", bg= "lightblue")
outputlabel.pack()
entrybox = Entry(window, width= 10, font= ("Comic Sans MS", 15), fg= "darkblue", bg= "lightblue")
entrybox.pack(pady= 3)
Button(window, text= "Check", bg= "green", fg= "white", font= ("Comic Sans MS", 12), command= checkanswer, width= 6).pack(pady= 3)
Button(window, text= "Reset", bg= "red", fg= "white", font= ("Comic Sans MS", 12), command= resetword, width= 6).pack(pady= 3)
scorelabel = Label(window, text= "Score: 0", font= ("Comic Sans MS", 12), fg= "darkblue", bg= "lightblue")
scorelabel.pack(pady= 3)

default()

window.mainloop()