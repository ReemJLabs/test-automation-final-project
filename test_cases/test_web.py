from time import sleep
import allure
import pytest
from utilities.common_ops import get_data
from workflows.web_flows import WebFlows
from extensions.verifications import Verifications
from smart_assertions import verify_expectations


@pytest.mark.usefixtures('init_web_driver')
class Test_Web:

    # Test Case 1
    @allure.title('Test01: Verify item add')
    @allure.description('This test verifies a successful search for an item and adding it to the cart')
    def test_adding_product(self):
        WebFlows.home_page_flow(get_data('ProductName'))
        Verifications.verify_number_of_results(get_data('ExpectedResults'))
        WebFlows.item_select()
        Verifications.verify_product_page_title(get_data('ProductTitle'))
        WebFlows.add_to_basket()
        Verifications.verify_add_to_cart_message(get_data('CartMessage'))


    # Test Case 2
    @allure.title('Test02: Verify filter behavior')
    @allure.description('This test verifies a successful filter results for high to low price')
    def test_filter(self):
        WebFlows.home_page_flow(get_data('ProductName'))
        WebFlows.search_result_flow('price-desc')
        Verifications.verify_first_item_highest_price()


    # Test Case 3
    @allure.title('Test03: Verify cart view')
    @allure.description('This test verifies a successful match between items and cart details')
    def test_add_to_cart_and_verify_cart_details(self):
        WebFlows.home_page_flow(get_data('ProductName'))
        Verifications.verify_number_of_results(get_data('ExpectedResults'))
        WebFlows.item_select()
        Verifications.verify_product_page_title(get_data('ProductTitle'))
        WebFlows.add_to_basket()
        Verifications.verify_add_to_cart_message(get_data('CartMessage'))
        WebFlows.navigate_to_cart()
        Verifications.soft_verify_cart_item_name(get_data('ProductTitle'))
        Verifications.soft_verify_cart_item_quantity(get_data('ItemQuantity'))
        Verifications.soft_verify_cart_item_price(get_data('ItemPrice'))
        verify_expectations()


    def teardown_method(self):
        WebFlows.clear_cart_mini()
        WebFlows.store_home_page()
