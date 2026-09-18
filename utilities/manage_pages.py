import test_cases.conftest as conf
from page_objects.desktop_objects.standard_page import StandardPage
from page_objects.electron_objects.task_page import TaskPage
from page_objects.mobile_objects.calculator_page import CalculatorPage
from page_objects.mobile_objects.saved_page import SavedPage
from page_objects.web_objects.home_page import HomePage
from page_objects.web_objects.product_page import ProductPage
from page_objects.web_objects.search_results_page import SearchResultPage
from page_objects.web_objects.cart_page import CartPage

#Web Objects
web_home = None
web_search_results = None
web_product = None
web_cart = None


#Mobile Objects
mobile_calculator = None
mobile_saved = None


#Electron Objects
electron_task = None

#Desktop Objects
standard_calc = None

class ManagePages:
    @staticmethod
    def init_web_pages():
        # Store web page objects in module globals for workflows to use
        globals()['web_home'] = HomePage(conf.driver)
        globals()['web_search_results'] = SearchResultPage(conf.driver)
        globals()['web_product'] = ProductPage(conf.driver)
        globals()['web_cart'] = CartPage(conf.driver)


    @staticmethod
    def init_mobile_pages():
        # Store mobile page objects in module globals
        globals()['mobile_calculator'] = CalculatorPage(conf.driver)
        globals()['mobile_saved'] = SavedPage(conf.driver)


    @staticmethod
    def init_electron_pages():
        # Store electron page objects in module globals
        globals()['electron_task'] = TaskPage(conf.driver)

    @staticmethod
    def init_desktop_pages():
        # Store desktop page objects in module globals
        globals()['standard_calc'] = StandardPage(conf.driver)