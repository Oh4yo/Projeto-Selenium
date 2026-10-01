from tests.pages.login_page import LoginPage
from tests.pages.inventory_page import InventoryPage


def test_ordenar_preco(driver):

    driver.get("https://www.saucedemo.com")

    LoginPage(driver).login(
        "standard_user",
        "secret_sauce"
    )

    InventoryPage(driver).sort_price_low_high()

    assert True


def test_ordenar_nome(driver):

    driver.get("https://www.saucedemo.com")

    LoginPage(driver).login(
        "standard_user",
        "secret_sauce"
    )

    InventoryPage(driver).sort_name_az()

    assert True