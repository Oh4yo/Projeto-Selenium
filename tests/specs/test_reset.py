from tests.pages.login_page import LoginPage
from tests.pages.inventory_page import InventoryPage
from tests.pages.menu_page import MenuPage
from tests.pages.cart_page import CartPage


def test_reset_app(driver):

    driver.get("https://www.saucedemo.com")

    LoginPage(driver).login(
        "standard_user",
        "secret_sauce"
    )

    inventory = InventoryPage(driver)

    inventory.add_product()

    MenuPage(driver).reset_app()

    inventory.go_to_cart()

    assert CartPage(driver).has_items() == 0