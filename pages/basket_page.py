from .base_page import BasePage
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_text_that_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY), \
            "There is no text, that basket is empty"
    
    def should_not_be_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_LIST), \
            "Basket is not empty, but should be"
    
    

