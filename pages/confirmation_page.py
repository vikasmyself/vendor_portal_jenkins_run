from base.selenium_driver import SeleniumDriver
from utils.custom_parser import getConfig

class Confirmation(SeleniumDriver):
    def __init__(self, driver, wait):
        super(Confirmation, self).__init__(driver, wait)
        self.driver = driver
        self.wait = wait
        self.ConfirmationPage_xpath = getConfig("Confirmation_Page", "ConfirmationPage_xpath")

    def verify_confirmation(self):
        self.waitForElement(self.ConfirmationPage_xpath,"xpath")
        confirm = self.isElementDisplayed(self.ConfirmationPage_xpath, "xpath")
        return confirm
