from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify(
        text='Hello, world',
        id = 'exharo',
        no = 203
    )

application = app