# create Flask app
from flask import Flask, request
import pandas as pd
import numpy as np
import pickle

app = Flask(__name__)
classifier = pickle.load(open('classifier.pkl', 'rb'))

@app.route('/')
def welcome():
    return 'Hello Flask'

@app.route('/predict')
def predict_note_authentication():
    variance = request.args.get('variance')
    skewness = request.args.get('skewness')
    curtosis = request.args.get('curtosis')
    entropy = request.args.get('entropy')
    prediction = classifier.predict([[variance, skewness, curtosis, entropy]])
    return f'The predicted value is {str(prediction)}'

@app.route('/predict_file', methods=['POST'])
def predict_note_file():
    df_test = pd.read_csv(request.files.get('file'))
    prediction = classifier.predict(df_test)
    return f'The predicted values for the csv is {str(list(prediction))}'

if __name__=='__main__':
    app.run(debug=True)
