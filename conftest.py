import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language example: es")

@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    if user_language:
        print("\nstart chrome browser for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    else:
        raise pytest.UsageError("--language is required param")
    yield browser
    print("\nquit browser..")
    browser.quit()