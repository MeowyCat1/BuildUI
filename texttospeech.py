from tkinter import *
from gtts import gTTS
import os

def submit():
    language = "en"

    speech = gTTS(text= textentry.get(), lang= language, slow= False)
    speech.save("speechfile.wav")
    os.system("speechfile.wav")

window = Tk()

frame1= Frame(window, bg= "yellow")

title = Label(frame1, text= "Text-to-Speech", bg= "Yellow", font= ("Comic Sans MS", 20))
title.pack(padx= 10, pady= 10)

frame1.pack()

frame2 = Frame(window, bg= "red")

enterlabel = Label(frame2, bg= "red", text= "Enter text here:", font= ("Comic Sans MS", 12))
enterlabel.pack(padx= 10, pady= 10)

textentry = Entry(frame2, bg= "pink", width= 50, font= 12)
textentry.pack(padx= 10, pady= 10)

submitbutton = Button(frame2, text= "Submit", font= ("Comic Sans MS", 15), bg= "pink", width= 100, command= submit)
submitbutton.pack(padx= 10, pady= 10)

frame2.pack()

window.mainloop()