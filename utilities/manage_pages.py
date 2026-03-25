import test_cases.conftest as conf
from page_objects.web_objects.home_page import HomePage
from page_objects.web_objects.product_page import ProductPage
from page_objects.web_objects.search_results_page import SearchResultPage
from page_objects.web_objects.cart_page import CartPage

#Web Objects
web_home = None
web_search_results = None
web_product = None
web_cart = None


class ManagePages:
    @staticmethod
    def init_web_pages():
        globals()['web_home'] = HomePage(conf.driver)
        globals()['web_search_results'] = SearchResultPage(conf.driver)
        globals()['web_product'] = ProductPage(conf.driver)
        globals()['web_cart'] = CartPage(conf.driver)

