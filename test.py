import requests


BASE = "http://127.0.0.1:8000/"

data={"id": 0, "class_name": "Pilates", "capacity": 10, "start_date": "22-10-2023", "end_date": "1-12-2023"}
response = requests.post(BASE + "/classes", json=data)
print(response.json())