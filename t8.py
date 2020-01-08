from tkinter import *

root = Tk()

canvas = Canvas(root, width=200, height=200)
canvas.pack()

blackline = canvas.create_line(0, 0, 200, 50)
redline = canvas.create_line(0, 100, 200, 50, fill='red')
greenbox = canvas.create_rectangle(25, 25, 150, 200, fill="blue")

canvas.delete(redline)

root.mainloop()