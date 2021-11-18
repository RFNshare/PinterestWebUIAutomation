import time
from utilities.base_class import BaseClass
from utilities.test_data import TestData
from pageobjects.base_page import HomePage


class TestCaseOne(BaseClass):
    def test_tc_001(self):
        home_page = HomePage(self.driver)
        home_page.first_page().get(TestData.BASE_URL)
