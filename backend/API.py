from flask_cors import CORS
from flask import Flask
app = Flask(__name__)
CORS(app)
@app.route('/showall')
def hello_world():
    return {
        "username": 1,
        "theme": 1,
        "image": 1,
    }

    