from .main_page import MainPage
from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math

class ProductPage(BasePage):
    def add_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.basket_button)
        add_button.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
    
    def alert_book_name_in_basket(self):
        path_book = self.browser.find_element(*ProductPageLocators.book_info)
        book_name = path_book.find_element(*ProductPageLocators.book_name)

        path_alert = self.browser.find_element(*ProductPageLocators.alert_str)
        alert_book_name = path_alert.find_element(*ProductPageLocators.alert_book_name)

        assert book_name.text == alert_book_name.text, "Именна книг не совпадают"