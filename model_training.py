import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle

df = pd.read_csv('BankNoteAuthentication.csv')

# print(df)

X = df.iloc[:, :-1]
y = df.iloc[:, -1]

# print(X.head(5))
# print(y.head(5))


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

# ## Implement Random Forest classifier
classifier = RandomForestClassifier()
classifier.fit(X_train, y_train)

# # Prediction
y_pred = classifier.predict(X_test)

score = accuracy_score(y_test, y_pred)
# print(score)

# ### Create a Pickle file using serialization
classifier = pickle.dump(classifier, open('classifier.pkl', 'wb'))

# print(classifier.predict([[0,1,2,1]]))
