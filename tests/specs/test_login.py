from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login_com_sucesso(driver):

    # Dado que o usuário acessa a página de login
    driver.get("https://www.saucedemo.com/")

    # Quando informa usuário e senha válidos
    campo_usuario = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "user-name"))
    )
    campo_usuario.send_keys("standard_user")

    campo_senha = driver.find_element(By.ID, "password")
    campo_senha.send_keys("secret_sauce")

    # E clica no botão Login
    botao_login = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "login-button"))
    )
    botao_login.click()

    # Então deve ser redirecionado para a página de produtos
    WebDriverWait(driver, 10).until(EC.url_contains("inventory.html"))

    assert "inventory.html" in driver.current_url

    titulo = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "title"))
    )

    assert titulo.text == "Products"
