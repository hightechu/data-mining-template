import pandas as pd
import time
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC
from sklearn import metrics

def main():
    movie_data = pd.read_csv('movie_descriptions.csv', header=0)
    movie_label = pd.read_csv('movie_genres.csv', header=0)
    movie_label=movie_label.values.ravel()
    X_train, X_test, y_train, y_test = train_test_split(movie_data, movie_label, test_size=0.2, random_state=1)

    clf = input("Choose a classifier (type 1,2, or 3 and hit enter): \n(1)Naive Bayes \n(2)Support Vector Machine \n(3)Naive Bayes Support Vector Machine Hybrid \n")
    if clf == '1':
        print("\n Naive Bayes")
        clf = MultinomialNB(alpha = 0.5, fit_prior = True)
        classifcation_acc(clf,X_train, X_test, y_train, y_test)
    elif clf == '2':
        print("\n SVM")
        clf = SVC(C = 0.8)
        classifcation_acc(clf,X_train, X_test, y_train, y_test)
    elif clf == '3':
        print("\n NBSVM")

    # clf2 = MultinomialNB(alpha = 0.5, fit_prior = True)
    # clf3 = MultinomialNB(alpha = 0.5, fit_prior = True)
    # clf4 = MultinomialNB(alpha = 0.5, fit_prior = True)



def classifcation_acc(clf,X_train, X_test, y_train, y_test):
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    acc = metrics.accuracy_score(y_test, y_pred)
    print(acc)

if __name__ == '__main__':
    main()
