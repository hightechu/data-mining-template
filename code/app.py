from DTMdescriptions import DTMdescriptions
import pandas as pd
import numpy as np
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn import metrics

def main():
    movie_data = pd.read_csv('../movie_descriptions.csv', header=0)
    movie_label = pd.read_csv('../movie_genres.csv', header=0)
    movie_label=movie_label.values.ravel()

    sentence = "Alice was in the kingdom with her wicked stepmother"

    clf = MultinomialNB(alpha = 0.5, fit_prior = True)
    clf.fit(movie_data, movie_label)
    genre_pred = clf.predict(DTMdescriptions(sentence, movie_data.columns.values).DTM())
    print(genre_pred[0])

if __name__ == '__main__':
    main()
