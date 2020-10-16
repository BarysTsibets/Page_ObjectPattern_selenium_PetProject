from .base_page import BasePage
from .locators import BasketPageLocators
# from .locators import ProductPageLocators


class BasketPage(BasePage):
    def should_not_be_items_in_the_basket(self):
        assert self.is_not_element_presented(*BasketPageLocators.Basket_Added_Items), \
            'Item(s) shown in the basket, but was not added'

    def should_be_your_basket_is_empty_message(self):
        assert self.is_element_presented(*BasketPageLocators.Empty_Basket_Message), \
            '(Yor basket is empty) message not shown'

