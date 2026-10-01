from tests.pages.login_page import LoginPage
from tests.pages.inventory_page import InventoryPage
from tests.pages.cart_page import CartPage
from tests.pages.checkout_page import CheckoutPage


def test_checkout_parcial(driver):

    driver.get("https://www.saucedemo.com")

    LoginPage(driver).login(
        "standard_user",
        "secret_sauce"
    )

    inventory = InventoryPage(driver)

    inventory.add_product()
    inventory.go_to_cart()

    CartPage(driver).start_checkout()

    checkout = CheckoutPage(driver)

    checkout.fill_form(
        "Douglas",
        "",
        ""
    )

    checkout.continue_checkout()

    assert "Error" in checkout.get_error_message()