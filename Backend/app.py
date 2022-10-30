import json
from flask import Flask, jsonify
import requests
import mysql.connector
from flask_cors import CORS

mydb = mysql.connector.connect(
  host="db",
  port=3306,
  user="brayan",
  password="colocolo",
  database='t1'
)

app = Flask(__name__)
CORS(app)

url = 'https://www.freetogame.com/api/games'
data = requests.get(url)
data = data.json()

app.secret_key = 'esto-es-una-clave-muy-secreta'

@app.route("/")
def index():
    return jsonify({"name": "pong"})

@app.route('/nombres', methods=['GET'])
def name():
    return jsonify({"name": "Brayan Espina Tramolao"})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)