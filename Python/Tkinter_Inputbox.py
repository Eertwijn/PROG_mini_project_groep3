from Tkinter import *

master = Tk()
e = Entry(master)
e.pack()

e.focus_set()

def callback():
    e.get()

b = Button(master, text = "Zoeken", width = 10, command = callback)
b.pack()

mainloop()
