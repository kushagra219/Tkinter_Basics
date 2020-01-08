from tkinter import *

root = Tk()

def printName(event):
    print("My name is Kush!")

button = Button(root, text="Print my Name")
button.bind("<Button-1>",printName)
button.pack()

root.mainloop()