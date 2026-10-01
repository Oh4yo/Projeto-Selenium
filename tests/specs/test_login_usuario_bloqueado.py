from tests.pages.login_page import LoginPage


def test_login_usuario_bloqueado(driver):

    driver.get("https://www.saucedemo.com")

    page = LoginPage(driver)

    page.login(
        "locked_out_user",
        "secret_sauce"
    )

    assert (
        "Sorry, this user has been locked out"
        in page.get_error_message()
    )