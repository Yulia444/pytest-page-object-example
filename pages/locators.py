from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    USER_ICON = (By.CSS_SELECTOR, "i.icon-user")


class BasketPageLocators():
    BASKET_LINK = (By.XPATH, '//a[@class="btn btn-default"]')
    BASKET_IS_EMPTY = (By.XPATH, '//p[contains(text(),"Your basket is empty")]'
                       )
    BASKET_LIST = (By.CSS_SELECTOR, 'form.basket_summary')


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '.login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '.register_form')
    REGISTER_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTER_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTER_CONFIRM_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTER_BUTTON = (By.TAG_NAME, 'button[name="registration_submit"]')


class ProductPageLocators():
    ADD_TO_CART = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, 'div.product_main h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'div.product_main p.price_color')
    ALERT_PRODUCT_NAME = (By.XPATH, '//div[@class="alertinner "][1]/strong')
    ALERT_PRODUCT_PRICE = (By.XPATH, '//div[@class="alertinner "]/p/strong')
    SUCCESS_MESSAGE = (By.XPATH, '//div[contains(@class, "alert")][1]//div[@class="alertinner "]')