from .pages.product_page import ProductPage

prod_link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'


def test_guest_can_add_item_in_basket(browser):
    prod_page = ProductPage(browser, prod_link)
    prod_page.open()
    prod_page.add_item_in_basket()
    # Getting the code from alert window
    prod_page.solve_quiz_and_get_code()
    prod_page.should_be_add_to_basket_button()
    # Item name and price confirmation
    prod_page.should_be_the_same_item_name_in_basket_and_confirmation()
    prod_page.should_match_item_price_and_item_price_in_basket()










    # open_page
    # find_add basket_button
    # click
    # solve the quz
    # SHOULD BE CHECK