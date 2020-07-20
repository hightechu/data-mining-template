from tkinter import *

root = Tk()
e = Entry(root, width = 50)
e.pack()

def click():
    label = Label(root, text = "Genre:" + e.get())
    label.pack()
    return label

button = Button(root, text="Enter", command = click)
button.pack()

root.mainloop()
