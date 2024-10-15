

from faker import Faker
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

from utilites.logger import Logger


class Check_out_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    fake = Faker()

    # locators

    cart_product_name = '//*[@id="checkout-review-table"]/div[1]/div/div[2]/div'
    cart_product_price = '//*[@id="checkout-review-table"]/div[2]/div[3]/div[2]/span'

    input_city = '//*[@id="select2-order-city_fias_id-container"]'

    delivery_button = '//*[@id="order-delivery_method"]/div[3]/label'

    user_name = '//input[@id="order-first_name"]'
    user_last_name = '//input[@id="order-last_name"]'
    user_phone = '//input[@id="order-phone"]'
    user_mail = '//input[@id="order-email"]'

    address = '//*[@id="deliveryself-storage_id"]/div[2]'

    payment = '//*[@id="order-payment_method"]/div[1]/label/span'

    '''GETTERS'''

    # info product
    def get_cart_product_name(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.cart_product_name)))

    def get_cart_product_price(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.cart_product_price)))

    # city
    def get_input_city(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.input_city)))

    #delivery_button
    def get_delivery_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.delivery_button)))

    #user info
    def get_user_name(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.user_name)))

    def get_user_last_name(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.user_last_name)))

    def get_user_phone(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.user_phone)))

    def get_user_mail(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.user_mail)))

    # address to delivery
    def get_address(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.address)))

    # payment
    def get_payment(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.payment)))

    '''ACTIONS'''

    def click_get_delivery_button(self):
        self.action.move_to_element(self.get_delivery_button()).perform()
        self.get_delivery_button().click()
        print("Click delivery button")

    def input_user_name(self):
        self.action.move_to_element(self.get_user_name()).perform()
        self.get_user_name().clear()
        self.get_user_name().send_keys(self.fake.first_name())
        print("Input NAME")

    def input_user_last_name(self):
        self.action.move_to_element(self.get_user_last_name()).perform()
        self.get_user_last_name().clear()
        self.get_user_last_name().send_keys(self.fake.last_name())
        print("Input LAST NAME")

    def input_user_phone(self):
        self.action.move_to_element(self.get_user_phone()).perform()
        self.get_user_phone().clear()
        self.get_user_phone().send_keys(self.fake.phone_number()[2:])
        print("Input PHONE")

    def input_user_mail(self):
        self.action.move_to_element(self.get_user_mail()).perform()
        self.get_user_mail().clear()
        self.get_user_mail().send_keys(self.fake.email())
        print("Input Mail")

    def click_address(self):
        self.action.move_to_element(self.get_address()).perform()
        self.get_address().click()
        print("Click address")

    def click_payment(self):
        self.action.move_to_element(self.get_payment()).perform()
        self.get_payment().click()
        print("Click payment")

    """METHODS"""

    def payment_product(self):
        Logger.add_start_step("PAYMENT product")

        self.get_current_url()

        self.assert_word(self.get_cart_product_name(),"Смартфон Samsung Galaxy A55 5G 8/256Gb Awesome Lemon (Желтый)")
        self.assert_word(self.get_cart_product_price(),"36090 руб.")

        self.click_get_delivery_button()
        self.input_user_name()
        self.input_user_last_name()
        self.input_user_phone()
        self.input_user_mail()
        self.click_address()
        self.click_payment()

        Logger.add_end_step(url=self.driver.current_url, method="Select product")

