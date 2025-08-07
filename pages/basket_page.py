from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    
    def go_to_basket(self):
        basket_button = self.browser.find_element(*BasketPageLocators.button)
        button_link = basket_button.find_element(*BasketPageLocators.basket_link)
        button_link.click()

    def should_see_basket_empty(self):
        basket_text = self.browser.find_element(*BasketPageLocators.basket_text)
        print(basket_text.text)
        assert basket_text.text == "Your basket is empty. Continue shopping", f"Текст в плажке {basket_text.text}"