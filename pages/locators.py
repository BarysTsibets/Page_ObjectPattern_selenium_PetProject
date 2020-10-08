from selenium.webdriver.common.by import By


class MainPageLocators:
    Login_Link = (By.CSS_SELECTOR, "#registration_link")


class LoginPageLocators:
    Login_Form = (By.CSS_SELECTOR, "#login_form")
    Register_Form = (By.CSS_SELECTOR, '#register_form')

