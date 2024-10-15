from time import sleep

import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilites.logger import Logger


class Select_product_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # url
    url_cart ="https://comfy-shop.ru/cart/checkout"

    # locators

    filter_price_start ='//input[@id="priceStart"]'
    filter_price_end = '//input[@id="priceEnd"]'

    filter_brand_1 = '//a[@title="Samsung"]'
    filter_brand_2 = '//a[@title="Xiaomi"]'
    filter_brand_3 = '//a[@title="Realme"]'
    filter_brand_4 = '//a[@title="Honor"]'

    filter_memory_1 ='//a[@title="256 Гб"]'
    filter_memory_2 ='//a[@title="128 Гб"]'

    filters_button ='/html/body/div[1]/main/div[3]/div[2]/div/div[1]/div[3]/div[2]'

    sort_button ='//span[@class="category-top-line-sort-selected-inner"]'
    price_down_button ='//a[@data-sort="price_down"]'

    product_name ='//*[@id="products"]/ul[1]/div[3]/div[5]/a'
    product_price ='//*[@id="products"]/ul[1]/div[3]/div[7]/div[1]/div/span/span'
    product_buy_button = '//*[@id="products"]/ul[1]/div[3]/div[7]/div[2]/div[1]/a[2]'

    cart_button ='//a[@title="Оформить заказ"]'



    '''GETTERS'''

    # Start/ End price range
    def get_filter_price_start(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.filter_price_start)))
    def get_filter_price_end(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.filter_price_end)))

    # Filters phone
    def get_filter_brand_1(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.filter_brand_1)))
    def get_filter_brand_2(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.filter_brand_2)))
    def get_filter_brand_3(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.filter_brand_3)))
    def get_filter_brand_4(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.filter_brand_4)))

    def get_filter_memory_1(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.filter_memory_1)))
    def get_filter_memory_2(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.filter_memory_2)))

    # accept filters button
    def get_filters_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.filters_button)))

    # Sorted for price (DOWN)
    def get_sort_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.sort_button)))
    def get_price_down_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.price_down_button)))

    # Product info
    def get_product_name(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.product_name)))

    def get_product_price(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.product_price)))

    # Product select
    def get_product_buy_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.product_buy_button)))

    # Cart button
    def get_cart_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.cart_button)))

    """ACTIONS"""

    # input price min/max
    def input_filter_price_1(self):
        self.action.move_to_element(self.get_filter_price_start()).perform()
        self.get_filter_price_start().clear()
        self.get_filter_price_start().send_keys('10000')
        print("Input START PRICE")
    def input_filter_price_2(self):
        self.action.move_to_element(self.get_filter_price_end()).perform()
        self.get_filter_price_end().clear()
        self.get_filter_price_end().send_keys('50000')
        print("Input START PRICE")

    # Selected Brands
    def click_filter_brand_1(self):
        self.action.move_to_element(self.get_filter_brand_1()).perform()
        self.get_filter_brand_1().click()
        print("Click filter filter_brand_1")
    def click_filter_brand_2(self):
        self.action.move_to_element(self.get_filter_brand_2()).perform()
        self.get_filter_brand_2().click()
        print("Click filter filter_brand_2")
    def click_filter_brand_3(self):
        self.action.move_to_element(self.get_filter_brand_3()).perform()
        self.get_filter_brand_3().click()
        print("Click filter filter_brand_3")
    def click_filter_brand_4(self):
        self.action.move_to_element(self.get_filter_brand_4()).perform()
        self.get_filter_brand_4().click()
        print("Click filter filter_brand_4")

    def click_filter_memory_1(self):
        self.action.move_to_element(self.get_filter_memory_1()).perform()
        self.get_filter_memory_1().click()
        print("Click filter filter_brand_4")
    def click_filter_memory_2(self):
        self.action.move_to_element(self.get_filter_memory_2()).perform()
        self.get_filter_memory_2().click()
        print("Click filter filter_brand_4")

    # Accept filters
    def click_filters_button(self):
        self.action.move_to_element(self.get_filters_button()).perform()
        self.get_filters_button().click()
        print("Click filter accept")

    # sorted for price def
    def click_sort_button(self):
        self.action.move_to_element(self.get_sort_button()).perform()
        self.get_sort_button().click()
        print("Click range to price button")
    def click_price_down_button(self):
        self.action.move_to_element(self.get_price_down_button()).perform()
        self.get_price_down_button().click()
        print("Click get price down button")

    # select product
    def click_product_buy_button(self):
        self.action.move_to_element(self.get_product_buy_button()).perform()
        self.get_product_buy_button().click()
        print("Click product buy button")

    # Click cart button
    def click_cart_button(self):
        self.action.move_to_element(self.get_cart_button()).perform()
        self.get_cart_button().click()
        print("Click CART button")


    # Methods

    def select_product(self):
        with allure.step("Select Product"):
            Logger.add_start_step("Select product")
            self.get_current_url()

            self.click_sort_button()
            self.click_price_down_button()

            self.input_filter_price_1()
            self.input_filter_price_2()

            self.click_filter_brand_1()
            self.click_filter_brand_2()
            self.click_filter_brand_3()
            self.click_filter_brand_4()

            self.click_filter_memory_1()
            self.click_filter_memory_2()

            self.click_filters_button()

            sleep(2)

            name = self.get_product_name()
            price= self.get_product_price()

            self.click_product_buy_button()
            sleep(2)
            self.information(self.get_product_name(), name)
            self.information(self.get_product_price(), price)
            sleep(2)
            self.click_cart_button()

            self.assert_url(self.url_cart)
            Logger.add_end_step(url=self.driver.current_url, method="Select product")
