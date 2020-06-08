from flask_cors import CORS
from flask import Flask
app = Flask(__name__)
from datasql import *
CORS(app)
@app.route('/showall')
def hello_world():
    getAll(0,1)
    return



    