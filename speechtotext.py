from tkinter import *

import speech_recognition as spkrec

window = Tk()

title = Label(window, text= "Speech To Text", font= 20)
title.grid(padx= 10, pady= 10)

spkrecbutton = Button(window, text= "Recognise Speech", font= 15)
spkrecbutton.grid(padx= 10, pady= 10)

outputtext = Text(width= 25, height= 5, state= DISABLED)
outputtext.grid(row= 1, column= 1, padx= 10, pady= 10)

savebutton = Button(window, text= "Save to File", font= 15)

savebutton.grid(row= 1, column= 2, padx= 10, pady=  10)

window.mainloop()