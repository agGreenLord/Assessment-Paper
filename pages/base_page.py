from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from .locators import BasePageLocators

class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
    
    def open(self):
        self.browser.get(self.url) 
        
    def is_element_present(self, how, what):
        try: 
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True
    
    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def should_be_logim_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not present"
        