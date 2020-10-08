from pages.base_page import BasePage
from pages.locators import LoginPageLocators

link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer'


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert 'login' in self.browser.current_url, "url don't have word 'login' ."

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_presented(*LoginPageLocators.Login_Form), \
            'Login form is not found on this page'

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_presented(*LoginPageLocators.Register_Form), \
            'Register form is not found on this page'
