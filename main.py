from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
app = Flask(__name__)
model = pickle.load(open('Linear_regression_model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


@app.route("/predict", methods=['POST'])
def predict():

    if request.method == 'POST':
        hr = float(request.form['hr'])
        if hr<=24:
            prediction=model.predict([[hr]])
            return render_template('index.html',prediction_text=prediction)
        else:
            warning1="Please check number of hour you insert"
            return render_template('index.html',warn_text=warning1)
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)