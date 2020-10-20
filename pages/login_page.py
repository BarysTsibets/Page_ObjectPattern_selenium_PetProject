from pages.base_page import BasePage
from pages.locators import LoginPageLocators
import faker

link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer'


def fake_email_creator():
    f = faker.Faker()
    mail = f.mail()
    return mail


EMAIL_1 = fake_email_creator()
PASW_1 = '123qwe!@#'


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.Email_Address_Field)
        email_field.send_key(email)
        password_field = self.browser.find_element(*LoginPageLocators.Password_Field)
        password_field.send_key(password)
        confirm_password = self.browser.find_element(*LoginPageLocators.Confirm_Password_Field)
        confirm_password.send_key(password)
        self.browser.find_element(*LoginPageLocators.Register_Button).click()

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
