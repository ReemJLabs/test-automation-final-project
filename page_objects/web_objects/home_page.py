from selenium.webdriver.common.by import By

# Home page locators
search_input = (By.ID, 'wc-block-search__input-1')
search_button = (By.CSS_SELECTOR, "button[aria-label='Search']")


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def search_input(self):
        return self.driver.find_element(search_input[0], search_input[1])

    def search_button(self):
        return self.driver.find_element(search_button[0], search_button[1])
