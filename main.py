from flask import	Flask, jsonify

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def index():
    return jsonify({"msssg": "hola"})

@app.route('/data', methods = ['GET'])
def info():
    return jsonify({"data": "Information"})



if __name__ == "__main__":
    
    app.run(debug=True, host='0.0.0.0' , port=4000)