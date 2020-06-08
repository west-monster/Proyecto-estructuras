from flask_cors import CORS
from flask import Flask
app = Flask(__name__)
from datasql import *
CORS(app)
@app.route('/showall')
def hello_world():
    return getAll(0,25);

    