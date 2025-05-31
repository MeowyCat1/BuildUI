from tkinter import *


window = Tk()

charlist = []


def start():
    global charlist
    word = input("Enter the word: ")
    charlist = list(word)
    num = 0
    charlistwithnum = []
    for char in charlist:
        charlistwithnum.append((char, num))
        num += 1
    charlist = charlistwithnum


found_chars = []

def check(letter):
    global charlist
    global found_chars
    global strikes
    for char in charlist:
        if char[0] == letter and char[1] not in found_chars:
            found_chars.append(char[1])
            

def make_string():
    global charlist
    global found_chars
    string = ""
    for char in charlist:
        if char[1] in found_chars:
            string = string + char[0]
        else:
            string = string + "_"
    return string

def check_win():
    global charlist
    global found_chars
    won = True
    while won == True:
        for char in charlist:
            if char[1] in found_chars:
                won = True
            else:
                won = False
                break
            break
    return won

def run_gui():
    inputletter = entrybox.get()
    check(inputletter)
    output.config(text = make_string())


        
    

entrybox = Entry(window)
entrybox.grid(row=0, column= 0)
button = Button(window, text= "Check", command= run_gui)
button.grid(row= 0, column= 1)
output = Label(window, text= "Waiting for output.")
output.grid(row= 1, column= 0)


start()



window.mainloop()