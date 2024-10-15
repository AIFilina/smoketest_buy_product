from time import sleep

import allure

from pages.check_out_page import Check_out_page
from pages.main_page import Main_page
from pages.select_product_page import Select_product_page
from tests.conftest import driver

@allure.description("Test buy product 1")
def test_buy_smartphone(driver):
    print("Start test buy 'Товар из категории Смартфоны'")

    # select category
    sc = Main_page(driver)
    sc.select_category()

    # Select product

    sp = Select_product_page(driver)
    sp.select_product()
    #payment
    co = Check_out_page(driver)
    co.payment_product()


    print("Finish test buy 'Товар из категории Смартфоны'")
    sleep(2)