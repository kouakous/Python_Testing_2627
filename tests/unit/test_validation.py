import server


def test_parse_places_nombres_valides():
    assert server.parse_places("5") == 5
    assert server.parse_places("0") == 0
    assert server.parse_places("10") == 10


def test_parse_places_nombres_invalides():
    assert server.parse_places("abc") is None
    assert server.parse_places("10.5") is None
    assert server.parse_places("") is None
