import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

movie_data = pd.read_csv('rotten_tomatoes_top_movies.csv')
print(movie_data.head(10))
