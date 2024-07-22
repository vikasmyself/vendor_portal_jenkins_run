import pytest
from pages.registration_page import Registration

class BaseTest:
    @pytest.fixture(autouse=True)
    def setup(self, oneTimeSetup):
        self.driver = self.__class__.driver
        self.wait = self.__class__.wait
        self.reg = Registration(self.driver, self.wait)
