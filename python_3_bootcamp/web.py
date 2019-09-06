import requests

url = "https://www.icanhazdadjoke.com/search"
response = requests.get(url,
    headers={"Accept": "application/json"},
    params={"limit":1,"term":"cat"}
    )

data = response.json()

print(data["results"][0]["joke"])
