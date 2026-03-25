import time
import allure
import pytest
import selenium.webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from utilities.common_ops import get_data, get_time_stamp
from utilities.event_listener import EventListener
from utilities.manage_pages import ManagePages
import sys

driver = None
actions = None


@pytest.fixture(scope='class')
def init_web_driver(request):
    edriver = get_web_driver()
    globals()['driver'] = EventFiringWebDriver(edriver,EventListener())
    #globals()['driver'] = get_web_driver() This is the old method before i used the event listener class above
    driver = globals()['driver']
    driver.maximize_window()
    driver.implicitly_wait(int(get_data('WaitTime')))
    driver.get(get_data('Url'))
    request.cls.driver = driver
    # Create single ActionChains instance and set it in multiple places for compatibility
    actions_instance = ActionChains(driver)
    globals()['action'] = actions_instance
    globals()['actions'] = actions_instance
    # Set module-level variable so conf.actions works
    #import sys
    sys.modules[__name__].actions = actions_instance
    ManagePages.init_web_pages()
    yield
    time.sleep(2)
    driver.quit()


def get_web_driver():
    web_driver = get_data('Browser')
    if web_driver.lower() == 'chrome':
        driver = get_chrome()
    elif web_driver.lower() == 'firefox':
        driver = get_firefox()
    elif web_driver.lower() == 'edge':
        driver = get_edge()
    else:
        driver = None
        raise Exception('Wrong Input, Unrecognized Browser')
    return driver

def get_chrome():
    srv = Service(ChromeDriverManager().install())         # Selenium 4.x
    chrome_driver = selenium.webdriver.Chrome(service=srv) # Selenium 4.x
    #chrome_driver = selenium.webdriver.Chrome(ChromeDriverManager().install()) # selenium 3.x
    return  chrome_driver

def get_firefox():
    srv = Service(executable_path=GeckoDriverManager().install())  # Selenium 4.x
    ff_driver = selenium.webdriver.Firefox(service=srv)            # Selenium 4.x
    #ff_driver = selenium.webdriver.Firefox(GeckoDriverManager().install()) # Selenium 3.x
    return ff_driver

def get_edge():
    srv = Service(EdgeChromiumDriverManager().install())  # Selenium 4.x
    edge_driver = selenium.webdriver.Edge(service=srv)    # Selenium 4.x
    #edge_driver = selenium.webdriver.Edge(EdgeChromiumDriverManager().install()) # Selenium 3.x
    return edge_driver

# Catch exceptions and errors
def pytest_exception_interact(node, call, report):
    if report.failed:
        if globals()['driver'] is not None: # if it is None -> this is exception from API test
            image = get_data('ScreenshotPath') + 'screen_' + str(get_time_stamp()) + '.png'
            globals()['driver'].get_screenshot_as_file(image)
            allure.attach.file(image, attachment_type=allure.attachment_type.PNG)



