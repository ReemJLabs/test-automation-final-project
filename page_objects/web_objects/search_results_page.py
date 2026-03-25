from selenium.webdriver.common.by import By

filter_field = (By.NAME, 'orderby')
results_number = (By.CSS_SELECTOR, 'p.woocommerce-result-count')
find_item = (By.XPATH, "//h2[contains(text(),'ATID Green Shoes')]")
product_item = (By.CSS_SELECTOR, 'li.product')
product_price = (By.CSS_SELECTOR, 'span.price bdi')


class SearchResultPage:
    def __init__(self, driver):
        self.driver = driver

    def filter_settings(self):
        return self.driver.find_element(*filter_field)

    def showing_results(self):
        return self.driver.find_element(*results_number)

    def select_item(self):
        return self.driver.find_element(*find_item)

    def get_product_items(self):
        return self.driver.find_elements(*product_item)

    def get_first_product_item(self):
        product_items = self.get_product_items()
        return product_items[0] if product_items else None

    def get_price_from_product(self, product_item):
        prices = product_item.find_elements(*product_price)
        return prices[-1] if prices else None

    def get_all_price_elements_from_product(self, product_item):
        return product_item.find_elements(*product_price)
