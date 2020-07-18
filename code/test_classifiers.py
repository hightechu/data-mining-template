import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from sklearn import metrics
from sklearn.metrics import balanced_accuracy_score

def main():
    movie_data = pd.read_csv('../movie_descriptions.csv', header=0)
    movie_label = pd.read_csv('../movie_genres.csv', header=0)
    movie_label=movie_label.values.ravel()
    X_train, X_test, y_train, y_test = train_test_split(movie_data, movie_label, test_size=0.2, random_state=1)

    clf = input("Choose a classifier (type 1,2, or 3 and hit enter): \n(1)Naive Bayes \n(2)Support Vector Machine \n(3)Neural Network \n")

    if clf == '1':
        print("\n Naive Bayes")
        clf = MultinomialNB(alpha = 0.5, fit_prior = True)
        classifcation_acc(clf,X_train, X_test, y_train, y_test)
        single_class(clf,X_train, X_test, y_train, y_test)

    elif clf == '2':
        print("\n SVM")
        clf = SVC(C = 0.8)
        classifcation_acc(clf,X_train, X_test, y_train, y_test)

    elif clf == '3':
        print("\n Neural Network")
        clf = MLPClassifier(random_state=1, max_iter=300)
        classifcation_acc(clf,X_train, X_test, y_train, y_test)

def classifcation_acc(clf,X_train, X_test, y_train, y_test):
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    acc = balanced_accuracy_score(y_test, y_pred)
    print(acc)

def single_class(clf,X_train, X_test, y_train, y_test):
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test.iloc[[0]])
    print(y_test[0])
    print(y_pred)

if __name__ == '__main__':
    main()
