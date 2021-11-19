from utilities.locators import *


class BasePage():
    def __init__(self, driver):
        self.driver = driver
        self.locators = HomePageLocators

    def first_page(self):
        return self.driver

    def login(self):
        return self.driver.find_element(*self.locators.LOGIN_BUTTON)

    def signup(self):
        return self.driver.find_element(*self.locators.SIGN_UP_BUTTON)

    def submit(self):
        return self.driver.find_element(*self.locators.SUBMIT_BUTTON)

    def email_input(self):
        return self.driver.find_element(*self.locators.EMAIL_INPUT)

    def pass_input(self):
        return self.driver.find_element(*self.locators.PASS_INPUT)

    def fb_btn(self):
        return self.driver.find_element(*self.locators.FB_BUTTON)

    def fb_emailbtn(self):
        return self.driver.find_element(*self.locators.FB_EMAIL)

    def fb_passbtn(self):
        return self.driver.find_element(*self.locators.FB_PASS)

    def fb_submitbtn(self):
        return self.driver.find_element(*self.locators.FB_SUBMIT)

    def g_btn(self):
        return self.driver.find_element(*self.locators.G_BUTTON)

    def age_btn(self):
        return self.driver.find_element(*self.locators.AGE_BUTTON)

