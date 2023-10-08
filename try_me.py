import requests


BASE = "http://127.0.0.1:8000/"
CLASSES = "http://127.0.0.1:8000/classes"
BOOKINGS = "http://127.0.0.1:8000/bookings"


# GET home 
response = requests.get(BASE)
def run_get_home():
    print(response.json())


# POST classes
def run_post_class(data):
    new_class = requests.post(CLASSES, json=data)
    print(new_class.json())


# GET classes
def run_get_all_classes():
    all_classes = requests.get(CLASSES)
    print(all_classes.json())


# POST bookings
def run_post_booking(data):
    booking = requests.post(BOOKINGS, json=data)
    print(booking.json())


# GET bookings
def run_get_all_bookings():
    all_bookings = requests.get(BOOKINGS)
    print(all_bookings.json())


""" Uncomment the method you want to try """

run_get_home()


# data = data={"class_name": "", "capacity": 0, "start_date": "01-01-2024", "end_date": ""}
# run_post_class(data)


# run_get_all_classes()


# data={"client_name": "Client", "date": "01-01-2024"}
# run_post_booking(data)


# run_get_all_bookings()