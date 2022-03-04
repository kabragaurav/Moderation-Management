import requests
import json
import sys

def pretty_print_response(response):
  json_data = response.json()
  json_data = json.dumps(json_data)         # convert to str
  json_object = json.loads(json_data)
  json_formatted_str = json.dumps(json_object, indent=2)
  print(json_formatted_str)
  print("\n ############################################ \n")

# TODO : try except

if __name__ == '__main__':
  photo = sys.argv[1]

  # First of all Heroku has read-only file system. So you can't upload anything directly to heroku. 
  # Use something like Amazon S3 to keep files.
  request_url = 'https://projectmoderation.herokuapp.com/detect-labels?image_name=' + photo
  response = requests.get(request_url)

  pretty_print_response(response)
