import pytest
from pages.flightsearch_page import FlightSearch
from base.basetest import BaseTest

@pytest.mark.usefixtures("oneTimeSetup")
class TestFlightSearch(BaseTest):
    def test_flightsearch(self):
        flight_search = FlightSearch(self.driver, self.wait)
        select_flights = flight_search.verify_flightsearch()
        assert select_flights == True
