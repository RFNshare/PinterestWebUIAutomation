import time
from selenium import webdriver
import pytest


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
    time.sleep(2)
    yield
    driver.close()
