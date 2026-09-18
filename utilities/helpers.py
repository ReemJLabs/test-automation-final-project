import re
import allure
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import test_cases.conftest as conf
import utilities.manage_pages as page
from utilities.common_ops import get_data
from page_objects.web_objects.cart_page import cart_icon as cart_icon_locator
from page_objects.web_objects.cart_page import mini_cart_remove_button as mini_cart_locator


class Helpers:
    #Data extraction and helper utilities

    @staticmethod
    @allure.step('Waiting for condition')
    def wait(condition):
        # Wait for a condition with config timeout. Stale nodes are retried until timeout.
        def _ignore_stale(driver):
            try:
                return condition(driver)
            except StaleElementReferenceException:
                return False
        return WebDriverWait(conf.driver, int(get_data('WaitTime'))).until(_ignore_stale)

    @staticmethod
    @allure.step('Hover over cart icon and wait for mini cart to appear')
    def hover_cart_icon():
        #Hover over cart icon and wait for mini-cart to appear
        Helpers.wait(EC.visibility_of_element_located(cart_icon_locator))
        cart_icon = page.web_cart.cart_icon()
        conf.actions.move_to_element(cart_icon).perform()
        Helpers.wait(EC.visibility_of_element_located(mini_cart_locator))

    @staticmethod
    @allure.step('Remove item from cart and wait until it disappears')
    def remove_item_and_wait(button):
        #Click remove button and wait for it to disappear
        button.click()
        Helpers.wait(EC.staleness_of(button))

    @staticmethod
    @allure.step('Get element text')
    def get_element_text(element):
        #Extract text from element and strip whitespace
        if not element:
            return None
        return element.text.strip()

    @staticmethod
    @allure.step('Get element value attribute')
    def get_element_value(element):
        #Extract value attribute from element (for input fields)
        if not element:
            return None
        return element.get_attribute('value')

    @staticmethod
    @allure.step('Check if cart is empty')
    def is_cart_empty():
        #Check if cart is empty. Returns True if empty or can't determine
        try:
            count = Helpers.get_element_text(page.web_cart.get_cart_count_element())
            return count in ['0', '', None]
        except:
            return True

    @staticmethod
    @allure.step('Extract numeric price value from source')
    def extract_price_value(source):
        #Extract numeric price value from element or text string, returns float or None
        if not source:
            return None
        text = source.text.strip() if hasattr(source, 'text') else str(source)
        if not text:
            return None
        price_match = re.search(r'[\d.]+', text.replace(',', ''))
        return float(price_match.group()) if price_match else None

    @staticmethod
    @allure.step('Get all product prices from search results')
    def get_all_product_prices():
        #Get all product prices from the page, returns list of floats
        product_items = page.web_search_results.get_product_items()
        if not product_items:
            raise AssertionError("No product items found on the page")
        prices = []
        for item in product_items:
            price_element = page.web_search_results.get_price_from_product(item)
            if price_element:
                price_value = Helpers.extract_price_value(price_element)
                if price_value is not None:
                    prices.append(price_value)
        if not prices:
            raise AssertionError("Could not extract any valid prices from the page")
        return prices

    @staticmethod
    @allure.step('Get first product price from search results')
    def get_first_product_price():
        #Get the first product's price value, returns float
        first_product = page.web_search_results.get_first_product_item()
        if not first_product:
            raise AssertionError("No product items found on the page")
        price_element = page.web_search_results.get_price_from_product(first_product)
        if not price_element:
            raise AssertionError("Could not find price element for first product")
        price_value = Helpers.extract_price_value(price_element)
        if price_value is None:
            raise AssertionError("Could not extract price from first product")
        return price_value
