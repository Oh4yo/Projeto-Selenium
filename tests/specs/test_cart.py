from tests.pages.login_page import LoginPage
from tests.pages.inventory_page import InventoryPage
from tests.pages.cart_page import CartPage


def test_adicionar_item_carrinho(driver):

    driver.get("https://www.saucedemo.com")

    LoginPage(driver).login(
        "standard_user",
        "secret_sauce"
    )

    inventory = InventoryPage(driver)

    inventory.add_product()
    inventory.go_to_cart()

    assert CartPage(driver).has_items() == 1


def test_remover_item_carrinho(driver):

    driver.get("https://www.saucedemo.com")

    LoginPage(driver).login(
        "standard_user",
        "secret_sauce"
    )

    inventory = InventoryPage(driver)

    inventory.add_product()
    inventory.go_to_cart()

    cart = CartPage(driver)

    cart.remove_item()

    assert cart.has_items() == 0


def test_carrinho_vazio(driver):

    driver.get("https://www.saucedemo.com")

    LoginPage(driver).login(
        "standard_user",
        "secret_sauce"
    )

    InventoryPage(driver).go_to_cart()

    assert CartPage(driver).has_items() == 0