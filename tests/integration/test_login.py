def test_email_connu_affiche_la_page_welcome(client):
    response = client.post("/showSummary", data={"email": "a@club.com"})

    assert response.status_code == 200
    assert b"Welcome, a@club.com" in response.data


def test_email_inconnu_affiche_un_message_erreur(client):
    response = client.post("/showSummary", data={"email": "inconnu@club.com"})

    assert response.status_code == 200
    assert b"Sorry, this email is not registered." in response.data


def test_competition_complete_affiche_un_message(client):
    response = client.post("/showSummary", data={"email": "a@club.com"})

    assert b"Competition full" in response.data
