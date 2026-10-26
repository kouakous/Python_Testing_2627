import pytest

import server


@pytest.fixture
def clubs_test():
    return [
        {"name": "Club A", "email": "a@club.com", "points": "10"},
        {"name": "Club B", "email": "b@club.com", "points": "2"},
    ]


@pytest.fixture
def competitions_test():
    return [
        {"name": "Compet Future", "date": "2030-06-01 10:00:00",
         "numberOfPlaces": "20"},
        {"name": "Compet Passee", "date": "2020-03-27 10:00:00",
         "numberOfPlaces": "25"},
    ]


@pytest.fixture
def client(monkeypatch, clubs_test, competitions_test):
    monkeypatch.setattr(server, "clubs", clubs_test)
    monkeypatch.setattr(server, "competitions", competitions_test)
    server.app.config["TESTING"] = True
    with server.app.test_client() as client:
        yield client
