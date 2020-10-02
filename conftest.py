import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


PATH1 = r'C:\Users\BorisPC\PycharmProjects\untitled\HelloWorld\StepikProject\driver\chromedriver.exe'
PATH2 = r'C:\Users\BorisPC\PycharmProjects\untitled\HelloWorld\StepikProject\driver\geckodriver.exe'


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: es, en,...(etc.) ")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    if browser_name == "chrome":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        print(f"\n Chrome browser starting...")
        browser = webdriver.Chrome(executable_path=PATH1, options=options)
    elif browser_name == "firefox":
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        print(f"\n Mozila browser starting...")
        browser = webdriver.Firefox(executable_path=PATH2, firefox_profile=fp)
    else:
        print(f"Browser <browser name> still not implemented")
    yield browser
    print("\nquit browser..")
    browser.quit()