import requests

response = requests.get('http://127.0.0.1:8000/api/vets_list')

json_respnose = response.json()

print(json_respnose)