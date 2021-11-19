import time
import pytest
from utilities.base_class import BaseClass
from utilities.test_data import TestData
from pageobjects.base_page import HomePage


# Signup
class TestTC_003(BaseClass):
    # Email Signup
    def test_tc_001(self):
        homepage = HomePage(self.driver)
        log = self.getLogger()
        homepage.signup().click()
        time.sleep(5)
        homepage.email_input().send_keys('af.qups@gmail.com')
        time.sleep(5)
        homepage.pass_input().send_keys('asdfgh123')
        homepage.age_btn().send_keys('25')
        time.sleep(5)
        homepage.submit().click()
        time.sleep(5)
        log.info("Successfully signup with email")

    @pytest.mark.now
    # FB Signup
    def test_tc_002(self):
        main_page = self.driver.current_window_handle
        log = self.getLogger()
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
        try:
            self.driver.quit()
            log.info("Signup with Facebook Success")
        except Exception as e:
            log.info(e)

    # Google Signup
    def test_tc_003(self):
        homepage = HomePage(self.driver)
        log = self.getLogger()
        homepage.login().click()
        homepage.g_btn().click()
        time.sleep(5)
        log.info("Signup with Google")
        # ____ Continue with Google ____STEP3***
