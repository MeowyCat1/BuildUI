from tkinter import *

class Paint(object):
    def __init__(self):
        self.window = Tk()
        self.window.title("Paint")
        self.window.config(bg= "lightblue")
        self.font = ("Comic Sans MS", 15)
        self.buttoncolour = "darkblue"
        self.fontcolour = "white"
        self.penbutton = Button(self.window, text= "Pen", activebackground= "purple", font= self.font, bg= self.buttoncolour, fg= self.fontcolour, activeforeground= "white")
        self.penbutton.grid(row= 0, column= 0)
        self.brushbutton = Button(self.window, text= "Brush", activebackground= "purple", font= self.font, bg= self.buttoncolour, fg= self.fontcolour, activeforeground= "white")
        self.brushbutton.grid(row= 0, column= 1)
        self.eraserbutton = Button(self.window, text= "Eraser", activebackground= "purple", font= self.font, bg= self.buttoncolour, fg= self.fontcolour, activeforeground= "white")
        self.eraserbutton.grid(row= 0, column= 2)
        self.colourbutton = Button(self.window, text= "Colour", activebackground= "purple", font= self.font, bg= self.buttoncolour, fg= self.fontcolour, activeforeground= "white")
        self.colourbutton.grid(row= 0, column= 3)
        #Tool Size Sliders
        self.penslider = Scale(self.window, from_= 1, to= 10, orient= HORIZONTAL, label= "Pen Size", font= ("Comic Sans MS", 12), bg= "lightblue", activebackground= "purple", troughcolor= "pink")
        self.penslider.grid(row=0,column=4)
        self.brushslider = Scale(self.window, from_= 10, to= 50, orient= HORIZONTAL, label= "Brush Size", font= ("Comic Sans MS", 12), bg= "lightblue", activebackground= "purple", troughcolor= "pink")
        self.brushslider.grid(row=0,column=5)
        self.eraserslider = Scale(self.window, from_= 1, to= 50, orient= HORIZONTAL, label= "Eraser Size", font= ("Comic Sans MS", 12), bg= "lightblue", activebackground= "purple", troughcolor= "pink")
        self.eraserslider.grid(row=0,column=6)

        self.window.mainloop()
if __name__ == "__main__":
    Paint()