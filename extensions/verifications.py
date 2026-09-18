import allure
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from smart_assertions import verify_expectations, soft_assert
import utilities.manage_pages as page
from utilities.helpers import Helpers
from page_objects.web_objects.product_page import product_title as product_title_locator
from page_objects.web_objects.product_page import add_to_cart_message as message_locator
from page_objects.web_objects.search_results_page import product_item as product_locator
from page_objects.web_objects.search_results_page import results_number as results_locator
from page_objects.web_objects.cart_page import cart_item_name as cart_name_locator
from page_objects.web_objects.cart_page import cart_item_price as cart_price_locator
from page_objects.web_objects.cart_page import cart_item_quantity as cart_qty_locator


class Verifications:
    #All assertion and verification methods

    @staticmethod
    @allure.step('Verifying values are equal')
    def verify_equals(actual, expected):
        #Verify two values are equal
        assert actual == expected, f'Verify Equals Failed, Actual: {actual} is not equal to Expected: {expected}'

    @staticmethod
    @allure.step('Verifying element is displayed')
    def is_displayed(elem: WebElement):
        #Verify element is displayed
        assert elem.is_displayed(), f'Verify is Displayed Failed, Element: {elem.text} is not Displayed'

    @staticmethod
    @allure.step('Verifying number of search results')
    def verify_number_of_results(expected: str):
        #Verify search results count matches expected
        Helpers.wait(EC.visibility_of_element_located(results_locator))
        actual = Helpers.get_element_text(page.web_search_results.showing_results())
        Verifications.verify_equals(actual, expected)

    @staticmethod
    @allure.step('Verifying product page title')
    def verify_product_page_title(expected_title: str):
        #Verify product page title matches expected
        Helpers.wait(EC.visibility_of_element_located(product_title_locator))
        actual = Helpers.get_element_text(page.web_product.product_title())
        Verifications.verify_equals(actual, expected_title)

    @staticmethod
    @allure.step('Verifying add to cart message')
    def verify_add_to_cart_message(expected_message: str):
        #Verify add to cart success message
        Helpers.wait(EC.visibility_of_element_located(message_locator))
        actual = Helpers.get_element_text(page.web_product.add_to_cart_message())
        Verifications.verify_equals(actual, expected_message)

    @staticmethod
    @allure.step('Verifying cart item name')
    def verify_cart_item_name(expected_name: str):
        #Verify cart item name matches expected
        Helpers.wait(EC.visibility_of_element_located(cart_name_locator))
        actual_name = Helpers.get_element_text(page.web_cart.get_cart_item_name())
        Verifications.verify_equals(actual_name, expected_name)

    @staticmethod
    @allure.step('Verifying cart item price')
    def verify_cart_item_price(expected_price_text: str):
        #Verify cart item price matches expected (compares numeric values)
        Helpers.wait(EC.visibility_of_element_located(cart_price_locator))
        actual_price = Helpers.extract_price_value(page.web_cart.get_cart_item_price())
        expected_price = Helpers.extract_price_value(expected_price_text)
        if actual_price is None or expected_price is None:
            raise AssertionError(f"Could not extract price values. Expected: '{expected_price_text}'")
        Verifications.verify_equals(actual_price, expected_price)

    @staticmethod
    @allure.step('Verifying cart item quantity')
    def verify_cart_item_quantity(expected_quantity: str):
        #Verify cart item quantity matches expected
        Helpers.wait(EC.visibility_of_element_located(cart_qty_locator))
        actual_quantity = Helpers.get_element_value(page.web_cart.get_cart_item_quantity())
        Verifications.verify_equals(actual_quantity, expected_quantity)

    @staticmethod
    @allure.step('Verifying first item has highest price')
    def verify_first_item_highest_price():
        #Verify that the first item has the highest price after sorting high to low
        Helpers.wait(EC.presence_of_all_elements_located(product_locator))
        all_prices = Helpers.get_all_product_prices()
        first_price = Helpers.get_first_product_price()
        highest_price = max(all_prices)
        assert first_price == highest_price, \
            f"First item price ({first_price}) is not the highest price ({highest_price}). All prices: {all_prices}"

    @staticmethod
    @allure.step('Soft verifying cart item name')
    def soft_verify_cart_item_name(expected_name: str):
        #Soft assertion for cart item name - allows test to continue if it fails
        Helpers.wait(EC.visibility_of_element_located(cart_name_locator))
        actual_name = Helpers.get_element_text(page.web_cart.get_cart_item_name())
        soft_assert(actual_name == expected_name,
        f'Cart item name verification failed - Actual: {actual_name} is not equal to Expected: {expected_name}')

    @staticmethod
    @allure.step('Soft verifying cart item quantity')
    def soft_verify_cart_item_quantity(expected_quantity: str):
        #Soft assertion for cart item quantity - allows test to continue if it fails
        Helpers.wait(EC.visibility_of_element_located(cart_qty_locator))
        actual_quantity = Helpers.get_element_value(page.web_cart.get_cart_item_quantity())
        soft_assert(actual_quantity == expected_quantity,
        f'Cart item quantity verification failed - Actual: {actual_quantity} is not equal to Expected: {expected_quantity}')

    @staticmethod
    @allure.step('Soft verifying cart item price')
    def soft_verify_cart_item_price(expected_price_text: str):
        #Soft assertion for cart item price - allows test to continue if it fails
        Helpers.wait(EC.visibility_of_element_located(cart_price_locator))
        actual_price = Helpers.extract_price_value(page.web_cart.get_cart_item_price())
        expected_price = Helpers.extract_price_value(expected_price_text)
        if actual_price is None or expected_price is None:
            soft_assert( False, f"Could not extract price values. Expected: '{expected_price_text}'")
        else:
            soft_assert(actual_price == expected_price,
            f'Cart item price verification failed - Actual: {actual_price} is not equal to Expected: {expected_price}')
