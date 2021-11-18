from selenium.webdriver.common.by import By


class HomePageLocators(object):
    # Login/Signup
    LOGIN_BUTTON = (By.XPATH, "//div[@class='tBJ dyH iFc yTZ erh tg7 mWe']")
    SIGN_UP_BUTTON = (By.XPATH, '//div[@class="tBJ dyH iFc yTZ pBj tg7 mWe"]')

    EMAIL_INPUT = (By.XPATH, "//input[@id='email']")
    PASS_INPUT = (By.XPATH, "//input[@id='password']")
    # Social Button
    FB_BUTTON = (By.XPATH, "//div[@data-test-id='facebook-connect-button']")
    G_BUTTON = (By.XPATH, "//div[@data-test-id='google-connect-button']")
    # Utilities
    AGE_BUTTON = (By.XPATH, "//div[@data-test-id='google-connect-button']")
    SUBMIT_BUTTON = (By.XPATH, "//div[text()='Continue']")

