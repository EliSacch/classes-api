from flask import Flask, request, jsonify
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
        # Get posted information
        new_class = request.json
        id = new_class['id']

        # Get existing data from data.json
        data = get_data()

        # If there is an error in the file, do not submit the new data
        if "error" in data.keys():
            return data
        
        else:
            # first check that "all_classes exist", or create it
            if "all_classes" not in data.keys():
                data['all_classes'] = {}

            # Then add the new_class
            data['all_classes'][f"{id}"] = new_class
            # Overwrite data.json file to include new data
            with open("data.json", "w") as f:
                json.dump(data, f)
                f.close()

            # return the newly added class with rsponse of 201
            return new_class, 201
    
    else:
        # if the method is not POST, we just get existing classes
        data = get_data()
        if "all_classes" in data.keys() and data['all_classes'] != {}:
            return data['all_classes']
        # if there is an error getting the data from the file, we return the error
        elif "error" in data.keys():
            return data
        # if there is no error, but there is no key called 'all_classes', we return a message
        else:
            return {"message": "There are no classes to display."}
        

if __name__ == "__main__":
    app.run(port=8000, debug=True)