from datetime import datetime

from selenium.common import WebDriverException, NoSuchElementException
from selenium.webdriver import ActionChains

from utilites.logger import Logger


class Base:
    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(driver)

    """Method get current url"""
    def get_current_url(self):
        try:
            get_url = self.driver.current_url
            print("Current url: " + get_url)
        except WebDriverException as e:
            print(f"Error getting current URL: {str(e)}")
            Logger.log_error(e)

    """Method assert word"""

    @staticmethod
    def assert_word(word, result):
        try:
            value_word = word.text
            assert value_word == result, f"Expected '{result}', but got '{value_word}'"
            print(f"Good value: {result}")
        except AssertionError as e:
            print(f"Assertion Error: {str(e)}")
            Logger.log_error(e)
        except NoSuchElementException as e:
            print(f"Error: Element not found: {str(e)}")
            Logger.log_error(e)


    """Method screenshot"""

    def get_screenshot(self):
        now_date = datetime.today().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot' + now_date + '.png'
        self.driver.save_screenshot('C:\\Users\\ajnaf\\PycharmProjects\\smoke_onlinetrade\\screen\\' + name_screenshot)


    """Method assert url"""
    def assert_url(self, result):
        try:
            get_url = self.driver.current_url
            assert get_url == result, f"Expected URL '{result}', but got '{get_url}'"
            print("Good value URL")
        except AssertionError as e:
            print(f"Assertion Error: {str(e)}")
            Logger.log_error(e)
        except WebDriverException as e:
            print(f"Error getting current URL: {str(e)}")
            Logger.log_error(e)

    """Method assert expected information and actual"""

    @staticmethod
    def information(expected, actual):
        try:
            value_expected = expected.text
            value_actual = actual.text
            assert value_expected == value_actual, f"Expected '{value_expected}', but got '{value_actual}'"
            print(f"The expected information ({value_expected}) is the same as the actual one")
        except AssertionError as e:
            print(f"Assertion Error: {str(e)}")
            Logger.log_error(e)
        except NoSuchElementException as e:
            print(f"Error: Element not found: {str(e)}")
            Logger.log_error(e)