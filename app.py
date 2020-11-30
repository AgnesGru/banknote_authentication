# create Flask app
import pickle
import numpy as np
from flask import Flask, render_template, request

app = Flask(__name__)
classifier = pickle.load(open('classifier.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')
    # return "Hello Docker"


@app.route('/predict', methods=['POST'])
def predict():
    int_features = [int(x) for x in request.form.values()]  # dla wszystkich danych z formularza html
    final_features = [np.array(int_features)]  # zrób z nich macierz poziomą
    prediction = classifier.predict(final_features)  # przekazac te dane do klasyfikatora i wywołaj metodę predict
    prediction = round(prediction[0], 0)
    if prediction == 1:
        prediction = 'Bank note'
    else:
        prediction = 'Fake note'

    return render_template("index.html", result='It is a {}'.format(str(prediction)))


if __name__ == '__main__':
    app.run()
