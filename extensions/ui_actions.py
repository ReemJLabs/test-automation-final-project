import allure
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select


class UiActions:
    #UI interaction actions

    @staticmethod
    @allure.step('Clicking on element')
    def click(elem: WebElement):
        #Click on an element
        elem.click()

    @staticmethod
    @allure.step('Entering text into element')
    def update_text(elem: WebElement, value: str):
        #Enter text into an element
        elem.send_keys(value)

    @staticmethod
    @allure.step('Selecting value from dropdown')
    def select_from_droplist(elem: WebElement, value: str):
        #Select a value from a dropdown
        select = Select(elem)
        select.select_by_value(value)