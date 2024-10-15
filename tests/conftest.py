import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope="module")
def driver():
    print("Driver open")
    options = webdriver.ChromeOptions()
    # Автоматическое закрытие окна
    options.add_experimental_option("detach", False)
    gg = Service()
    driver = webdriver.Chrome()
    yield driver
    print("Driver close")


# noinspection PyTypeChecker
@pytest.fixture(scope="module")
def set_group():
    print("enter system")
    yield
    print("exit system")