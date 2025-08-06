from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest

def pytest_addoption(parser):
    parser.addoption("--language", action="store", default="en",
                     help="Choose language: en, fr, etc, ru")
    
@pytest.fixture(scope='function')
def browser(request):
    user_language = request.config.getoption("language")

    option = Options()
    option.add_experimental_option("prefs", {"intl:accept_language": user_language})

    browser = webdriver.Chrome(options=option)
    yield browser
    browser.quit()


