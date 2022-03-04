import flask
from flask import request
import csv
import boto3


app = flask.Flask(__name__)

with open('./aws_credentials.csv', 'r') as f:
  next(f)   # go to next row
  reader = csv.reader(f)
  for line in reader:
    access_key_id = line[0]
    secret_access_key = line[1]

client = boto3.client('rekognition', 
                      aws_access_key_id=access_key_id, 
                      aws_secret_access_key=secret_access_key,
                      region_name='us-west-2')


@app.route('/', methods=['GET'])
def home():
    img_bytes = request.args['arg1']
    return client.detect_labels(Image={ 'Bytes': img_bytes })