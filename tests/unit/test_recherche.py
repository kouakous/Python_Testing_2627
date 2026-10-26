import server


def test_email_connu_renvoie_le_club():
    clubs = [
        {"name": "Club A", "email": "a@club.com", "points": "10"},
        {"name": "Club B", "email": "b@club.com", "points": "2"},
    ]

    resultat = server.get_club_by_email("b@club.com", clubs)

    assert resultat["name"] == "Club B"


def test_email_inconnu_renvoie_none():
    clubs = [
        {"name": "Club A", "email": "a@club.com", "points": "10"},
    ]

    resultat = server.get_club_by_email("inconnu@club.com", clubs)

    assert resultat is None


def test_nom_competition_connu_renvoie_la_competition():
    competitions = [
        {"name": "Competition A", "date": "2020-03-27 10:00:00",
         "numberOfPlaces": "10"},
        {"name": "Competition B", "date": "2020-03-28 09:00:00",
         "numberOfPlaces": "20"},
    ]

    resultat = server.get_competition_by_name("Competition B", competitions)

    assert resultat["name"] == "Competition B"


def test_nom_competition_inconnu_renvoie_none():
    competitions = [
        {"name": "Competition A", "date": "2020-03-27 10:00:00",
         "numberOfPlaces": "10"},
    ]

    resultat = server.get_competition_by_name("Competition C", competitions)

    assert resultat is None


def test_nom_club_connu_renvoie_le_club():
    clubs = [
        {"name": "Club A", "email": "a@club.com", "points": "10"},
        {"name": "Club B", "email": "b@club.com", "points": "2"},
    ]

    resultat = server.get_club_by_name("Club B", clubs)

    assert resultat["name"] == "Club B"


def test_nom_club_inconnu_renvoie_none():
    clubs = [
        {"name": "Club A", "email": "a@club.com", "points": "10"},
    ]

    resultat = server.get_club_by_name("Club C", clubs)

    assert resultat is None


def test_email_liste_vide_renvoie_none():
    assert server.get_club_by_email("a@club.com", []) is None


def test_nom_club_liste_vide_renvoie_none():
    assert server.get_club_by_name("Club A", []) is None


def test_nom_competition_liste_vide_renvoie_none():
    assert server.get_competition_by_name("Compet Future", []) is None
