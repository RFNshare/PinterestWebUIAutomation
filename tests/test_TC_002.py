import time

import pytest

from utilities.base_class import BaseClass
from utilities.test_data import TestData
from pageobjects.base_page import HomePage


# Login
class TestTC_002(BaseClass):
    # Email Login
    @pytest.mark.now
    def test_tc_001(self):
        homepage = HomePage(self.driver)
        homepage.login().click()
        time.sleep(5)
        homepage.email_input().send_keys(TestData.DEMO_EMAIL)
        homepage.pass_input().send_keys(TestData.DEMO_PASS)
        time.sleep(5)
        homepage.submit().click()
        time.sleep(10)

    # FB Login
    def test_tc_002(self):
        homepage = HomePage(self.driver)
        homepage.login().click()
        homepage.fb_btn().click()
        # ____ Continue with facebook ____ STEP3

    # Google Login
    def test_tc_003(self):
        homepage = HomePage(self.driver)
        homepage.login().click()
        homepage.g_btn().click()
        time.sleep(5)
        # ____ Continue with Google ____STEP3***
