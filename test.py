import requests


BASE = "http://127.0.0.1:8000/"

data={"id": 2, "client_name": "client4", "date": "3-03-2024"}
response = requests.post(BASE + "/bookings", json=data)
print(response.json())