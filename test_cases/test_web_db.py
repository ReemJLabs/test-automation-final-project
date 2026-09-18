import allure
import pytest

from extensions.verifications import Verifications
from workflows.db_flows import DBFlows
from workflows.web_flows import WebFlows


@pytest.mark.usefixtures('init_web_driver')
@pytest.mark.usefixtures('init_db_connection')
class Test_Web_DB:
    @allure.title('Test01: Item search via DB')
    @allure.description('This test verify Item search using elements taken from database')
    def test_verify_item_search_db(self):
        expected_title = DBFlows.item_results_via_db()
        WebFlows.item_select()
        Verifications.verify_product_page_title(expected_title)