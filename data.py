import json

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
    

def overwrite_data(data):
    with open("data.json", "w") as f:
        json.dump(data, f)
        f.close()


def add_booking(class_date, client_name, data):
    """ This function is used to add a booking to the file """
    if "bookings" not in data:
        data["bookings"] = {}
    if f"{class_date}" not in data["bookings"]:
        data["bookings"][f"{class_date}"] = [client_name]
    else:
        data["bookings"][f"{class_date}"].append(client_name)
    overwrite_data(data)