from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def acessar(self):
        self.driver.get("https://www.saucedemo.com/")

    def preencher_usuario(self, usuario):
        self.driver.find_element(By.ID, "username").send_keys(usuario)

    def preencher_senha(self, senha):
        self.driver.find_element(By.ID, "password").send_keys(senha)

    def clicar_login(self):
        self.driver.find_element(By.ID, "login").click()