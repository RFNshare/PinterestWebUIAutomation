from selenium.webdriver.common.by import By


class HomePageLocators(object):
    # Login/Signup
    LOGIN_BUTTON = (By.XPATH, "//div[@class='tBJ dyH iFc yTZ erh tg7 mWe']")
    SIGN_UP_BUTTON = (By.XPATH, '//div[@class="tBJ dyH iFc yTZ pBj tg7 mWe"]')
    # Login/Signup by email input
    EMAIL_INPUT = (By.XPATH, "//input[@id='email']")
    PASS_INPUT = (By.XPATH, "//input[@id='password']")
    AGE_BUTTON = (By.XPATH, "//input[@id='age']")
    SUBMIT_BUTTON = (By.XPATH, "//div[@data-test-id='registerFormSubmitButton']")
    # Login/Signup by facebook input
    FB_BUTTON = (By.XPATH, "//div[@data-test-id='facebook-connect-button']")
    FB_EMAIL = (By.XPATH, "//input[@id='email']")
    FB_PASS = (By.XPATH, "//input[@id='pass']")
    FB_SUBMIT = (By.XPATH, "//input[@name='login']")
    # Utilities
    G_BUTTON = (By.XPATH, "//div[@data-test-id='google-connect-button']")
