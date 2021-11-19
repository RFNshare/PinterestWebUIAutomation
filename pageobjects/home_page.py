from utilities.locators import *


class HomePage():
    def __init__(self, driver):
        self.driver = driver
        self.locators = HomePageLocators

    def first_page(self):
        return self.driver

    def logo_btn(self):
        return self.driver.find_element(*self.locators.LOGO)
