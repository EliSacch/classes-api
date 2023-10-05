from flask import Flask, request, jsonify
import json


app = Flask(__name__)


@app.route("/")
def home():
    """This is the home"""
    return {"message": "Welcome!"}


@app.route("/classes", methods=["POST", "GET"])
def classes():
    """Classes endpoint, to show existig classes
    and create new ones.
    The classes are saved in a file called data.json"""
    if request.method == "POST":
        # get posted information
        new_class = request.json
        id = new_class['id']

        # get existing data from data.json
        f = open("data.json")
        data = json.load(f)
        gym_classes = data["gym_classes"]

        # add new class to existing classes
        gym_classes[f"{id}"] = new_class

        # overwrite data.json file to include new data
        with open("data.json", "w") as f:
            json.dump(data, f)
            f.close()
        # return the newly added class with rsponse of 201
        return new_class, 201
    
    else:
        # if the method is not POST, we just get existing classes
        f = open("data.json")
        data = json.load(f)
        gym_classes = data["gym_classes"]
        f.close()
        # If there is no existing class we return a message
        return gym_classes if gym_classes != {} else {"message": "There are no classes yet"}, 200
    

if __name__ == "__main__":
    app.run(port=8000, debug=True)