import time
import pytest
import pickle

from selenium.webdriver import Keys

from utilities.base_class import BaseClass
from utilities.test_data import TestData
from pageobjects.home_page import HomePage
from pageobjects.base_page import BasePage
from .test_TC_002 import TestTC_002


# Homepage
class TestTC_004(BaseClass):
    # Email Signup
    @pytest.mark.login_4
    def test_tc_000(self):
        homepage = BasePage(self.driver)
        homepage.login().click()
        time.sleep(5)
        homepage.email_input().send_keys(TestData.DEMO_EMAIL)
        homepage.pass_input().send_keys(TestData.DEMO_PASS)
        time.sleep(5)
        homepage.submit().click()
        time.sleep(3)

    def test_tc_001(self):
        homepage = HomePage(self.driver)
        homepage.logo_btn().click()
        logo = self.getLogger()
        logo.info("Successfully click logo button")

    @pytest.mark.login_4
    def test_tc_002(self):
        homepage = HomePage(self.driver)
        homepage.home_btn().click()
        logo = self.getLogger()
        logo.info("Successfully click home button")

    @pytest.mark.login_4
    def test_tc_003(self):
        homepage = HomePage(self.driver)
        homepage.search().send_keys("Avatar", Keys.ENTER)
        time.sleep(15)
        # logo = self.getLogger()
        # logo.info("Successfully click home button")