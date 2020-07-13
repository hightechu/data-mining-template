from tkinter import *

class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("Machine Learning In Python")
        self.minsize(640, 400)

root = Root()
root.mainloop()
