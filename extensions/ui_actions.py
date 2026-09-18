import allure
import test_cases.conftest as conf
from selenium.webdriver import ActionChains
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
    @allure.step('mouse hover tooltip')
    def mouse_hover_tooltip(elem: WebElement):
        # Unwrap EventFiringWebDriver so ActionChains can use the real driver/element
        driver = getattr(conf.driver, 'wrapped_driver', conf.driver)
        target = getattr(elem, 'wrapped_element', elem)
        ActionChains(driver).move_to_element(target).click().perform()

    @staticmethod
    @allure.step('Selecting value from dropdown')
    def select_from_droplist(elem: WebElement, value: str):
        #Select a value from a dropdown
        select = Select(elem)
        select.select_by_value(value)