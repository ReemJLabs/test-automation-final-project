from selenium.webdriver.common.by import By

# Product page locators
add_to_cart_button = (By.NAME, "add-to-cart")
product_title = (By.XPATH, "//h1[text()='ATID Green Shoes']")
add_to_cart_message = (By.CSS_SELECTOR, "div.woocommerce-message")


class ProductPage:
    def __init__(self, driver):
        self.driver = driver

    def add_to_cart_button(self):
        return self.driver.find_element(add_to_cart_button[0], add_to_cart_button[1])

    def product_title(self):
        return self.driver.find_element(product_title[0], product_title[1])

    def add_to_cart_message(self):
        return self.driver.find_element(add_to_cart_message[0], add_to_cart_message[1])
