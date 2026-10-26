def test_purchase_places_texte(client):
    response = client.post("/purchasePlaces", data={
        "competition": "Compet Future",
        "club": "Club A",
        "places": "abc",
    })

    assert response.status_code == 200
    assert b"Please enter a valid number of places." in response.data


def test_purchase_places_vide(client):
    response = client.post("/purchasePlaces", data={
        "competition": "Compet Future",
        "club": "Club A",
        "places": "",
    })

    assert response.status_code == 200
    assert b"Please enter a valid number of places." in response.data


def test_purchase_deduit_les_points(client, clubs_test):
    client.post("/purchasePlaces", data={
        "competition": "Compet Future",
        "club": "Club A",
        "places": "3",
    })

    assert int(clubs_test[0]["points"]) == 7


def test_purchase_deduit_les_places(client, competitions_test):
    client.post("/purchasePlaces", data={
        "competition": "Compet Future",
        "club": "Club A",
        "places": "3",
    })

    assert int(competitions_test[0]["numberOfPlaces"]) == 17


def test_purchase_message_indique_le_nombre_de_places(client):
    response = client.post("/purchasePlaces", data={
        "competition": "Compet Future",
        "club": "Club A",
        "places": "3",
    })

    assert b"3 places booked" in response.data


def test_purchase_club_inconnu(client):
    response = client.post("/purchasePlaces", data={
        "competition": "Compet Future",
        "club": "Club Inconnu",
        "places": "3",
    })

    assert response.status_code == 200
    assert b"Something went wrong-please try again" in response.data


def test_purchase_competition_inconnue(client):
    response = client.post("/purchasePlaces", data={
        "competition": "Compet Inconnue",
        "club": "Club A",
        "places": "3",
    })

    assert response.status_code == 200
    assert b"Something went wrong-please try again" in response.data


def test_purchase_refuse_si_points_insuffisants(client, clubs_test):
    response = client.post("/purchasePlaces", data={
        "competition": "Compet Future",
        "club": "Club B",
        "places": "5",
    })

    assert b"You do not have enough points." in response.data
    assert int(clubs_test[1]["points"]) == 2
