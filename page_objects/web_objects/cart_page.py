from selenium.webdriver.common.by import By

# Cart page locators
cart_icon = (By.CSS_SELECTOR, 'a[href*="cart-2"]')
view_cart_button = (By.CSS_SELECTOR, 'a.wc-forward[href*="cart"]')
cart_item_name = (By.CSS_SELECTOR, 'td.product-name a')
cart_item_price = (By.CSS_SELECTOR, 'td.product-price bdi')
cart_item_quantity = (By.CSS_SELECTOR, 'input.qty')
# Cart clearing locators
all_remove_buttons = (By.CSS_SELECTOR, 'a.remove')
cart_count = (By.CSS_SELECTOR, 'a[href*="cart-2"] .count')
# Mini-cart locators
mini_cart_remove_button = (By.CSS_SELECTOR, '.mini_cart_item a.remove')


class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def cart_icon(self):
        return self.driver.find_element(*cart_icon)

    def view_cart_button(self):
        return self.driver.find_element(*view_cart_button)

    def get_cart_item_name(self):
        return self.driver.find_element(*cart_item_name)

    def get_cart_item_price(self):
        return self.driver.find_element(*cart_item_price)

    def get_cart_item_quantity(self):
        return self.driver.find_element(*cart_item_quantity)

    def get_all_remove_buttons(self):
        return self.driver.find_elements(*all_remove_buttons)

    def get_cart_count_element(self):
        return self.driver.find_element(*cart_count)

    def get_mini_cart_remove_buttons(self):
        return self.driver.find_elements(*mini_cart_remove_button)
