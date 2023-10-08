import requests


BASE = "http://127.0.0.1:8000/"
CLASSES = "http://127.0.0.1:8000/classes"
BOOKINGS = "http://127.0.0.1:8000/bookings"


# GET home 
"""response = requests.get(BASE)
print(response.json())"""


# POST classes
"""data={"class_name": "", "capacity": 0, "start_date": "01-01-2024", "end_date": ""}
new_class = requests.post(CLASSES, json=data)
print(new_class.json())"""


# GET classes
"""all_classes = requests.get(CLASSES)
print(all_classes.json())"""


# POST bookings
"""data={"client_name": "Client", "date": "01-01-2024"}
booking = requests.post(BOOKINGS, json=data)
print(booking.json())"""


# GET bookings
"""all_bookings = requests.get(BOOKINGS)
print(all_bookings.json())"""