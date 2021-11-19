import time
import pytest
from utilities.base_class import BaseClass
from utilities.test_data import TestData
from pageobjects.base_page import HomePage


# Login
class TestTC_002(BaseClass):
    # Email Login
    def test_tc_001(self):
        homepage = HomePage(self.driver)
        homepage.login().click()
        time.sleep(5)
        homepage.email_input().send_keys(TestData.DEMO_EMAIL)
        homepage.pass_input().send_keys(TestData.DEMO_PASS)
        time.sleep(5)
        homepage.submit().click()
        time.sleep(10)

    @pytest.mark.now
    # FB Login
    def test_tc_002(self):
        main_page = self.driver.current_window_handle
        homepage = HomePage(self.driver)
        homepage.login().click()
        homepage.fb_btn().click()
        time.sleep(15)
        for handle in self.driver.window_handles:
            if handle != main_page:
                fb_login = handle
                self.driver.switch_to.window(fb_login)
        time.sleep(3)
        homepage.fb_emailbtn().send_keys(TestData.DEMO_EMAIL)
        time.sleep(3)
        homepage.fb_passbtn().send_keys(TestData.DEMO_PASS)
        time.sleep(3)
        homepage.fb_submitbtn().click()
        time.sleep(3)

    # Google Login
    def test_tc_003(self):
        homepage = HomePage(self.driver)
        homepage.login().click()
        homepage.g_btn().click()
        time.sleep(5)
        # ____ Continue with Google ____STEP3***
