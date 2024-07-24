from base.selenium_driver import SeleniumDriver
from utils.custom_parser import getConfig

class Registration(SeleniumDriver):
    def __init__(self, driver, wait):
        super(Registration, self).__init__(driver, wait)
        self.driver = driver
        self.wait = wait
        self.Registration_Home_Page_xpath = getConfig("Registration_Page","Registration_Home_Page_xpath")
        self.FirstName_xpath = getConfig("Registration_Page", "FirstName_xpath")
        self.LastName_xpath = getConfig("Registration_Page", "LastName_xpath")
        self.Email_xpath = getConfig("Registration_Page", "Email_xpath")
        self.Password_xpath = getConfig("Registration_Page", "Password_xpath")
        self.Street_xpath = getConfig("Registration_Page", "Street_xpath")
        self.City_xpath = getConfig("Registration_Page", "City_xpath")
        self.State_xpath = getConfig("Registration_Page", "State_xpath")
        self.Zip_xpath = getConfig("Registration_Page", "Zip_xpath")
        self.Register_Button_xpath = getConfig("Registration_Page", "Register_Button_xpath")
        self.FirstName = getConfig("Registration_Page", "FirstName")
        self.LastName = getConfig("Registration_Page", "LastName")
        self.Email = getConfig("Registration_Page", "Email")
        self.Password = getConfig("Registration_Page", "Password")
        self.Street =getConfig("Registration_Page", "Street")
        self.City = getConfig("Registration_Page", "City")
        self.State = getConfig("Registration_Page", "State")
        self.Zip = getConfig("Registration_Page", "Zip")
        self.GoToFlightSearch = getConfig("Registration_Page","GoToFlightSearch")

    def verify_registration_page(self):
        reg_page_appears = self.isElementDisplayed(self.Registration_Home_Page_xpath, "xpath")
        self.screenShot("Registration Home Page appears")
        return reg_page_appears

    def verify_loginsuccessful(self):
        self.sendKeys(self.FirstName, self.FirstName_xpath, "xpath")
        self.sendKeys(self.LastName, self.LastName_xpath, "xpath")
        self.sendKeys(self.Email,self.Email_xpath,"xpath")
        self.sendKeys(self.Password,self.Password_xpath,"xpath")
        self.sendKeys(self.Street,self.Street_xpath,"xpath")
        self.sendKeys(self.City,self.City_xpath,"xpath")
        self.sendKeys(self.Zip,self.Zip_xpath,"xpath")
        self.selectDropdown(self.State_xpath,"xpath",visible_text=self.State)
        self.elementClick(self.Register_Button_xpath,"xpath")
        flight_search = self.isElementDisplayed(self.GoToFlightSearch,"xpath")
        self.elementClick(self.GoToFlightSearch,"xpath")
        return flight_search
