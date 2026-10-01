from tests.pages.login_page import LoginPage


def test_login_credenciais_invalidas(driver):

    driver.get("https://www.saucedemo.com")

    page = LoginPage(driver)

    page.login(
        "usuario_invalido",
        "senha_invalida"
    )

    assert (
        "Username and password do not match"
        in page.get_error_message()
    )