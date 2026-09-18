import allure
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
import test_cases.conftest as conf
from extensions.ui_actions import UiActions
import utilities.manage_pages as page
from utilities.common_ops import get_data
from utilities.helpers import Helpers
from page_objects.web_objects.cart_page import cart_icon as cart_icon_locator
from page_objects.web_objects.cart_page import view_cart_button as view_cart_locator
from page_objects.web_objects.search_results_page import results_number as results_locator
from page_objects.web_objects.search_results_page import find_item as find_item_locator
from page_objects.web_objects.search_results_page import filter_field as filter_locator


class WebFlows:
    # User action flows - sequences of user interactions

    @staticmethod
    @allure.step('Searching for an item')
    def home_page_flow(product_name: str):
        # Search for a product from home page
        UiActions.update_text(page.web_home.search_input(), product_name)
        UiActions.click(page.web_home.search_button())
        Helpers.wait(EC.visibility_of_element_located(results_locator))

    @staticmethod
    @allure.step('Applying price filter on search results')
    def search_result_flow(filter_value: str):
        # Apply filter on search results page. WooCommerce can rebuild the dropdown after search.
        last_error = None
        for _ in range(3):
            try:
                Helpers.wait(EC.element_to_be_clickable(filter_locator))
                UiActions.select_from_droplist(page.web_search_results.filter_settings(), filter_value)
                return
            except StaleElementReferenceException as error:
                last_error = error
        raise last_error

    @staticmethod
    @allure.step('Selecting item from search results')
    def item_select():
        # Select an item from search results
        Helpers.wait(EC.element_to_be_clickable(find_item_locator))
        UiActions.click(page.web_search_results.select_item())

    @staticmethod
    @allure.step('Adding product to basket')
    def add_to_basket():
        # Add current product to basket
        UiActions.click(page.web_product.add_to_cart_button())

    @staticmethod
    @allure.step('Navigating to cart page')
    def navigate_to_cart():
        # Navigate to cart page by hovering over cart icon and clicking VIEW CART
        Helpers.wait(EC.visibility_of_element_located(cart_icon_locator))
        cart_icon = page.web_cart.cart_icon()
        conf.actions.move_to_element(cart_icon).perform()
        Helpers.wait(EC.visibility_of_element_located(view_cart_locator))
        UiActions.click(page.web_cart.view_cart_button())
        Helpers.wait(EC.url_contains('cart'))
        assert 'cart' in conf.driver.current_url, "Failed to navigate to cart page"

    @staticmethod
    @allure.step('Navigating to store home page')
    def store_home_page():
        # Navigate back to store home page
        conf.driver.get(get_data('Url'))

    @staticmethod
    @allure.step('Clearing cart via cart page')
    def clear_cart():
        # Remove all items from cart (navigates to cart page)
        if Helpers.is_cart_empty():
            return
        try:
            WebFlows.navigate_to_cart()
            while True:
                buttons = page.web_cart.get_all_remove_buttons()
                if not buttons:
                    break
                Helpers.remove_item_and_wait(buttons[0])
        except Exception:
            pass  # Teardown must not fail the test if the cart is already empty
        conf.driver.get(get_data('Url'))

    @staticmethod
    @allure.step('Clearing cart via mini-cart')
    def clear_cart_mini():
        # Remove all items from cart using mini-cart dropdown (no page navigation)
        if Helpers.is_cart_empty():
            return
        try:
            Helpers.hover_cart_icon()
            while True:
                buttons = page.web_cart.get_mini_cart_remove_buttons()
                if not buttons:
                    break
                Helpers.remove_item_and_wait(buttons[0])
                Helpers.hover_cart_icon()
        except Exception:
            pass  # Teardown must not fail the test if the cart is already empty
