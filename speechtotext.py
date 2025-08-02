from tkinter import *
from tkinter import filedialog, messagebox

import speech_recognition as spkrec

def speechrec():
    recognisespeech = spkrec.Recognizer()
    with spkrec.Microphone() as source:
        print("Ready to Speak.")
        audio = recognisespeech.listen(source, phrase_time_limit= 20)
        try:
            textresult = recognisespeech.recognize_google(audio)
        except:
            textresult = "Could not recognise voice. Please try again."
        outputtext.config(state= NORMAL)
        outputtext.delete(1.0, END)
        outputtext.insert(END, textresult)
        outputtext.config(state= DISABLED)
    
def savetext():
    filename = filedialog.asksaveasfile(defaultextension= ".txt", filetypes= [("Text Files", ".txt")])
    if filename:
        print(outputtext.get(1.0, END), file= filename)
        messagebox.showinfo(title= "Success", message= "File Saved Successfully")
    else:
        messagebox.showerror(title= "Error", message= "File Not Saved")

window = Tk()

title = Label(window, text= "Speech To Text", font= 20)
title.grid(padx= 10, pady= 10)

spkrecbutton = Button(window, text= "Recognise Speech", font= 15, command= speechrec)
spkrecbutton.grid(padx= 10, pady= 10)

outputtext = Text(width= 50, height= 10, state= DISABLED)
outputtext.grid(row= 1, column= 1, padx= 10, pady= 10)

savebutton = Button(window, text= "Save to File", font= 15, command= savetext)

savebutton.grid(row= 1, column= 2, padx= 10, pady=  10)

window.mainloop()