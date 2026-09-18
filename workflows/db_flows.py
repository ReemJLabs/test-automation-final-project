import allure

from extensions.db_actions import DBActions
from workflows.web_flows import WebFlows


class DBFlows:
    @staticmethod
    @allure.step('Search for item via Database Flow')
    def item_results_via_db():
        columns = ['name', 'type']
        result = DBActions.get_query_result(columns, 'products', 'comments', 'correct')
        if not result:
            raise Exception("No product row found in DB with comments = 'correct'")
        search_term, product_title = result[0]
        WebFlows.home_page_flow(search_term)
        return product_title



