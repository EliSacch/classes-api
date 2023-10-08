def test_can_get_classes(client):
    response = client.get('/classes')
    assert response.status_code == 200


def test_can_add_class(client):
    response = client.post('/classes', json={"class_name": "Test class", "capacity": 2, "start_date": "01-05-2029", "end_date": "3-05-2029"})
    assert response.status_code == 201


def test_cannot_add_class_with_missing_data(client):
    response = client.post('/classes', json={"capacity": 12, "start_date": "01-03-2024", "end_date": "3-03-2024"})
    assert response.status_code == 400
    assert "Mandatory value not provided 'class_name'" in response.json["errors"]


def test_cannot_add_class_with_invalid_capacity(client):
    response = client.post('/classes', json={"class_name": "Test class", "capacity": "invalid", "start_date": "01-04-2024", "end_date": "3-04-2024"})
    assert response.status_code == 400


def test_cannot_add_class_with_negative_or_zero_capacity(client):
    response = client.post('/classes', json={"class_name": "Test class", "capacity": 0, "start_date": "01-04-2024", "end_date": "3-04-2024"})
    assert response.status_code == 400


def test_cannot_add_class_with_invalid_date(client):
    response = client.post('/classes', json={"class_name": "Test class", "capacity": 2, "start_date": "invalid", "end_date": "3-03-2024"})
    assert response.status_code == 400
    assert "Invalid date passed" in response.json["errors"]


def test_cannot_add_end_date_before_start(client):
    response = client.post('/classes', json={"class_name": "Test class2", "capacity": 2, "start_date": "01-03-2023", "end_date": "3-03-2022"})
    assert response.status_code == 400
 

def test_cannot_add_overlapping_class(client):
    class_1 = client.post('/classes', json={"class_name": "Class 1", "capacity": 2, "start_date": "01-03-2024", "end_date": "3-03-2024"})
    assert class_1.status_code == 201
    response = client.post('/classes', json={"class_name": "Class 2", "capacity": 2, "start_date": "01-03-2024", "end_date": "3-03-2024"})
    assert response.status_code == 400
