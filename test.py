import requests


BASE = "http://127.0.0.1:8000/"

data={"id": 1, "class_name": "Pilates", "capacity": 10, "start_date": "01-10-2023", "end_date": "31-10-2023"}
response = requests.post("http://127.0.0.1:8000/classes", json=data)
print(response.json())