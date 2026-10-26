import server


def test_load_clubs_renvoie_des_clubs_complets():
    clubs = server.loadClubs()

    assert len(clubs) > 0
    for club in clubs:
        assert "name" in club and "email" in club and "points" in club


def test_load_competitions_renvoie_des_competitions_completes():
    competitions = server.loadCompetitions()

    assert len(competitions) > 0
    for competition in competitions:
        assert "name" in competition and "date" in competition
        assert "numberOfPlaces" in competition


def test_chargement_fonctionne_depuis_un_autre_dossier(monkeypatch, tmp_path):
    monkeypatch.chdir(tmp_path)

    assert len(server.loadClubs()) > 0
    assert len(server.loadCompetitions()) > 0
