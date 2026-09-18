import time
import allure
import pytest
import selenium.webdriver

from selenium.webdriver import ActionChains
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from utilities.common_ops import get_data, get_time_stamp
from utilities.event_listener import EventListener
from utilities.manage_pages import ManagePages
import sys
import psycopg2

driver = None
actions = None
actions2 = None
m_action = None
mobile_size = None
db_connector = None


@pytest.fixture(scope='class')
def init_web_driver(request):
    edriver = get_web_driver()
    # Wrap driver so EventListener logs navigate/find/click
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


@pytest.fixture(scope='class')
def init_mobile_driver(request):
    # Start Appium session and page objects for the test class
    from appium.webdriver.common.multi_action import MultiAction
    from appium.webdriver.common.touch_action import TouchAction
    edriver = get_mobile_driver()
    globals()['driver'] = EventFiringWebDriver(edriver, EventListener())
    driver = globals()['driver']
    driver.implicitly_wait(int(get_data('WaitTime')))
    request.cls.driver = driver
    # Two TouchActions plus MultiAction are needed for pinch/zoom
    globals()['action'] = TouchAction(driver)
    request.cls.action = globals()['action']
    globals()['action2'] = TouchAction(driver)
    request.cls.action2 = globals()['action2']
    globals()['m_action'] = MultiAction(driver)
    request.cls.m_action = globals()['m_action']
    globals()['mobile_size'] = driver.get_window_size()
    request.cls.mobile_size = globals()['mobile_size']
    ManagePages.init_mobile_pages()
    yield
    time.sleep(2)
    driver.quit()


@pytest.fixture(scope='class')
def init_electron_driver(request):
    # Start Electron app session and page objects for the test class
    edriver = get_electron_driver()
    globals()['driver'] = EventFiringWebDriver(edriver, EventListener())
    driver = globals()['driver']
    driver.implicitly_wait(int(get_data('WaitTime')))
    request.cls.driver = driver
    globals()['action'] = ActionChains(driver)
    request.cls.action = globals()['action']
    ManagePages.init_electron_pages()
    yield
    driver.quit()


@pytest.fixture(scope='class')
def init_desktop_driver(request):
    # Start Windows Calculator session and page objects for the test class
    edriver = get_desktop_driver()
    globals()['driver'] = EventFiringWebDriver(edriver, EventListener())
    driver = globals()['driver']
    driver.implicitly_wait(int(get_data('WaitTime')))
    request.cls.driver = driver
    ManagePages.init_desktop_pages()
    yield
    driver.quit()

@pytest.fixture(scope='class')
def init_db_connection(request):
    # Open PostgreSQL connection used by web+DB tests
    db_connector = psycopg2.connect(
        host=get_data('DB_Host'),
        port=get_data('DB_Port'),
        dbname=get_data('DB_Name'),
        user=get_data('DB_User'),
        password=get_data('DB_Pass')
    )
    globals()['db_connector'] = db_connector
    request.cls.db_connector = db_connector
    yield
    db_connector.close()


def get_web_driver():
    # Pick Chrome, Firefox, or Edge from data.xml
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


def get_mobile_driver():
    # Pick Android or iOS from data.xml
    if get_data('Mobile_Device').lower() == 'android':
        driver = get_android(get_data('Udid'))
    elif get_data('Mobile_Device').lower() == 'ios':
        driver = get_ios(get_data('Udid'))
    else:
        driver = None
        raise Exception('Wrong input, unrecognized mobile OS')
    return driver


def get_electron_driver():
    # ChromeDriver pointed at the Electron app binary
    options = selenium.webdriver.ChromeOptions()
    options.binary_location = get_data('Electron_App')
    driver = selenium.webdriver.Chrome(chrome_options=options, executable_path=get_data('Electron_Driver'))
    return driver


def get_desktop_driver():
    # WinAppDriver session for Windows Calculator
    import appium.webdriver
    dc = {}
    dc['app'] = get_data('Application_Name')
    dc['platformName'] = 'Windows'
    dc['deviceName'] = 'WindowsPC'
    driver = appium.webdriver.Remote(get_data('WinAppDriver_Service'), dc)
    return driver



def get_chrome():
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager
    srv = Service(ChromeDriverManager().install())         # Selenium 4.x
    chrome_driver = selenium.webdriver.Chrome(service=srv) # Selenium 4.x
    #chrome_driver = selenium.webdriver.Chrome(ChromeDriverManager().install()) # selenium 3.x
    return  chrome_driver

def get_firefox():
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.firefox import GeckoDriverManager
    srv = Service(executable_path=GeckoDriverManager().install())  # Selenium 4.x
    ff_driver = selenium.webdriver.Firefox(service=srv)            # Selenium 4.x
    #ff_driver = selenium.webdriver.Firefox(GeckoDriverManager().install()) # Selenium 3.x
    return ff_driver

def get_edge():
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.microsoft import EdgeChromiumDriverManager
    srv = Service(EdgeChromiumDriverManager().install())  # Selenium 4.x
    edge_driver = selenium.webdriver.Edge(service=srv)    # Selenium 4.x
    #edge_driver = selenium.webdriver.Edge(EdgeChromiumDriverManager().install()) # Selenium 3.x
    return edge_driver


def get_android(udid):
    # Appium desired capabilities for the mortgage calculator APK
    import appium.webdriver
    dc = {}
    dc['udid'] = udid
    dc['appPackage'] = get_data('App_Package')
    dc['appActivity'] = get_data('App_Activity')
    dc['platformName'] = 'android'
    dc['automationName'] = 'UiAutomator2'
    android_driver = appium.webdriver.Remote(get_data('Appium_Server'), dc)
    return android_driver

def get_ios(udid):
    # Appium desired capabilities for iOS
    import appium.webdriver
    dc = {}
    dc['udid'] = udid
    dc['bundle_id'] = get_data('Bundle_ID')
    dc['platformName'] = 'ios'
    dc['automationName'] = 'XCUITest'
    ios_driver = appium.webdriver.Remote(get_data('Appium_Server'), dc)
    return ios_driver

# Catch exceptions and errors
def pytest_exception_interact(node, call, report):
    if report.failed:
        if globals()['driver'] is not None: # if it is None -> this is exception from API test
            image = get_data('ScreenshotPath') + 'screen_' + str(get_time_stamp()) + '.png'
            globals()['driver'].get_screenshot_as_file(image)
            allure.attach.file(image, attachment_type=allure.attachment_type.PNG)



