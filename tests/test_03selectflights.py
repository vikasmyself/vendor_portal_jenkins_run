import pytest
from base.basetest import BaseTest
from pages.selectflight_page import SelectFlight

@pytest.mark.usefixtures("oneTimeSetup")
class TestSelectFlight(BaseTest):
    def test_selectflight(self):
        select_flight = SelectFlight(self.driver, self.wait)
        select_flight.verify_selectflight()
