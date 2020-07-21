### Classifiers
Classifiers are different formulas that you can use to classify data. In the case of this project the data is the movie description and the classification is either sci-fi or fantasy. Luckily [Sklearn](https://scikit-learn.org/stable/) has some existing function that do the calculations for you; However, you are going to be providing the values that the function will use to perform the calculation. By changing the values, the classifier will have a different accuracy (how often it guesses the correct genre for a given description), and your goal is to find the highest accuracy possible!
### Naive Bayes
Naive Bayes is a mathematical formula that calculates probability. Check out [this quick review](https://www.youtube.com/embed/O2L2Uv9pdDA?start=454&end=530) to get a basic understanding. In the video the classication is either **"normal"** mail or **"spam"** mail - you can think of this as the equivalent of the sci-fi or fantasy labels. Feel free to watch the whole video, but this section gives a surface level explanation to how this formula works and it's only 3 minutes long!
![naivebayes](https://user-images.githubusercontent.com/45152371/87989535-09b5c000-ca97-11ea-8cfe-c30b6180cf84.png)

## Time to start coding!
Open up your project in a text-editor and navigate to the "code folder". In there you'll find a Python file called "test_classifiers.py". That's where the action happens. You can see the first section already has some code.
```python
...
def main():
    movie_data = pd.read_csv('../movie_descriptions.csv', header=0)
    movie_label = pd.read_csv('../movie_genres.csv', header=0)
    movie_label=movie_label.values.ravel()
...
```
This reads a csv file (the files that contain the data) and turns it into a structure that Python will be able to interpret. If you want, you can open the csv files in excel or google sheets and take a look at how they looked originally. You'll notice that movie_descriptions.csv is a very large file with words at the top as the headers and numbers filling in the rows and columns. This is because the file is a record of how many times each word occurs in a given description. This format is called a **document term matrix** and looks like this:
![Screen Shot 2020-07-20 at 4 21 25 PM](https://user-images.githubusercontent.com/45152371/87995705-14775180-caa5-11ea-9508-4b09b8369274.png)

## Training and Testing
To start, you'll split your data into a training and test set. You do this because you need to **"train"** your machine to understand patterns, just like you would study key terms to memorize them for a test. The **test set** is used to see how accurate your trained machine is on new data that it hasn't seen before. This would be like taking a test at school and getting your grade back.

You're lucky again because Sklearn has a method that splits the data for you: [`train_test_split`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html)
```python
# X_train, X_test, y_train, y_test = train_test_split(<data>, <label>, <percentage of data used for testing>, random_state=1)
X_train, X_test, y_train, y_test = train_test_split(movie_data, movie_label, test_size=0.2, random_state=1)
```
- [ ] Add a line of code that splits your data into a training and a testing set

you can change the `<percentage of data used for testing>` but in general, the training set should be larger than the test set.
- [ ] Run the program in command line to check for errors. Make sure you're in the code folder of your project directory and run:
```sh
> python3 test_classifiers.py
```
## Your First Classifier!
This is the exciting part, you're going to start seeing how accurate your classifier is! There is an if/elif/else statement in the `main()` for your benefit. When you run your program you can choose one of the 3 classifiers you're going to test. If you let all run at could take quite some time because the dataset has around 2000 examples and they have to calculate with all that information. If you run your program and nothing happens for a bit, be patient, it's probably just calculating!

- [ ] Add a [Multinomial Naive Bayes](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.MultinomialNB.html?highlight=multinomial%20bayes#sklearn.naive_bayes.MultinomialNB) classifier from sklearn under the first `if` statement:
```python
    if clf == '1':
        print(Naive Bayes")
        clf = MultinomialNB(alpha = 0.5, fit_prior = True) # your code
        classifcation_acc(clf,X_train, X_test, y_train, y_test)
```
 - [ ] Run the program in command line to check for errors and see your first accuracy!. Make sure you're in the code folder of your project directory and run:
```sh
> python3 test_classifiers.py
```
The **alpha** value can be set from anything between 0 and 1
- [ ] Try different alpha values and see which gives the highest accuracy

The **fit_prior** can be True or False
- [ ] Try changing the fit_prior and see which gives the highest accuracy

- [ ] When you think you have the highest accuracy you can get, create a [pull request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request)
