import pytest

import main
from data import overwrite_data


@pytest.fixture()
def app():
    initial_data = {"class_id": 0, "booking_id": 0}
    overwrite_data(initial_data, "tests/test_data.json")
    print("CLEARING test_data")
    app = main.app
    app.config["file_path"] = "tests/test_data.json"

    yield app


@pytest.fixture()
def client(app):
    return app.test_client()