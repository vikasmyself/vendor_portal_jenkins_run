import pytest
from base.basetest import BaseTest
from pages.confirmation_page import Confirmation


@pytest.mark.usefixtures("oneTimeSetup")
class TestConfirmation(BaseTest):
    def test_confirmation(self):
        confirm = Confirmation(self.driver, self.wait)
        status = confirm.verify_confirmation()
        assert status == True
