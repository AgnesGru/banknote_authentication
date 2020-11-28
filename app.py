# create Flask app
import pickle
import numpy as np
from flask import Flask, render_template, request

app = Flask(__name__)
classifier = pickle.load(open('classifier.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    int_features = [int(x) for x in request.form.values()]  # dla wszystkich danych z formularza html
    final_features = [np.array(int_features)] # zrób z nich macierz poziomą
    # variance = request.args.get('variance')
    # skewness = request.args.get('skewness')
    # curtosis = request.args.get('curtosis')
    # entropy = request.args.get('entropy')
    # prediction = classifier.predict([[variance, skewness, curtosis, entropy]])
    prediction = classifier.predict(final_features)  # przekazac te dane do klasyfikatora i wywołaj metodę predict
    prediction = round(prediction[0], 0)
    if prediction == 1:
        prediction = 'Bank note'
    else:
        prediction = 'Fake note'

    return render_template("index.html", result='It is a {}'.format(str(prediction)))
    # return f'The predicted value is {str(prediction)}'

# @app.route('/predict_file', methods=['POST'])
# def predict_note_file():
#     df_test = pd.read_csv(request.files.get('file'))
#     prediction = classifier.predict(df_test)
#     return f'The predicted values for the csv is {str(list(prediction))}'


if __name__=='__main__':
    app.run(debug=True)
