from selenium.webdriver.common.by import By

from .base_page import BasePage


class MenuPage(BasePage):

    MENU = (By.ID, "react-burger-menu-btn")

    LOGOUT = (By.ID, "logout_sidebar_link")

    RESET = (By.ID, "reset_sidebar_link")

    def logout(self):
        self.click(*self.MENU)
        self.click(*self.LOGOUT)

    def reset_app(self):
        self.click(*self.MENU)
        self.click(*self.RESET)