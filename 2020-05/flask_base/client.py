import requests

resp = requests.put("http://0.0.0.0:5000/data", json={"article": "Flask"})
print(resp)
print(resp.json())
