from tkinter import *
import tkinter.colorchooser as colour

class Paint(object):

    defaultpensize = 2.0
    defaultpencolour = "black"
    def __init__(self):
        self.window = Tk()
        self.window.title("Paint")
        self.window.config(bg= "lightblue")
        self.font = ("Comic Sans MS", 15)
        self.buttoncolour = "darkblue"
        self.fontcolour = "white"
        self.penbutton = Button(self.window, text= "Pen", activebackground= "purple", font= self.font, bg= self.buttoncolour, fg= self.fontcolour, activeforeground= "white", command= self.usepen)
        self.penbutton.grid(row= 0, column= 0)
        self.brushbutton = Button(self.window, text= "Brush", activebackground= "purple", font= self.font, bg= self.buttoncolour, fg= self.fontcolour, activeforeground= "white", command= self.usebrush)
        self.brushbutton.grid(row= 0, column= 1)
        self.eraserbutton = Button(self.window, text= "Eraser", activebackground= "purple", font= self.font, bg= self.buttoncolour, fg= self.fontcolour, activeforeground= "white", command= self.useeraser)
        self.eraserbutton.grid(row= 0, column= 2)
        self.colourbutton = Button(self.window, text= "Colour", activebackground= "purple", font= self.font, bg= self.buttoncolour, fg= self.fontcolour, activeforeground= "white", command= self.choosecolour)
        self.colourbutton.grid(row= 0, column= 3)
        #Tool Size Sliders
        self.penslider = Scale(self.window, from_= 1, to= 10, orient= HORIZONTAL, label= "Pen Size", font= ("Comic Sans MS", 12), bg= "lightblue", activebackground= "purple", troughcolor= "pink")
        self.penslider.grid(row=0,column=4)
        self.brushslider = Scale(self.window, from_= 10, to= 50, orient= HORIZONTAL, label= "Brush Size", font= ("Comic Sans MS", 12), bg= "lightblue", activebackground= "purple", troughcolor= "pink")
        self.eraserslider = Scale(self.window, from_= 1, to= 50, orient= HORIZONTAL, label= "Eraser Size", font= ("Comic Sans MS", 12), bg= "lightblue", activebackground= "purple", troughcolor= "pink")
        self.canvas = Canvas(self.window, bg= "white", width= 200, height= 200, highlightbackground= "black", highlightthickness= 8)
        self.canvas.grid(row= 1, column= 0, columnspan= 5, sticky= "nsew")
        self.setup()
        self.window.mainloop()

    def setup(self):
        self.old_x = None
        self.old_y = None
        self.linewidth = self.penslider.get()
        self.colour = self.defaultpencolour
        self.eraseron = False
        self.activebutton = self.penbutton
        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<ButtonRelease-1>", self.reset)

    def usepen(self):
        self.activatebutton(self.penbutton)
        self.brushslider.grid_remove()
        self.eraserslider.grid_remove()
        self.penslider.grid(row= 0, column= 4)
    
    def usebrush(self):
        self.activatebutton(self.brushbutton)
        self.penslider.grid_remove()
        self.eraserslider.grid_remove()
        self.brushslider.grid(row= 0, column= 4)

    def useeraser(self):
        self.activatebutton(self.eraserbutton, erasermode = True)
        self.brushslider.grid_remove()
        self.penslider.grid_remove()
        self.eraserslider.grid(row= 0, column= 4)

    def choosecolour(self):
        self.eraseron = False
        self.colour = colour.askcolor(color= self.colour)[1]

    def paint(self, event):
        if self.activebutton == self.brushbutton:
            self.linewidth = self.brushslider.get()
        elif self.activebutton == self.penbutton:
            self.linewidth = self.penslider.get()
        else:
            self.linewidth = self.eraserslider.get()
        paint_colour = "white" if self.eraseron else self.colour
        if self.old_x and self.old_y:
            self.canvas.create_line(self.old_x, self.old_y, event.x, event.y, width= self.linewidth, fill = paint_colour, capstyle= ROUND, smooth= True, splinesteps= 50)
        self.old_x = event.x
        self.old_y = event.y
    def activatebutton(self, buttontoactivate, erasermode = False):
        self.activebutton.config(relief= "raised")
        buttontoactivate.config(relief= "sunken")
        self.activebutton = buttontoactivate
        self.eraseron = erasermode

    def reset(self, event):
        self.old_x, self.old_y = None,None

if __name__ == "__main__":
    Paint()