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