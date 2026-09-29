from tests.pages.login_page import LoginPage


class LoginTransaction:
    def __init__(self, driver):
        self.page = LoginPage(driver)

    def realizar_login(self, usuario, senha):
        self.page.acessar()
        self.page.preencher_usuario(usuario)
        self.page.preencher_senha(senha)
        self.page.clicar_login()