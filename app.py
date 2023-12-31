from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

with open('house_prediction_model.pkl', 'rb') as file:
    model = pickle.load(file)

#instagram.in/page

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/login')
def login():
    return render_template('login.html')
@app.route("/predict", methods=['POST', 'GET'])
def predict():
    bed = int(request.form['bed'])
    bath = int(request.form['bath'])
    loc = int(request.form['loc'])
    size = int(request.form['size'])
    status = int(request.form['status'])
    face = int(request.form['face'])
    Type = int(request.form['Type'])

    input_data = np.array([[bed, bath, loc, size, status, face, Type]])
    prediction = model.predict(input_data)[0]
    return render_template('index.html', prediction=prediction)
if __name__ == 'main':
    app.run()
