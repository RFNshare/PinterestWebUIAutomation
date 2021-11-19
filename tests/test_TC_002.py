import time
import pytest
import pickle
from utilities.base_class import BaseClass
from utilities.test_data import TestData
from pageobjects.base_page import BasePage


# Login
class TestTC_002(BaseClass):
    # Email Login
    def test_tc_001(self):
        homepage = BasePage(self.driver)
        log = self.getLogger()
        homepage.login().click()
        time.sleep(5)
        # clear
        homepage.email_input().send_keys(TestData.DEMO_EMAIL)
        # clear
        homepage.pass_input().send_keys(TestData.DEMO_PASS)
        time.sleep(5)
        homepage.submit().click()
        time.sleep(3)
        log.info("Login by email success")

    # FB Login
    def test_tc_002(self):
        main_page = self.driver.current_window_handle
        log = self.getLogger()
        homepage = BasePage(self.driver)
        homepage.login().click()
        homepage.fb_btn().click()
        time.sleep(15)
        for handle in self.driver.window_handles:
            if handle != main_page:
                fb_login = handle
                self.driver.switch_to.window(fb_login)
        time.sleep(3)
        # clear
        homepage.fb_emailbtn().send_keys(TestData.DEMO_EMAIL)
        # clear
        time.sleep(3)
        homepage.fb_passbtn().send_keys(TestData.DEMO_PASS)
        time.sleep(3)
        homepage.fb_submitbtn().click()
        try:
            self.driver.quit()
            log.info("Login with Facebook Success")
        except Exception as e:
            log.info(e)

    # Google Login
    def test_tc_003(self):
        homepage = BasePage(self.driver)
        log = self.getLogger()
        homepage.login().click()
        homepage.g_btn().click()
        time.sleep(5)
        log.info("Login with Google")
        # ____ Continue with Google ____STEP3***
