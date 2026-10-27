from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait


def verifier_texte_affiche(browser, texte):
    try:
        WebDriverWait(browser, 10).until(
            lambda page: texte in page.page_source)
    except TimeoutException:
        contenu = browser.find_element("tag name", "body").text
        raise AssertionError(f"{texte!r} absent de la page :\n{contenu}")


def test_parcours_complet_de_reservation(browser, live_server):
    browser.get(live_server)
    browser.find_element("name", "email").send_keys("a@club.com")
    browser.find_element("tag name", "button").click()
    verifier_texte_affiche(browser, "Welcome, a@club.com")

    browser.find_element("link text", "Book Places").click()
    verifier_texte_affiche(browser, "How many places?")
    browser.find_element("name", "places").send_keys("3")
    browser.find_element("tag name", "button").click()
    verifier_texte_affiche(browser, "3 places booked")
    verifier_texte_affiche(browser, "Points available: 7")

    browser.find_element("link text", "Logout").click()
    verifier_texte_affiche(browser, "GUDLFT Registration Portal")


def test_tableau_des_points_public(browser, live_server):
    browser.get(live_server)

    browser.find_element("link text", "View clubs points").click()

    verifier_texte_affiche(browser, "Clubs points")
    verifier_texte_affiche(browser, "Club A")
    verifier_texte_affiche(browser, "Club B")
