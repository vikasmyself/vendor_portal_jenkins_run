import pytest
from base.basetest import BaseTest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

@pytest.mark.usefixtures("oneTimeSetup")
class TestTempo(BaseTest):
    def test_temproary(self):
        options = Options()
        options.add_argument("--headless")

        driver = webdriver.Firefox(options=options)
        driver.get('https://www.google.com')
        print(driver.title)  # Should print "Google" if headless is working
        driver.quit()



