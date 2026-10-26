def test_tableau_points_accessible_sans_connexion(client):
    response = client.get("/points")

    assert response.status_code == 200
    assert b"Club A" in response.data
    assert b"Club B" in response.data


def test_tableau_points_affiche_les_points(client):
    response = client.get("/points")

    assert b"<td>10</td>" in response.data
    assert b"<td>2</td>" in response.data


def test_accueil_contient_un_lien_vers_le_tableau(client):
    response = client.get("/")

    assert b'href="/points"' in response.data
