### Classifier Number 3: Neural Networks
Of all machine learning techniques, you may have heard of this one. When many people think of Artificial intelligence, they often think of computers trying to emulate human intelligence. Human behaviour is a result of [neurons](https://www.brainfacts.org/brain-anatomy-and-function/anatomy/2012/the-neuron) transmitting information throughout the nervous system. Neural networks are named after them because their structure is inspired by the human nervous system. Check out [this video](https://www.youtube.com/watch?v=bfmFfD2RIcg) to learn more.
![nn](https://user-images.githubusercontent.com/45152371/88002517-8eb0d180-cab7-11ea-8163-a53190d72899.png)
### Creating Your Neural Network
It may be no surprise to you that sklearn has a neural network class.
- [ ] Add a neural network after the `else:` in code/test_classifiers.py
```python
...
    elif clf == '3':
        print("Neural Network")
        clf = MLPClassifier(hidden_layer_sizes=(80,), activation = 'tanh',
            alpha = 0.0005, learning_rate_init = 0.005)
        classifcation_acc(clf,X_train, X_test, y_train, y_test)
...
```
- [ ] Run your code to see the accuracy and test for errors:
```sh
> python3 test_classifiers.py
```
This classifier also has a lot of parameters. Start with the one's in the code above and try out others from the [sklearn docs](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html#sklearn.neural_network.MLPClassifier) if you want!
- [ ] hidden_layer_sizes - can be any positive integer in the format (100,)
- [ ] activation - can be 'identity', 'logistic', 'tanh', 'relu'
- [ ] alpha - positive number (keep it small)
- [ ] learning_rate_init - positive number (keep it small)

- [ ] Once you think you have found the highest accuracy you can for this classifier, create a [pull request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request)
