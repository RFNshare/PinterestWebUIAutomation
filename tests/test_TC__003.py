import time

import pytest

from utilities.base_class import BaseClass
from utilities.test_data import TestData
from pageobjects.base_page import HomePage


# Signup
class TestTC_003(BaseClass):
    # Email Signup
    @pytest.mark.now
    def test_tc_001(self):
        homepage = HomePage(self.driver)
        homepage.signup().click()
        time.sleep(5)
        homepage.email_input().send_keys('af.qups@gmail.com')
        time.sleep(5)
        homepage.pass_input().send_keys('asdfgh123')
        homepage.age_btn().send_keys('25')
        time.sleep(5)
        homepage.submit().click()
        time.sleep(5)

    # FB Signup
    def test_tc_002(self):
        homepage = HomePage(self.driver)
        homepage.login().click()
        homepage.fb_btn().click()
        # ____ Continue with facebook ____ STEP3

    # Google Signup
    def test_tc_003(self):
        homepage = HomePage(self.driver)
        homepage.login().click()
        homepage.g_btn().click()
        time.sleep(5)
        # ____ Continue with Google ____STEP3***
