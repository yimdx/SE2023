import requests
import json

url = "http://127.0.0.1:3000/admin/login"
headers = {"Content-Type": "application/json"}
data = {
    "username": "admin",
    "password": "_qwe123"
}

response = requests.post(url, headers=headers, data=json.dumps(data))

print(response.status_code)
print(response)