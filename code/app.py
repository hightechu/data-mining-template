from DTMdescriptions import DTMdescriptions
import pandas as pd
import numpy as np
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn import metrics
from tkinter import *

# import csvs here

# your code here
# your code here

root = Tk()
root.title("Sci-Fi or Fantasy AI")
instructions = Label(root, text = "Enter a movie description and I will guess if it \
is Sci-Fi or Fantasy")
instructions.pack()
input = Entry(root, width = 100)
input.pack()

def click():
    # your code here
    # your code here 
    genre = Label(root, text = "I think \"" + input.get() + "\" is " + genre_pred[0])
    genre.pack()

button = Button(root, text="Enter", command = click)
button.pack()

root.mainloop()
