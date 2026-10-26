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


def test_validate_booking_plus_de_12_places():
    resultat = server.validate_booking(make_club(30), make_competition(20), 13)

    assert resultat == "You cannot book more than 12 places in a competition."


def test_validate_booking_exactement_12_places():
    resultat = server.validate_booking(make_club(30), make_competition(20), 12)

    assert resultat is None


def test_validate_booking_cumul_au_dela_de_12_places():
    resultat = server.validate_booking(make_club(30), make_competition(20), 3,
                                       already_booked=10)

    assert resultat == "You cannot book more than 12 places in a competition."


def test_validate_booking_cumul_exactement_12_places():
    resultat = server.validate_booking(make_club(30), make_competition(20), 2,
                                       already_booked=10)

    assert resultat is None


def test_validate_booking_competition_complete():
    resultat = server.validate_booking(make_club(10), make_competition(0), 1)

    assert resultat == "This competition is full."


def test_validate_booking_places_insuffisantes():
    resultat = server.validate_booking(make_club(10), make_competition(2), 3)

    assert resultat == "Not enough places available in this competition."


def test_validate_booking_prend_exactement_les_places_restantes():
    resultat = server.validate_booking(make_club(10), make_competition(3), 3)

    assert resultat is None


def test_parse_places_accepte_un_nombre_negatif():
    assert server.parse_places("-5") == -5


def test_parse_places_ignore_les_espaces():
    assert server.parse_places(" 3 ") == 3


def test_validate_booking_zero_place():
    resultat = server.validate_booking(make_club(10), make_competition(20), 0)

    assert resultat == "Please enter a positive number of places."


def test_validate_booking_nombre_negatif():
    resultat = server.validate_booking(make_club(10), make_competition(20), -5)

    assert resultat == "Please enter a positive number of places."


def test_parse_places_espace_seul():
    assert server.parse_places(" ") is None


def test_validate_booking_competition_passee():
    competition = make_competition(20, "2020-03-27 10:00:00")

    resultat = server.validate_booking(make_club(10), competition, 3)

    assert resultat == "This competition is already over."
