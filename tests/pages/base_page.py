from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find(self, by, value):
        return WebDriverWait(
            self.driver,
            10,
            ignored_exceptions=[StaleElementReferenceException]
        ).until(
            EC.presence_of_element_located((by, value))
        )

    def click(self, by, value):
        WebDriverWait(
            self.driver,
            10,
            ignored_exceptions=[StaleElementReferenceException]
        ).until(
            EC.element_to_be_clickable((by, value))
        ).click()

    def type(self, by, value, text):
        element = WebDriverWait(
            self.driver,
            10,
            ignored_exceptions=[StaleElementReferenceException]
        ).until(
            EC.visibility_of_element_located((by, value))
        )

        element.clear()
        element.send_keys(text)

    def get_text(self, by, value):
        return WebDriverWait(
            self.driver,
            10,
            ignored_exceptions=[StaleElementReferenceException]
        ).until(
            EC.visibility_of_element_located((by, value))
        ).text