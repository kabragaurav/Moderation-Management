import requests
import json
import base64

def pretty_print_response(json_data):
  json_data = json.dumps(json_data)
  json_object = json.loads(json_data)
  json_formatted_str = json.dumps(json_object, indent=2)
  print(json_formatted_str)

photo = input('Enter path:')

# with open(photo, 'rb') as img:
#     # img_bytes = img.read()
#     base64_image=base64.b64encode(img.read())
#     base_64_binary = base64.decodebytes(base64_image)

# print(img_bytes)

# First of all Heroku has read-only file system. So you can't upload anything directly to heroku. Use something like Amazon S3 to keep files.
uri = 'https://projectmoderation.herokuapp.com/?image_name=' + photo
response = requests.get(uri)

# print(pretty_print_response(response))
print(response.json())
pretty_print_response(response.json())
