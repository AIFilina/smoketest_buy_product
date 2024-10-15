

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base
from utilites.logger import Logger


class Main_page(Base):
    url = "https://comfy-shop.ru/"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #URL

    url_category ="https://comfy-shop.ru/category/smartfony"

    #locators
    geo_button = '//*[@id="header"]/div[1]/div/div[1]/div[1]'
    city_button = '//*[@id="header-city-b9001e55-72ed-43bf-b7eb-41b86a14380e"]'

    # burger_menu_button = '//*[@id="header"]/div[3]/div[1]'
    category_1 = '//img[@alt="Смартфоны и гаджеты"]'
    category_2 = '//a[@href="/category/smartfony"]'

    # getters
    def get_geo_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.geo_button)))

    def get_city_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.city_button)))

    def get_category_1(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.category_1)))

    def get_category_2(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.category_2)))

    # actions
    def click_geo_button(self):
        self.get_geo_button().click()
        print("Click geo button")

    def click_city_button(self):
        self.get_city_button().click()
        print("Click city button")

    def move_to_category_1(self):
        self.action.move_to_element(self.get_category_1()).perform()
        print("Move to category 1")

    def click_category_2(self):
        self.get_category_2().click()
        print("Click category 2")

    # Methods

    def select_category(self):
        Logger.add_start_step("Select category product")
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_geo_button()
        self.click_city_button()
        self.move_to_category_1()
        self.click_category_2()
        self.assert_url(self.url_category)
        Logger.add_end_step(url=self.driver.current_url, method="Select category product")