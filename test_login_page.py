from .pages.login_page import LoginPage

log_link = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'


# Login page tests
def test_guest_should_see_register_form(browser):
    log_page = LoginPage(browser, log_link)
    log_page.open()
    log_page.should_be_register_form()


def test_guest_should_see_login_form(browser):
    log_page = LoginPage(browser, log_link)
    log_page.open()
    log_page.should_be_login_form()


def test_link_should_be_login_url(browser):
    log_page = LoginPage(browser, log_link)
    log_page.open()
    log_page.should_be_login_url()


def test_should_be_login_page(browser):
    log_page = LoginPage(browser, log_link)
    log_page.open()
    log_page.should_be_login_page()
