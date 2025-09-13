from tkinter import *
import requests
import html
import random

window = Tk()

def processquiz(answer=None):
    '''Does quizzy stuff'''
    global response
    if answer:
        pass
    else:
        response = requests.get("https://opentdb.com/api.php?amount=1&difficulty=easy").json()
        if response["response_code"] == 0:
            questionlabel = Label(window, text= html.unescape(response["results"][0]["question"]), font= ("Times New Roman", 12))
            questionlabel.grid(row= 1)
            answerslist = response["results"][0]["incorrect_answers"]
            answerslist.append(["results"][0]["correct_answer"])
            
            for answer in answerslist:
                Button(window, text= answer, command= lambda answer:processquiz(answer=answer)).grid(row= answerslist.index(answer)+2)
window.title("Multiple Choice Quiz")

Label(window, text= "Welcome to the Quiz!", font= ("Cooper", 20)).grid()

processquiz()

window.mainloop()