#Use the template below to get started
import requests
import json

url = "https://api.nationalize.io/?name=nathaniel"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
else:
    print(f"Error code: {response.status_code}")
name = data['name']
print(name)