import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from sklearn import metrics
from sklearn.metrics import balanced_accuracy_score

def main():
    # convert csv files to pandas dataframes
    movie_data = pd.read_csv('../movie_descriptions.csv', header=0)
    movie_label = pd.read_csv('../movie_genres.csv', header=0)
    movie_label=movie_label.values.ravel()
    # Split data into 20% test set and 80% train set
    X_train, X_test, y_train, y_test = train_test_split(movie_data, movie_label, test_size=0.2, random_state=1)

    clf = input("Choose a classifier (type 1,2, or 3 and hit enter): \n(1)Naive Bayes \n(2)Support Vector Machine \n(3)Neural Network \n")

    if clf == '1':
        print("Naive Bayes")
        clf = MultinomialNB(alpha = 0.5, fit_prior = True)
        classifcation_acc(clf,X_train, X_test, y_train, y_test)

    elif clf == '2':
        print("SVM")
        clf = SVC(C = 1.5, kernel = 'rbf', degree = 4, gamma = 'scale')
        classifcation_acc(clf,X_train, X_test, y_train, y_test)

    else:
        print("Neural Network")
        clf = MLPClassifier(hidden_layer_sizes=(80,), activation = 'tanh',
            alpha = 0.0005, learning_rate_init = 2)
        classifcation_acc(clf,X_train, X_test, y_train, y_test)

# uses the data to train a classifier using the training set(fit())
# makes a prediction on the testing set (predict())
# Calculates the accuracy (balanced_accuracy_score())
def classifcation_acc(clf,X_train, X_test, y_train, y_test):
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    acc = balanced_accuracy_score(y_test, y_pred)
    print(acc)


if __name__ == '__main__':
    main()
