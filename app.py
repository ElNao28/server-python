from flask import Flask, request, render_template, jsonify
import joblib
import pandas as pd
import logging
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input

app = Flask(__name__)

def create_model():
    model = Sequential()
    model.add(Input(shape=([5])))
    model.add(Dense(64, activation='relu'))
    model.add(Dense(32, activation='relu'))
    model.add(Dense(8, activation='relu'))
    model.add(Dense(1))
    model.compile(loss='mean_squared_error', optimizer='adam')
    return model

# Configurar el registro
logging.basicConfig(level=logging.DEBUG)

# Cargar el modelo entrenado
model = joblib.load('modeloSc.pkl')
app.logger.debug('Modelo cargado correctamente.')

@app.route('/')
def home():
    return render_template('formulario.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        #Obtener los datos enviados en el request
        AST = 2.0
        CHE = 4
        ALP = 7.6
        ALT = 8.8
        ALL = 32

        #AST = float(request.form['AST'])
        #CHE = int(request.form['CHE'])
        #ALP = float(request.form['ALP'])
        #ALT = float(request.form['ALT'])
        #ALL = int(request.form['ALL'])
        
        # Crear un DataFrame con los datos
        data_df = pd.DataFrame([[AST, CHE, ALP, ALT, ALL]], columns=['Engine Size(L)', 'Cylinders', 'Consumption Hwy (L/100 km)', 'Fuel Consumption Comb (L/100 km)', 'Fuel Consumption Comb (mpg)'])
        app.logger.debug(f'DataFrame creado: {data_df}')
        
        # Realizar predicciones
        prediction = model.predict(data_df)
        app.logger.debug(f'Predicción: {prediction[0]}')
        
        # Convertir la predicción a un tipo de dato adecuado para la respuesta
        predicted_value = prediction  # Asumimos que prediction[0] es un array de un solo elemento
        
        # Devolver las predicciones como respuesta JSON
        print(f"la predicciones {predicted_value}")
        return jsonify({'categoria': float(predicted_value)})  # Convertir a float para JSON
    except Exception as e:
        app.logger.error(f'Error en la predicción: {str(e)}')
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
