import requests
for _ in range(10):
    response = requests.get(
        "https://icanhazdadjoke.com/", 
        headers={"Accept": "application/json"}, # telling what output from https://icanhazdadjoke.com/ we want
    )
    json_response = response.json()   # asking api for a JSON response
    joke = json_response['joke']
    print(joke) # printing response
