import server


def test_get_booked_places_sans_reservation():
    assert server.get_booked_places({}, "Compet", "Club A") == 0


def test_get_booked_places_avec_reservation():
    bookings = {("Compet", "Club A"): 5}

    assert server.get_booked_places(bookings, "Compet", "Club A") == 5


def test_record_booking_premiere_reservation():
    bookings = {}

    server.record_booking(bookings, "Compet", "Club A", 4)

    assert bookings == {("Compet", "Club A"): 4}


def test_record_booking_additionne_les_reservations():
    bookings = {("Compet", "Club A"): 4}

    server.record_booking(bookings, "Compet", "Club A", 3)

    assert bookings == {("Compet", "Club A"): 7}


def test_get_booked_places_autre_club():
    bookings = {("Compet", "Club A"): 5}

    assert server.get_booked_places(bookings, "Compet", "Club B") == 0


def test_get_booked_places_autre_competition():
    bookings = {("Compet", "Club A"): 5}

    assert server.get_booked_places(bookings, "Autre", "Club A") == 0


def test_record_booking_separe_les_clubs():
    bookings = {}

    server.record_booking(bookings, "Compet", "Club A", 4)
    server.record_booking(bookings, "Compet", "Club B", 2)

    assert bookings == {("Compet", "Club A"): 4, ("Compet", "Club B"): 2}
