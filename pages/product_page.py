from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_login_page(self):
        # наличие кнопки добавить в корзину
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BUCKET_BUTTON), "Add to bucket button is not presented"

    def should_be_promo(self):
        # наличие промокода
        assert "promo" in self.browser.current_url, "Promo is not presented"
    
    def add_to_bucket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BUCKET_BUTTON)
        button.click()
    
    def equal_price(self):
        price = self.browser.find_element(*ProductPageLocators.PRICE)
        message_price = self.browser.find_element(*ProductPageLocators.MESSAGE_PRICE)
        assert price.text == message_price.text, "Price is incorrect!"

    def should_be_right_message(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        message_name = self.browser.find_element(*ProductPageLocators.MESSAGE_NAME)
        assert product_name.text == message_name.text, "Message is incorrect!"
    
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_NAME), \
       "Success message is presented, but should not be"
    
    def should_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_NAME), \
       "Success message is disappeared, but should not be"
