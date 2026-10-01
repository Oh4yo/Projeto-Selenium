from selenium.webdriver.common.by import By
from .base_page import BasePage


class LoginPage(BasePage):

    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    def login(self, user, password):
        self.type(*self.USERNAME, user)
        self.type(*self.PASSWORD, password)
        self.click(*self.LOGIN_BTN)

    def get_error_message(self):
        return self.get_text(*self.ERROR_MESSAGE)