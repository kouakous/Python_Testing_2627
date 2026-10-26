def test_book_affiche_la_page_de_reservation(client):
    response = client.get("/book/Compet Future/Club A")

    assert response.status_code == 200
    assert b"Booking for Compet Future" in response.data


def test_book_competition_inconnue(client):
    response = client.get("/book/Compet Inconnue/Club A")

    assert response.status_code == 200
    assert b"Something went wrong-please try again" in response.data


def test_book_club_inconnu(client):
    response = client.get("/book/Compet Future/Club Inconnu")

    assert response.status_code == 200
    assert b"Something went wrong-please try again" in response.data