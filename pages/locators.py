from selenium.webdriver.common.by import By


class BasePageLocators:
    Login_Link = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    Basket_Link = (By.CSS_SELECTOR, '[class="btn-group"]>[class="btn btn-default"]')


class BasketPageLocators:
    Basket_Added_Items = (By.CSS_SELECTOR, '[class="basket-items"]')
    Empty_Basket_Message = (By.CSS_SELECTOR, '[id="content_inner"]>p')


class LoginPageLocators:
    Login_Form = (By.CSS_SELECTOR, "#login_form")
    Register_Form = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators:
    Add_Basket_Button = (By.CSS_SELECTOR, '[value="Add to basket"]')
    Item_Name_Confirm_Message = (By.XPATH, '//div[@id="messages"]/div[1]/div[1]/strong')
    Item_Name = (By.CSS_SELECTOR, '[class="col-sm-6 product_main"]>h1')
    Item_Price = (By.CSS_SELECTOR, 'p[class="price_color"]')
    Item_Price_In_Message = (By.XPATH, '//div[@id="messages"]/div[3]/div/p/strong')
    SUCCESS_MESSAGE = (By.XPATH, '//div[@id="messages"]/div[1]/div[1]')
