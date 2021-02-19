# pip install requests

import json
import requests

headers = {'Content-Type': 'application/json'}

api_url = 'https://openlibrary.org/books/OL7353617M.json'

response = requests.get(api_url, headers=headers)

if response.status_code == 200:
    json = json.loads(response.content.decode('utf-8'))
    print(json)
    print(json['number_of_pages'])
    print(json['publishers'])
else:
    print("Failed")