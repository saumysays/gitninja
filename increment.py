import requests

url = "https://github.com/thisissamridh"

for i in range(100):
    response = requests.get(url)
    print(f"Response code for visit {i+1}: {response.status_code}")