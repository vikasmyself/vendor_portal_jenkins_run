from base.selenium_driver import SeleniumDriver
from utils.custom_parser import getConfig

class FlightSearch(SeleniumDriver):
    def __init__(self, driver, wait):
        super(FlightSearch, self).__init__(driver, wait)
        self.driver = driver
        self.wait = wait
        self.RoundTrip_xpath = getConfig("Flight_Search","RoundTrip_xpath")
        self.Passengers_xpath = getConfig("Flight_Search","Passengers_xpath")
        self.DepartingFrom_xpath = getConfig("Flight_Search","DepartingFrom_xpath")
        self.ArrivingIn_xpath = getConfig("Flight_Search","ArrivingIn_xpath")
        self.ServiceClass_Economy_xpath = getConfig("Flight_Search","ServiceClass_Economy_xpath")
        self.ServiceClass_First_xpath = getConfig("Flight_Search","ServiceClass_First_xpath")
        self.ServiceClass_Business_xpath = getConfig("Flight_Search","ServiceClass_Business_xpath")
        self.SearchFlights_button_xpath = getConfig("Flight_Search","SearchFlights_button_xpath")
        self.SelectFlights_xpath = getConfig("Select_Flights","SelectFlights_xpath")
    def verify_flightsearch(self):
        self.elementClick(self.RoundTrip_xpath,"xpath")
        self.selectDropdown(self.Passengers_xpath,"xpath",visible_text="Two")
        self.selectDropdown(self.DepartingFrom_xpath,"xpath",visible_text="London")
        self.selectDropdown(self.ArrivingIn_xpath,"xpath",visible_text="Paris")
        self.elementClick(self.ServiceClass_Business_xpath,"xpath")
        self.elementClick(self.SearchFlights_button_xpath,"xpath")
        select_flights = self.isElementDisplayed(self.SelectFlights_xpath,"xpath")
        return select_flights