#Imports
from flask import Flask, jsonify
from data import products, Rutas

#Instancia
app = Flask(__name__)


#Rutas
@app.route('/', methods=['GET'])
def index():
    response = jsonify({"information": Rutas})
    return response


@app.route('/data', methods=['GET'])
def all_data():
    return jsonify({"data": products})


@app.route('/data/{id}', methods=['GET'])
def data_by_id():
    return jsonify({"data": "Information"})


@app.route('/create', methods=['POST'])
def create_data():
    return jsonify({"data": "Information"})


@app.route('/modify/{id}', methods=['patch'])
def update_data():
    return jsonify({"data": "Information"})


#Punto de entrada
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=4000)
