from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators
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


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    prod_page = ProductPage(browser, prod_link)
    prod_page.open()
    prod_page.add_item_in_basket()
    time.sleep(2)
    result = prod_page.is_not_element_presented(*ProductPageLocators.SUCCESS_MESSAGE)
    assert result is True, 'Guest_can_see_success_message_after_adding_product_to_basket'


def test_guest_cant_see_success_message(browser):
    prod_page2 = ProductPage(browser, prod_link)
    prod_page2.open()
    result = prod_page2.is_not_element_presented(*ProductPageLocators.SUCCESS_MESSAGE)
    assert result is True, "Guest can see success message"


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    prod_page3 = ProductPage(browser, prod_link)
    prod_page3.open()
    prod_page3.add_item_in_basket()
    result = prod_page3.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE)
    assert result is True, "Message disappeared after adding product to basket"

