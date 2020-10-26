from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.Email_Address_Field)
        email_field.send_keys(email)
        password_field = self.browser.find_element(*LoginPageLocators.Password_Field)
        password_field.send_keys(password)
        confirm_password = self.browser.find_element(*LoginPageLocators.Confirm_Password_Field)
        confirm_password.send_keys(password)
        self.browser.find_element(*LoginPageLocators.Register_Button).click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, "url don't have word 'login' ."

    def should_be_login_form(self):
        assert self.is_element_presented(*LoginPageLocators.Login_Form), \
            'Login form is not found on this page'

    def should_be_register_form(self):
        assert self.is_element_presented(*LoginPageLocators.Register_Form), \
            'Register form is not found on this page'
