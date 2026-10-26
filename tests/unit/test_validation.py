import server


def make_club(points):
    return {"name": "Club A", "email": "a@club.com", "points": str(points)}


def make_competition(places, date="2030-06-01 10:00:00"):
    return {"name": "Compet", "date": date, "numberOfPlaces": str(places)}


def test_parse_places_nombres_valides():
    assert server.parse_places("5") == 5
    assert server.parse_places("0") == 0
    assert server.parse_places("10") == 10


def test_parse_places_nombres_invalides():
    assert server.parse_places("abc") is None
    assert server.parse_places("10.5") is None
    assert server.parse_places("") is None


def test_validate_booking_reservation_valide():
    resultat = server.validate_booking(make_club(10), make_competition(20), 3)

    assert resultat is None


def test_validate_booking_points_insuffisants():
    resultat = server.validate_booking(make_club(2), make_competition(20), 3)

    assert resultat == "You do not have enough points."


def test_validate_booking_utilise_exactement_tous_les_points():
    resultat = server.validate_booking(make_club(3), make_competition(20), 3)

    assert resultat is None


def test_validate_booking_une_seule_place():
    resultat = server.validate_booking(make_club(1), make_competition(20), 1)

    assert resultat is None
