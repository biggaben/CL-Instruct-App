import requests

url = 'http://localhost:5000/generate-code'
payload = {'prompt': 'Hello there! Who are you?'}
response = requests.post(url, json=payload)

print(response.json())