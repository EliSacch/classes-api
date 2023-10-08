def test_can_book_class_with_valid_date_and_name(client):
    client.post('/classes', json={"class_name": "Zumba", "capacity": 10, "start_date": "01-03-2024", "end_date": "15-03-2024"})
    response = client.post('/bookings', json={"client_name": "client", "date": "01-03-2024"})
    assert response.status_code == 201


def test_cannot_book_class_with_no_client_name(client):
    client.post('/classes', json={"class_name": "Zumba", "capacity": 10, "start_date": "01-03-2024", "end_date": "15-03-2024"})
    response = client.post('/bookings', json={"date": "01-03-2024"})
    assert response.status_code == 400


def test_cannot_book_class_for_a_date_with_no_classes(client):
    client.post('/classes', json={"class_name": "Zumba", "capacity": 10, "start_date": "01-03-2024", "end_date": "15-03-2024"})
    response = client.post('/bookings', json={"client_name": "client", "date": "01-05-2029"})
    assert response.status_code == 400
    assert response.json['error'] == "Please, choose a valid date."


def test_cannot_book_class_with_invalid_date_format(client):
    client.post('/classes', json={"class_name": "Zumba", "capacity": 10, "start_date": "01-03-2024", "end_date": "15-03-2024"})
    response = client.post('/bookings', json={"client_name": "client", "date": "01/03"})
    assert response.status_code == 400


def test_cannot_book_class_over_capacity(client):
    client.post('/classes', json={"class_name": "Zumba", "capacity": 1, "start_date": "01-03-2024", "end_date": "15-03-2024"})
    first_booking = client.post('/bookings', json={"client_name": "Client 1", "date": "01-03-2024"})
    assert first_booking.status_code == 201
    second_booking = client.post('/bookings', json={"client_name": "Client 1", "date": "01-03-2024"})
    assert second_booking.status_code == 400
    