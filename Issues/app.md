### Your Best Classifier
At this point, you've tested out 3 (or more) machine learning algorithms and achieved the best accuracy you could find with each one! Now, choose the one that had the highest overall accuracy and you will use that one to make your app in `app.py`.

- [ ] Start by reading in the data from the csv files just as in test_classifiers

```python
movie_data = pd.read_csv('../movie_descriptions.csv', header=0)
movie_label = pd.read_csv('../movie_genres.csv', header=0)
movie_label=movie_label.values.ravel()
```  
This time, you don't have to split your data into testing and training set because you already know the performance of your classifier.

- [ ] Copy and paste your best classifier from test_classifier.py (note that my example below is not necessarily the best)

```python
clf = MultinomialNB(alpha = 0.5, fit_prior = True)
```
- [ ] **Train** your machine using the [`fit()`](https://scikit-learn.org/stable/developers/develop.html) method from sklearn
```python
clf.fit(movie_data, movie_label)
```
### User Interface
Right now there is a super simple user interface interface with just a prompt, an input box and a button. You need to take the input from the box and let the classifier decide if it is sci-fi or fantasy. Since the data that you used to train your classifier was in the form of a Document Term Matrix (DTM), it expects another sample of the same shape to classify. For this reason, you will first use the `DTM()` function from the *DTMdescription* class in the same folder with your sentence. You don't need to work in this file, but you're welcome to take a look at it and read the comments to see kind of how it works. The `DTM ()` function will return a DTM version of your sentence with the same words as the original training set as the headings. Reminder of what a DTM looks like:
![Screen Shot 2020-07-20 at 4 21 25 PM](https://user-images.githubusercontent.com/45152371/87995705-14775180-caa5-11ea-9508-4b09b8369274.png)
- [ ] in the `click()` function in `app.py` set description = to the DTM version of the input
```python
...
def click():
    description = DTMdescriptions(input.get(), movie_data.columns.values).DTM() # your code
    # this line will be next
    genre = Label(root, text = "I think \"" + input.get() + "\" is " + genre_pred[0])
    genre.pack()
...
```
- [ ] Next, give your new description to the trained classifier to predict whether it is sci-fi or fantasy using (no surprise here) sklearn's `predict()` function

```python
...
def click():
    description = DTMdescriptions(input.get(), movie_data.columns.values).DTM()
    genre_pred = clf.predict(description) # your code
    genre = Label(root, text = "I think \"" + input.get() + "\" is " + genre_pred[0])
    genre.pack()
...
```
- [ ] Run app.py and try out your awesome new AI app!
```sh
> python3 app.py
```
- [ ] Once you're satisfied with your work, create a [pull request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request)
