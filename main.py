from flask import Flask, request
from validation import validate_class, validate_overlapping, validate_booking

import json


app = Flask(__name__)


def get_data():
    """
    This function is used to get data from data.json file.
    It opens the file and handle exceptions in case data cannot be retrieved.
    """
    try:
        f = open("data.json")
        data = json.load(f)
        f.close()
        return data
        
    except FileNotFoundError:
        # This exception checks if the file exists
        return {"error": "This file doesn't exist."}
    except Exception:
        # To handle all other exceptions
        return {"error": "There was a problem retrieving the data from this file."}
    

def check_capacity(class_date, data, class_capacity):
    """ This function is used to check if the bookings have reached the availability for a class
    in a specific date """
    available = True
    if "bookings" in data and class_date in data["bookings"]:
        booked = data["bookings"][f"{class_date}"]
        available = booked < class_capacity
    
    return available

    

def add_booking(class_date, data):
    """ This function is used to add a booking to the file """
    if "bookings" not in data:
        data["bookings"] = {}
    if f"{class_date}" not in data["bookings"]:
        data["bookings"][f"{class_date}"] = 1
    else:
        data["bookings"][f"{class_date}"] += 1
    with open("data.json", "w") as f:
        json.dump(data, f)
        f.close()


@app.route("/")
def home():
    """ This is the home """
    return {"message": "Welcome!"}


@app.route("/classes", methods=["POST", "GET"])
def classes():
    """
    Classes endpoint, to show existig classes
    and create new ones.
    The classes are saved in a file called data.json
    """
    if request.method == "POST":
        # Get existing data from data.json
        data = get_data()

        # Get posted information
        new_class = validate_class(request.json)
        
        if "error" in new_class:
            return new_class["error"], 400 # Bad request
        else:
            id = new_class['id']
        
        # If there is an error in the file, do not submit the new data
        if "error" in data.keys():
            return data, 500 # Server error
        else:
            # first check that "all_classes exist", or create it
            if "all_classes" not in data.keys():
                data['all_classes'] = {}

        if 'error' not in new_class and 'error' not in data.keys():

            # Check if there is an overlapping class
            is_overlapping = validate_overlapping(new_class, data['all_classes'])

            if is_overlapping == False:
                # Then add the new_class
                data['all_classes'][f"{id}"] = new_class
                # Overwrite data.json file to include new data
                with open("data.json", "w") as f:
                    json.dump(data, f)
                    f.close()

                # return the newly added class with rsponse of 201
                return new_class, 201 # Created
            else:
                return {"error": "We could not save this class because it overlaps with existing classes"}, 400
    
    else:
        # if the method is not POST, we just get existing classes
        data = get_data()
        if "all_classes" in data.keys() and data['all_classes'] != {}:
            return data['all_classes'], 200 # OK
        # if there is an error getting the data from the file, we return the error
        elif "error" in data.keys():
            return data, 500 # Bad request
        # if there is no error, but there is no key called 'all_classes', we return a message
        else:
            return {"message": "There are no classes to display."}, 200 # OK
        

@app.route("/bookings/", methods=["POST", "GET"])
def bookings():
    """
    bookings endpoint, to book a class.
    The bookings are saved in a file called data.json
    """
    if request.method == "POST":
        # Get existing data from data.json
        data = get_data()
        if "error" in data.keys():
            return data, 500 # Server error
        elif "all_classes" not in data.keys() or data["all_classes"] == {}:
            return {"message": "There are no classes to book."}, 200 # OK
        else:
            requested_class = request.json

            # check if date was passed
            if "date" in requested_class:
                check_booking = validate_booking(requested_class["date"], data["all_classes"])
                valid_booking = check_booking[0]
                class_capacity = check_booking[1]

                is_available = check_capacity(requested_class["date"], data, class_capacity)
                
                if valid_booking == False:
                    return {"error": "Please, choose a valid date."}, 400 # Bad request
                elif is_available == False:
                    return {"error": "Sorry, this class is full."}, 400 # Bad request
                else:
                    try:
                        add_booking(requested_class["date"], data)
                        return {"message": "Booking confirmed"}, 201 # Created
                    except:
                        return {"There was a problem saving this booking"}, 500 # Server error

            else:
                return {"error": "Please, choose a date."}, 400 # Bad request

    else:
        return {"meggage": "Book a class"}, 200 # OK

        

if __name__ == "__main__":
    app.run(port=8000, debug=True)