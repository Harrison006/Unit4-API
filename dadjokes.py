import requests

response = requests.get('https://icanhazdadjoke.com/')

print(response.json)