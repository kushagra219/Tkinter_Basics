from tkinter import *

root = Tk()

def leftclick(event):
    print("Left")

def middleclick(event):
    print("Middle")

def rightclick(event):
    print("Right")

frame = Frame(height=300, width=250)
frame.bind("<Button-1>", leftclick)
frame.bind("<Button-3>", rightclick)
frame.pack()

root.mainloop()