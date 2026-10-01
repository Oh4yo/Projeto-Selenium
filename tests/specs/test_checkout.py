from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_compra_produto_com_sucesso(driver):

    driver.get("https://www.saucedemo.com/")

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "user-name"))
    ).send_keys("standard_user")

    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    WebDriverWait(driver, 10).until(
        EC.url_contains("inventory.html")
    )

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.ID, "add-to-cart-sauce-labs-backpack")
        )
    ).click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.CLASS_NAME, "shopping_cart_link")
        )
    ).click()

    WebDriverWait(driver, 10).until(
        EC.url_contains("cart.html")
    )

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.ID, "checkout")
        )
    ).click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.ID, "first-name")
        )
    ).send_keys("Douglas")

    driver.find_element(By.ID, "last-name").send_keys("Teste")
    driver.find_element(By.ID, "postal-code").send_keys("12345")

    driver.find_element(By.ID, "continue").click()

    WebDriverWait(driver, 10).until(
        EC.url_contains("checkout-step-two.html")
    )

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.ID, "finish")
        )
    ).click()

    mensagem = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "complete-header")
        )
    )

    assert "Thank you" in mensagem.text