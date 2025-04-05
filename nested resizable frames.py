import tkinter as tk

window = tk.Tk()
window.columnconfigure(0, weight= 5)
window.rowconfigure(0, weight= 5)

f1 = tk.Frame(window, borderwidth= 3, relief= "groove", padx= 15, pady= 15)
f1.grid(pady= 40, padx= 40, column= 0, row= 0, sticky= "nsew")
f1.columnconfigure(0, weight= 5)
f1.columnconfigure(1, weight= 5)
f1.rowconfigure(0, weight=5)

f2 = tk.Frame(f1, borderwidth= 2, relief= "raised")
f2.grid(row= 0, column= 0, pady= 10, sticky="nsew")
f3 = tk.Frame(f1, borderwidth= 2, relief= "sunken")
f3.grid(row= 0, column= 1, pady= 10, sticky= "nsew")

l1 = tk.Label(f2, text= "Frame 2")
l2 = tk.Label(f3, text= "Frame 3")
l1.pack()
l2.pack()

window.mainloop()