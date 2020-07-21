## Classifier  Number 2: Support Vector Machines
The purpose of support vector machines is to find a line that best separates the data based on their classifcation, in this case Sci-Fi and Fantasy. Checkout another fun stat quest clearly explained video for [Support Vector Machines](https://www.youtube.com/embed/efR1C6CvhmE?start=42&end=405) to learn a little bit more.
![SorFSVM](https://user-images.githubusercontent.com/45152371/87999447-b2701980-caaf-11ea-8bb5-716b31025ba8.png)

## Building Your Support Vector Machine
It's that time again - time to create another awesome classifier!
- [ ] Use the [SVC (Support Vector Classification)](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html) from sklearn below the `elif` in your code/test_classifiers.py file:
```python
...
    elif clf == '2':
        print("SVM")
        clf = SVC(C = 1.5, kernel = 'rbf', degree = 4, gamma = 'scale')# your code
        classifcation_acc(clf,X_train, X_test, y_train, y_test)
...
```
- [ ] Run the program in command line to check for errors and see your first accuracy!. Make sure you're in the code folder of your project directory and run:
```sh
> python3 test_classifiers.py
```
As you can see, this classifier has many possible parameters and if you got to [sklearn documentation](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html) you can add even more.
But to start try different values for these parameters and try to achieve the highest accuracy you can
- [ ] Change the *C* value - it can be any positive number
- [ ] Try different *kernels* - it can be one of 'linear', 'poly', 'rbf', 'sigmoid', or 'precomputed'
- [ ] Experiment with *degree* values - they can be any integer
- [ ] Change the *gamma* parameter - it can be 'scale', or  'auto'

- [ ] Once you think you have found the highest accuracy you can for this classifier, create a [pull request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request)
