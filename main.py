from flask import Flask, request, current_app
from data import get_data, overwrite_data, add_booking
from validation import validate_class, validate_overlapping, validate_booking, check_capacity
import os

app = Flask(__name__)


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
        data = get_data(current_app.config["file_path"])

        # Get posted information
        new_class = validate_class(request.json)
        
        if "error" in new_class:
            return new_class["error"], 400 # Bad request
        
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
                # The id is automatically assigned to the class
                if "class_id" not in data.keys():
                    data["class_id"] = 0
                class_id = data["class_id"]
                data['all_classes'][f"{class_id}"] = new_class
                data['class_id'] += 1

                # Overwrite data.json file to include new data
                overwrite_data(data, current_app.config["file_path"])

                # return the newly added class with rsponse of 201
                return new_class, 201 # Created
            else:
                return {"error": "We could not save this class because it overlaps with existing classes"}, 400
    
    else:
        # if the method is not POST, we just get existing classes
        data = get_data(current_app.config["file_path"])
        if "all_classes" in data.keys() and data['all_classes'] != {}:
            return data['all_classes'], 200 # OK
        # if there is an error getting the data from the file, we return the error
        elif "error" in data.keys():
            return data, 500 # Bad request
        # if there is no error, but there is no key called 'all_classes', we return a message
        else:
            return {"message": "There are no classes to display."}, 200 # OK
        

@app.route("/bookings", methods=["POST", "GET"])
def bookings():
    """
    bookings endpoint, to book a class.
    The bookings are saved in a file called data.json
    """
    if request.method == "POST":
        # Get existing data from data.json
        data = get_data(current_app.config["file_path"])
        if "error" in data.keys():
            return data, 500 # Server error
        elif "all_classes" not in data.keys() or data["all_classes"] == {}:
            return {"message": "There are no classes to book."}, 200 # OK
        else:
            requested_class = request.json

            # check if date was passed
            if "date" in requested_class and "client_name" in requested_class:
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
                        # The id is automatically assigned to the booking
                        if "booking_id" not in data.keys():
                            data["booking_id"] = 0
                        booking_id = data["booking_id"]
                        data["booking_id"] += 1

                        add_booking(booking_id, requested_class["date"], requested_class["client_name"], data, current_app.config["file_path"])
                        return {"message": "Booking confirmed"}, 201 # Created
                    except:
                        return {"There was a problem saving this booking"}, 500 # Server error
            else:
                return {"error": "Please, enter all information (client_name, date)."}, 400 # Bad request

    else:
        # if the method is not POST, we just get existing bookings
        data = get_data(current_app.config["file_path"])
        if "bookings" in data.keys() and data['bookings'] != {}:
            return data['bookings'], 200 # OK
        # if there is an error getting the data from the file, we return the error
        elif "error" in data.keys():
            return data, 500 # Bad request
        # if there is no error, but there is no key called 'bookings', we return a message
        else:
            return {"message": "There are no bookings to display."}, 200 # OK
        

if __name__ == "__main__":
    app.config["file_path"] = "data.json"

    file_path = app.config["file_path"]
    
    if os.path.getsize(file_path) == 0:
        overwrite_data({
            "class_id": 0,
            "booking_id": 0
        }, file_path)

    # debug should be set to False in production, but I will leave it to True for assessment
    app.run(port=8000, debug=True)