from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage


class InventoryPage(BasePage):

    ADD_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART = (By.CLASS_NAME, "shopping_cart_link")
    SORT = (By.CLASS_NAME, "product_sort_container")

    def add_product(self):
        self.click(*self.ADD_BACKPACK)

    def go_to_cart(self):
        self.click(*self.CART)

    def sort_price_low_high(self):
        dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.SORT)
        )

        Select(dropdown).select_by_value("lohi")

    def sort_name_az(self):
        dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.SORT)
        )

        Select(dropdown).select_by_value("az")