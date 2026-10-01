from tests.pages.login_page import LoginPage
from tests.pages.menu_page import MenuPage


def test_logout(driver):

    driver.get("https://www.saucedemo.com")

    LoginPage(driver).login(
        "standard_user",
        "secret_sauce"
    )

    MenuPage(driver).logout()

    assert "saucedemo" in driver.current_url