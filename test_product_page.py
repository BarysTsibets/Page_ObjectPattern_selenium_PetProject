from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators
from .pages.basket_page import BasketPage
import time
import pytest

# The shellcoder's handbook" book
prod_link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/'
# "Coders at work" book
prod_link2 = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
# Promo page
prod_link3 = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


@pytest.mark.skip
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param(
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                      marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_item_in_basket(browser, link):
    prod_page = ProductPage(browser, link)
    prod_page.open()
    prod_page.add_item_in_basket()
    # Getting the code from alert window
    prod_page.solve_quiz_and_get_code()
    prod_page.should_be_add_to_basket_button()
    # Item name and price confirmation
    prod_page.should_be_the_same_item_name_in_basket_and_in_confirmation()
    prod_page.should_match_item_price_and_item_price_in_confirmation()


# @pytest.mark.skip
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    prod_page = ProductPage(browser, prod_link)
    prod_page.open()
    prod_page.add_item_in_basket()
    prod_page.should_not_be_success_message()


# @pytest.mark.skip
def test_guest_cant_see_success_message(browser):
    prod_page = ProductPage(browser, prod_link)
    prod_page.open()
    prod_page.should_not_be_success_message()


# @pytest.mark.skip
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    prod_page = ProductPage(browser, prod_link)
    prod_page.open()
    prod_page.add_item_in_basket()
    prod_page.should_be_disappeared_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    prod_page = ProductPage(browser, link)
    prod_page.open()
    prod_page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    prod_page = ProductPage(browser, link)
    prod_page.open()
    prod_page.go_to_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    prod_page = ProductPage(browser, prod_link)
    prod_page.open()
    prod_page.go_to_basket_page()
    # BasketPage.should_not_be_items_in_the_basket()
    prod_page.should_not_be_items_in_the_basket()
    prod_page.should_be_your_basket_is_empty_message()

