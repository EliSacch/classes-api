import json
from main import app

try:
    with open("data.json", "w") as f:
        json.dump({}, f)
        f.close()
except:
    print("There was an error opening the file")


# Home
def test_home():
    response = app.test_client().get('/')
    assert response.status_code == 200


# Test classes when there is no data yet
def test_can_get_classes():
    response = app.test_client().get('/classes')
    assert response.status_code == 200
    assert response.json['message'] == "There are no classes to display."


# Test booking where there is no data
def test_cannot_book_with_no_classes():
    response = app.test_client().post('/bookings/', json={"id": 0, "date": "01-01-2023"})
    assert response.status_code == 200
    assert response.json['message'] == "There are no classes to book."


# Test class creation
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


# Test bookings when there is at least one class
def test_can_book_class_with_valid_date():
    response = app.test_client().post('/bookings/', json={"id": 0, "date": "01-03-2024"})
    assert response.status_code == 201


def test_cannot_book_class_for_a_date_with_no_classes():
    response = app.test_client().post('/bookings/', json={"id": 1, "date": "01-03-2029"})
    assert response.status_code == 400
    assert response.json['error'] == "Please, choose a valid date."


def test_cannot_book_class_with_invalid_date_format():
    response = app.test_client().post('/bookings/', json={"id": 1, "date": "01/01"})
    assert response.status_code == 400


def test_class_count():
    response = app.test_client().post('/bookings/', json={"id": 0, "date": "01-03-2024"})
    assert response.status_code == 201
    try:
        f = open("data.json")
        data = json.load(f)
        f.close()
    except Exception:
        print("There was an error opening the file")
    assert data["bookings"]["01-03-2024"] == 2
    