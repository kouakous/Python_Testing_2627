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
