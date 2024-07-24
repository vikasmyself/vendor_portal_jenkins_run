import logging
import pytest
from base.basetest import BaseTest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import utils.custom_logger as cl

@pytest.mark.usefixtures("oneTimeSetup")
class TestTempo(BaseTest):
    log = cl.customLogger(logging.DEBUG)
    def test_temproary(self):
        options = Options()
        options.add_argument("--headless")
        self.log.info("Inside test_temp01")
        driver = webdriver.Firefox(options=options)
        driver.get('https://www.google.com')
        print(driver.title)  # Should print "Google" if headless is working
        driver.quit()







