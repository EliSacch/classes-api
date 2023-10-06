import json
from main import app

try:
    with open("data.json", "w") as f:
        json.dump({}, f)
        f.close()
except:
    print("There was an error opening the file")


def test_home():
    response = app.test_client().get('/')
    assert response.status_code == 200


def test_can_get_classes():
    response = app.test_client().get('/classes')
    assert response.status_code == 200
    assert response.json['message'] == "There are no classes to display."


def test_can_add_class():
    response = app.test_client().post('/classes', json={"id": 0, "class_name": "Test class", "capacity": 12, "start_date": "01-03-2024", "end_date": "3-03-2024"})
    assert response.status_code == 201


def test_cannot_add_class_with_missing_data():
    response = app.test_client().post('/classes', json={"id": 1, "capacity": 12, "start_date": "01-03-2024", "end_date": "3-03-2024"})
    assert response.status_code == 400
    assert "Mandatory value not provided 'class_name'" in response.json["errors"]


def test_cannot_add_class_with_invalid_date():
    response = app.test_client().post('/classes', json={"id": 1, "class_name": "Test class", "capacity": 12, "start_date": "invalid", "end_date": "3-03-2024"})
    assert response.status_code == 400
    assert "Invalid date passed" in response.json["errors"]


def test_cannot_add_end_date_before_start():
    response = app.test_client().post('/classes', json={"id": 1, "class_name": "Test class2", "capacity": 12, "start_date": "01-03-2023", "end_date": "3-03-2022"})
    assert response.status_code == 400
 

def test_cannot_add_overlapping_class():
    response = app.test_client().post('/classes', json={"id": 1, "class_name": "Test class2", "capacity": 12, "start_date": "01-03-2024", "end_date": "3-03-2024"})
    assert response.status_code == 400
