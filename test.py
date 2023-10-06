import requests


BASE = "http://127.0.0.1:8000/"

data={"id": 2, "class_name": "Zumba", "capacity": 12, "start_date": "01-01-2024", "end_date": "31-01-2024"}
response = requests.post(BASE + "/classes", json=data)
print(response.json())