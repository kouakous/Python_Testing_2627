import threading

import pytest
from werkzeug.serving import make_server

import server


@pytest.fixture
def live_server(monkeypatch, clubs_test, competitions_test):
    monkeypatch.setattr(server, "clubs", clubs_test)
    monkeypatch.setattr(server, "competitions", competitions_test)
    monkeypatch.setattr(server, "bookings", {})
    http_server = make_server("127.0.0.1", 0, server.app)
    thread = threading.Thread(target=http_server.serve_forever, daemon=True)
    thread.start()
    yield f"http://127.0.0.1:{http_server.server_port}"
    http_server.shutdown()


@pytest.fixture
def browser():
    webdriver = pytest.importorskip("selenium.webdriver")
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    try:
        driver = webdriver.Chrome(options=options)
    except Exception:
        pytest.skip("Google Chrome n'est pas disponible sur cette machine")
    yield driver
    driver.quit()
