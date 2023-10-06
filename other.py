import requests


BASE = "http://127.0.0.1:8000/"

data={"id": 2, "date": "14-03-2020"}
response = requests.post(BASE + "/bookings", json=data)
print(response.json())