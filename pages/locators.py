from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")



class LoginPageLocators():
    URL = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGIST_FORM = (By.CSS_SELECTOR, "#registr_form")


class ProductPageLocators():
    basket_button = (By.CSS_SELECTOR, ".btn-add-to-basket")
    alert_str = (By.CSS_SELECTOR, ".alertinner")
    alert_book_name = (By.TAG_NAME, "strong")
    book_info = (By.CSS_SELECTOR, ".product_main")
    book_name = (By.TAG_NAME, 'h1')
