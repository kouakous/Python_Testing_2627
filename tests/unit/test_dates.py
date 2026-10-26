import server


def test_is_past_date_passee():
    competition = {"name": "Compet", "date": "2020-03-27 10:00:00",
                   "numberOfPlaces": "20"}

    assert server.is_past(competition)


def test_is_past_date_future():
    competition = {"name": "Compet", "date": "2030-06-01 10:00:00",
                   "numberOfPlaces": "20"}

    assert not server.is_past(competition)
