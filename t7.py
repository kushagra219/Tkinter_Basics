from tkinter import *
import tkinter.messagebox

root = Tk()
tkinter.messagebox.showinfo('Windows title', 'Monkeys can live upto 300 years')
ans = tkinter.messagebox.askquestion('Question1', 'Do you like silly faces?')

if ans == 'yes':
    print(" 8===)~ ")

root.mainloop()