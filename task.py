import requests
import json
response_API = requests.get('https://api.postalpincode.in/pincode/110001')
# print(response_API.status_code)
data = response_API.text
print(response_API.json)
Name = data[1]["Name"]

# parse_json = json.loads(data)
# print(parse_json)
# BranchType= parse_json[0]['name']
print(Name +" | ")