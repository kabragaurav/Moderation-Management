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
                      region_name='us-east-2')


@app.route('/detect-labels', methods=['GET'])
def detect_labels_service():
    img_name = request.args['image_name']
    return client.detect_labels(Image={ 'S3Object': {
        'Bucket' : 'moderationbkt',
        'Name' : img_name
    } } )

@app.route('/detect_moderation_labels', methods=['GET'])
def detect_moderation_labels_service():
    img_name = request.args['image_name']
    return client.detect_moderation_labels(Image={ 'S3Object': {
        'Bucket' : 'moderationbkt',
        'Name' : img_name
    } } )

@app.route('/detect_protective_equipment', methods=['GET'])
def detect_protective_equipment_service():
    img_name = request.args['image_name']
    return client.detect_protective_equipment(Image={ 'S3Object': {
        'Bucket' : 'moderationbkt',
        'Name' : img_name
    } } )

@app.route('/detect_text', methods=['GET'])
def detect_text_service():
    img_name = request.args['image_name']
    return client.detect_text(Image={ 'S3Object': {
        'Bucket' : 'moderationbkt',
        'Name' : img_name
    } } )

@app.route('/detect_faces', methods=['GET'])
def detect_faces_service():
    img_name = request.args['image_name']
    return client.detect_faces(Image={ 'S3Object': {
        'Bucket' : 'moderationbkt',
        'Name' : img_name
    } } )


@app.route('/recognize_celebrities', methods=['GET'])
def recognize_celebrities_service():
    img_name = request.args['image_name']
    return client.recognize_celebrities(Image={ 'S3Object': {
        'Bucket' : 'moderationbkt',
        'Name' : img_name
    } } )

