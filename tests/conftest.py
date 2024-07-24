import pytest
from base.webdriverfactory import WebDriverFactory
from selenium.webdriver.support.ui import WebDriverWait

@pytest.fixture(scope='session')
def driver_setup(browser, osType):
    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance()
    wait = WebDriverWait(driver, 50)
    yield driver, wait
    driver.quit()

@pytest.fixture(scope='class')
def oneTimeSetup(request, driver_setup):
    driver, wait = driver_setup
    if request.cls is not None:
        request.cls.driver = driver
        request.cls.wait = wait

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Type of browser. E.g. chrome, firefox")
    parser.addoption("--osType", action="store", default="windows", help="Type of operating system. E.g. windows, linux, mac")

@pytest.fixture(scope='session')
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope='session')
def osType(request):
    return request.config.getoption("--osType")
