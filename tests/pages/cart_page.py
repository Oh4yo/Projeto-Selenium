from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage


class CartPage(BasePage):

    CHECKOUT = (By.ID, "checkout")
    REMOVE = (By.ID, "remove-sauce-labs-backpack")
    CONTINUE_SHOPPING = (By.ID, "continue-shopping")
    CART_ITEM = (By.CLASS_NAME, "cart_item")

    def start_checkout(self):
        self.click(*self.CHECKOUT)

    def remove_item(self):
        self.click(*self.REMOVE)

    def continue_shopping(self):
        self.click(*self.CONTINUE_SHOPPING)

    def has_items(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, "cart_contents_container")
            )
        )

        return len(
            self.driver.find_elements(*self.CART_ITEM)
        )