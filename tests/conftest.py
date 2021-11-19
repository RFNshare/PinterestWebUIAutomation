import time
from selenium import webdriver
import pytest
import json


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def home_setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(
            executable_path='C:/files/chromedriver.exe')
    elif browser_name == "firefox":
        driver = webdriver.Firefox(
            executable_path=r'C:/files/geckodriver.exe')
    request.cls.driver = driver
    time.sleep(2)
    yield
    driver.close()


# def save_cookie(driver, path):
#     with open(path, 'w') as filehandler:
#         json.dump(driver.get_cookies(), filehandler)
#
#
# def load_cookie(driver, path):
#     with open(path, 'r') as cookiesfile:
#         cookies = json.load(cookiesfile)
#     for cookie in cookies:
#         driver.add_cookie(cookie)


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(
            executable_path='C:/files/chromedriver.exe')
    elif browser_name == "firefox":
        driver = webdriver.Firefox(
            executable_path=r'C:/files/geckodriver.exe')
    request.cls.driver = driver
    driver.get(
        "https://www.pinterest.com/"
    )
    driver.maximize_window()
    # save_cookie(driver)
    # load_cookie(driver)

    time.sleep(2)
    yield
    driver.close()
