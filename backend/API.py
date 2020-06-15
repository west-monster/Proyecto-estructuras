from flask_cors import CORS
from flask import Flask, request
from flask import jsonify
app = Flask(__name__)
from datasql import *
CORS(app)
@app.route('/seeAll', methods=["GET"])
def seAllF():
    return getAllAPI(request.args['first'],request.args['last'])

@app.route('/search', methods=["GET"])
def searchF():
    return searchAPI(request.args['target'])

@app.route('/delete', methods=["POST"])
def deleteF():
    ids = request.get_json()['targets']

    for id in ids:
        deleteAPI(id)
    return '1'

@app.route('/deleteAll', methods=["DELETE"])
def deleteAllF():
    deleteAllAPI()
    return '1'
@app.route('/edit', methods=["POST"])
def editF():
    editAPI(request.get_json()['target'])
    return '1'