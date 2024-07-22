from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from utils.custom_parser import getConfig


class WebDriverFactory:
    def __init__(self, browser):
        self.browser = browser

    def _set_common_options(self, options, browser_name):
        options.add_argument("--disable-infobars")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-gpu")
        #options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1280,1024")

        if browser_name.lower() == "firefox":
            options.add_argument("--headless")
        elif browser_name.lower() in ["chrome", "edge"]:
            options.add_argument("--headless")

    def getWebDriverInstance(self):
        baseURL = getConfig("Setup", "baseURL")
        hubURL = getConfig("Setup", "hubURL")
        selenium_grid = getConfig("Setup", "selenium_grid").lower() == "true"

        if self.browser.lower() == "chrome":
            options = webdriver.ChromeOptions()
            self._set_common_options(options, "chrome")

            if selenium_grid:
                driver = webdriver.Remote(command_executor=hubURL, options=options)
            else:
                driver = webdriver.Chrome(options=options)

        elif self.browser.lower() == "firefox":
            options = webdriver.FirefoxOptions()
            self._set_common_options(options, "firefox")

            if selenium_grid:
                driver = webdriver.Remote(command_executor=hubURL, options=options)
            else:
                driver = webdriver.Firefox(options=options)

        elif self.browser.lower() == "edge":
            options = webdriver.EdgeOptions()
            self._set_common_options(options, "edge")

            if selenium_grid:
                driver = webdriver.Remote(command_executor=hubURL, options=options)
            else:
                driver = webdriver.Edge(options=options)

        else:
            raise Exception(f"Browser '{self.browser}' is not supported")

        driver.maximize_window()
        driver.get(baseURL)
        return driver
