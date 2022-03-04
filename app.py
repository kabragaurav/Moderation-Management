import flask
from flask import request


app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    img_bytes = request.args['arg1']
    return 'Hello World ' + str(type(img_bytes)) + " " + str(img_bytes)