import requests
for _ in range(10):
    response = requests.get(
        "https://icanhazdadjoke.com/", 
        headers={"Accept": "application/json"},
    )
    json_response = response.json()
    print(json_response)
