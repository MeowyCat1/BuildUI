import tkinter as tk
import tkinter.messagebox as msg
import random

class noughtsandcrosses:
    def __init__(self, window):
        self.window = window
        self.window.title("Noughts and Crosses")
        self.mode = None
        self.currentplayer = "X"
        self.buttons = [[None for _ in range(3)]for _ in range(3)]
        self.createmodeselection()

    def createmodeselection(self):
        self.modeframe = tk.Frame(self.window)
        self.modeframe.pack()
        self.optionslabel = tk.Label(self.modeframe, text= "Select gamemode")
        self.optionslabel.pack()
        self.singleplayerbutton = tk.Button(self.modeframe, text= "Singleplayer", command= lambda: self.start_game("single"))
        self.singleplayerbutton.pack()
        self.multiplayerbutton = tk.Button(self.modeframe, text= "Multiplayer", command= lambda: self.start_game("multi"))
        self.multiplayerbutton.pack()

    def start_game(self, mode):
        self.mode = mode
        self.modeframe.destroy()
        self.createwidget()

    def createwidget(self):
        for row in range(3):
            for col in range(3):
                button = tk.Button(self.window, text= "", width= 4, height= 4, command = lambda r = row, c = col : self.onbuttonclicked(r, c))
                button.grid(row= row, column= col)
                self.buttons[row][col] = button

    def onbuttonclicked(self, row, col):
        if self.buttons[row][col]["text"] == "" and not self.checkwinner():
            self.buttons[row][col]["text"] = self.currentplayer
            if self.checkwinner():
                msg.showinfo(title= "Game Over", message= f"Player {self.currentplayer} wins!")
                self.resetgame()
            elif self.isboardfull():
                msg.showinfo(title= "Game Over", message= "It's a tie!")
                self.resetgame()

    def checkwinner(self):
        pass

    def resetgame(self):
        pass

    def isboardfull(self):
        pass

if __name__ == "__main__":
    window = tk.Tk()
    game = noughtsandcrosses(window)
    window.mainloop()