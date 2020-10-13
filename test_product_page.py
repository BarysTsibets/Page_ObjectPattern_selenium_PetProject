from .pages.product_page import ProductPage
import pytest

# The shellcoder's handbook" book
prod_link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
# "Coders at work" book
prod_link2 = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
# Promo page
prod_link3 = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"


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

    # open_page
    # find_add basket_button
    # click
    # solve the quz
    # SHOULD BE CHECK
