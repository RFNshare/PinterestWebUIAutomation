from utilities.locators import *


class HomePage():
    def __init__(self, driver):
        self.driver = driver
        self.locators = HomePageLocators

    def first_page(self):
        return self.driver

    def logo_btn(self):
        return self.driver.find_element(*self.locators.LOGO)

    def home_btn(self):
        return self.driver.find_element(*self.locators.HOME)

    def search(self):
        return self.driver.find_element(*self.locators.SEARCH)

    def notifications(self):
        return self.driver.find_element(*self.locators.NOTIFICATION)

    def messages(self):
        return self.driver.find_element(*self.locators.MESSAGES)

    def profile(self):
        return self.driver.find_element(*self.locators.PROFILE)

    def messages_box(self):
        return self.driver.find_element(*self.locators.MESSAGES_BOX)

    def profile_button(self):
        return self.driver.find_element(*self.locators.PROFILE_BUTTON)

    def profile_edit_button(self):
        return self.driver.find_element(*self.locators.PROFILE_EDIT_BUTTON)

    def profile_share_button(self):
        return self.driver.find_element(*self.locators.PROFILE_SHARE_BUTTON)

    def question_button(self):
        return self.driver.find_element(*self.locators.QUESTION_MARK)
