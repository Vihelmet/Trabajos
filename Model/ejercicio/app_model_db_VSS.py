from flask import Flask, request, jsonify
import os
import pickle
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression
import pandas as pd
import sqlite3


os.chdir(os.path.dirname(__file__))

app = Flask(__name__)
app.config['DEBUG'] = True

model = pickle.load(open('data/advertising_model', 'rb'))
data = pd.read_csv('data/Advertising.csv')

@app.route("/", methods=['GET'])
def hello():
    return "Bienvenido a mi API del modelo advertising"

@app.route('/v2/predict', methods=['GET'])

def predict_sales():
    
    advertising = request.json

    prediction = model.predict([list(advertising.values())])

    return jsonify({'prediction': prediction[0]})

@app.route('/v2/ingest_data', methods=['POST'])

def ingest_data():
    
    new_data = request.json
    
    data = data.append(new_data, ignore_index=True)
    data.to_csv('data/Advertising.csv', index=False)

    return jsonify({'message': 'Datos incluidos con éxito'})

@app.route('/v2/retrain', methods=['PUT'])

def retrain_model():
    # Obtener todos los datos de la base de datos
    all_data = pd.read_csv('data/Advertising.csv')

    # Separar los datos en características (X) y variable objetivo (y)
    X = all_data.drop('sales', axis=1)
    y = all_data['sales']

    # Entrenar un nuevo modelo
    model = LinearRegression()
    model.fit(X, y)

    # Guardar el nuevo modelo entrenado
    pickle.dump(model, open('model.pkl', 'wb'))

    return jsonify({'message': 'Nuevo modelo entrenado con éxito'})
app.run()

