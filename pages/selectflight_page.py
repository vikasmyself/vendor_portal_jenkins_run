from base.selenium_driver import SeleniumDriver
from utils.custom_parser import getConfig

class SelectFlight(SeleniumDriver):
    def __init__(self, driver, wait):
        super(SelectFlight, self).__init__(driver, wait)
        self.driver = driver
        self.wait = wait
        self.DepartureEmiratesBusiness = getConfig("Select_Flights", "DepartureEmiratesBusiness")
        self.ArrivalQatarBusiness = getConfig("Select_Flights", "ArrivalQatarBusiness")
        self.ConfirmFlights = getConfig("Select_Flights", "ConfirmFlights")

    def verify_selectflight(self):
        self.elementClick(self.DepartureEmiratesBusiness, "xpath")
        self.elementClick(self.ArrivalQatarBusiness, "xpath")
        self.elementClick(self.ConfirmFlights, "xpath")
