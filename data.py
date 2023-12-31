import json

def get_data(file_path):
    """
    This function is used to get data from data.json file.
    It opens the file and handle exceptions in case data cannot be retrieved.
    """
    try:
        f = open(file_path)
        data = json.load(f)
        f.close()
        return data
        
    except FileNotFoundError:
        # This exception checks if the file exists
        return {"error": "This file doesn't exist."}
    except Exception:
        # To handle all other exceptions
        return {"error": "There was a problem retrieving the data from this file."}


def overwrite_data(data, file_path):
    with open(file_path, "w") as f:
        json.dump(data, f)
        f.close()


def add_booking(id, class_date, client_name, data, file_path):
    """ This function is used to add a booking to the file """
    if "bookings" not in data:
        data["bookings"] = {}
    if f"{class_date}" not in data["bookings"]:
        data["bookings"][f"{class_date}"] = {
            "count": 1,
            "clients_list":[
                {"booking_id": id,
                 "client":client_name
                 }
                 ]
                 }
    else:
        data["bookings"][f"{class_date}"]["count"] += 1
        data["bookings"][f"{class_date}"]["clients_list"].append(
            {"booking_id": id,
            "client":client_name
            })
    overwrite_data(data,file_path)