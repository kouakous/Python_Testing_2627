import server


def test_tableau_points_trie_les_clubs_par_nom():
    clubs = [
        {"name": "Zeta", "email": "z@club.com", "points": "5"},
        {"name": "Alpha", "email": "a@club.com", "points": "8"},
    ]

    tableau = server.get_points_board(clubs)

    assert [club["name"] for club in tableau] == ["Alpha", "Zeta"]


def test_tableau_points_contient_tous_les_clubs(clubs_test):
    tableau = server.get_points_board(clubs_test)

    assert len(tableau) == len(clubs_test)


def test_tableau_points_ne_modifie_pas_la_liste_d_origine():
    clubs = [
        {"name": "Zeta", "email": "z@club.com", "points": "5"},
        {"name": "Alpha", "email": "a@club.com", "points": "8"},
    ]

    server.get_points_board(clubs)

    assert clubs[0]["name"] == "Zeta"


def test_tableau_points_liste_vide():
    assert server.get_points_board([]) == []
