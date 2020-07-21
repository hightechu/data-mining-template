from DTMdescriptions import DTMdescriptions
import pandas as pd
import numpy as np
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn import metrics
from tkinter import *

movie_data = pd.read_csv('../movie_descriptions.csv', header=0)
movie_label = pd.read_csv('../movie_genres.csv', header=0)
movie_label=movie_label.values.ravel()

clf = MultinomialNB(alpha = 0.5, fit_prior = True)
clf.fit(movie_data, movie_label)

root = Tk()
root.title("Sci-Fi or Fantasy AI")
instructions = Label(root, text = "Enter a movie description and I will guess if it \
is Sci-Fi or Fantasy")
instructions.pack()
input = Entry(root, width = 100)
input.pack()

def click():
    description = DTMdescriptions(input.get(), movie_data.columns.values).DTM()
    genre_pred = clf.predict(description)
    genre = Label(root, text = "I think \"" + input.get() + "\" is " + genre_pred[0])
    genre.pack()

button = Button(root, text="Enter", command = click)
button.pack()

root.mainloop()
