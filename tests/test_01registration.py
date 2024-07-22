import pytest
from pages.registration_page import Registration
from base.basetest import BaseTest

@pytest.mark.usefixtures("oneTimeSetup")
class TestRegistration(BaseTest):
    def test_registration_page_appears(self):
        reg_page_appears = self.reg.verify_registration_page()
        assert reg_page_appears == True

    def test_loginsuccessful(self):
        login_success = self.reg.verify_loginsuccessful()
        assert login_success == True
