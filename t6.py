from tkinter import *

def donothing():
    print("Ok i did it.")

root = Tk()
# ***Main Menu***
menu = Menu()
root.config(menu=menu)

submenu = Menu()
menu.add_cascade(label="File", menu=submenu)
submenu.add_command(label="New Project", command=donothing)
submenu.add_command(label="New...", command=donothing)
submenu.add_separator()
submenu.add_command(label="Quit!", command=quit)

editmenu = Menu()
menu.add_cascade(label="Edit", menu=editmenu)
editmenu.add_command(label="Redo", command=donothing)

# ***Toolbar***
toolbar = Frame(root, bg="Red")

insertButt = Button(toolbar, text="Insert Image", command=donothing)
insertButt.pack(side=LEFT, padx=2, pady=2)
printButt = Button(toolbar, text="Print", command=donothing)
printButt.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X)

# ***Status Bar***

status = Label(root, text="Preparing to do nothing", bd=2, anchor=W, relief=SUNKEN)
status.pack(side=BOTTOM, fill=X)
root.mainloop()