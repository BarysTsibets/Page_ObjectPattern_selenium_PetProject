from .pages.login_page import LoginPage
from .pages.base_page import BasePage
from .pages.basket_page import BasketPage
import pytest
import time


# promo_link = \
#     "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=midsummer"
link = "http://selenium1py.pythonanywhere.com/"



@pytest.mark.skip
def test_guest_can_go_to_login_page(browser):
    page = BasePage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

@pytest.mark.skip
def test_guest_should_see_login_link(browser):
    page = BasePage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.should_not_be_items_in_the_basket()
    page.should_be_your_basket_is_empty_message()





