from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_cart(self):
        add_to_cart = self.browser.find_element(*ProductPageLocators.
                                                ADD_TO_CART)
        add_to_cart.click()
    
    def should_be_add_to_cart_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_CART), \
            "Adding to cart is not present"
    
    def should_not_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is disappeared, but should not be"
    
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.
                                           SUCCESS_MESSAGE), \
            "Success message is displayed, but should not be"
    
    def should_be_added_to_cart(self):
        product_price = self.browser.find_element(*ProductPageLocators.
                                                  PRODUCT_PRICE).text
        product_name = self.browser.find_element(*ProductPageLocators.
                                                 PRODUCT_NAME).text

        in_basket_product_price = self.browser.\
            find_element(*ProductPageLocators.ALERT_PRODUCT_PRICE).text
        in_basket_product_name = self.browser.\
            find_element(*ProductPageLocators.ALERT_PRODUCT_NAME).text
        if_added_to_cart = product_name == in_basket_product_name \
            and product_price == in_basket_product_price

        assert if_added_to_cart, f"{product_name} is not added to cart"
