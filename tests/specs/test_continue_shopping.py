from tests.pages.login_page import LoginPage
from tests.pages.inventory_page import InventoryPage
from tests.pages.cart_page import CartPage


def test_continuar_comprando(driver):

    driver.get("https://www.saucedemo.com")

    LoginPage(driver).login(
        "standard_user",
        "secret_sauce"
    )

    inventory = InventoryPage(driver)

    inventory.add_product()
    inventory.go_to_cart()

    cart = CartPage(driver)

    cart.continue_shopping()

    assert "inventory" in driver.current_url