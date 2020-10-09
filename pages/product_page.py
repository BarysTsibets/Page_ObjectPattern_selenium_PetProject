from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_item_in_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.Add_Basket_Button)
        add_to_basket_button.click()

    def should_be_add_to_basket_button(self):
        assert self.is_element_presented(*ProductPageLocators.Add_Basket_Button),\
            'No "Add to basket button" presented on this page'

    def should_be_the_same_item_name_in_basket_and_confirmation(self):
        item_name = self.browser.find_element(*ProductPageLocators.Item_Name)
        conf_item = self.browser.find_element(*ProductPageLocators.Item_Name_Confirm_Message)
        assert item_name.text == conf_item.text, \
            'Another item name in confirmation message'

    def should_match_item_price_and_item_price_in_basket(self):
        item_price = self.browser.find_element(*ProductPageLocators.Item_Price)
        item_price_basket = self.browser.find_element(*ProductPageLocators.Item_Price_In_Message)
        # print(item_price.text)
        # print(item_price_basket.text)
        assert item_price.text == item_price_basket.text,\
            "Item price and Item Price in confirmation message different"








