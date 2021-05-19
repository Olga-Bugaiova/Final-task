from .base_page import BasePage
from test_session1.locators import ProductPageLocators
from test_session1.locators import MainPageLocators
from test_session1.locators import LoginPageLocators
from selenium.common.exceptions import NoAlertPresentException


        
class BasketPage(BasePage):
    def should_be_basket_page(self):               
        self.should_be_basket_button()
        self.should_be_pushed_basket_button()
        self.should_not_be_success_message()
        self.should_be_note_about_added_book()
        self.should_disappeared_be_note_about_added_book()
        self.should_not_see_product_in_basket()
        self.should_see_empty_basket_note()


    
    def should_be_basket_button(self):
         # реализуйте проверку, что есть кнопка "Добавить в корзину"
        assert self.is_element_present(*ProductPageLocators.BASCKET_ADD_BUTTON), "No basket button is presented"  
    
    def should_be_pushed_basket_button(self):
        basket_button = self.browser.find_element(*ProductPageLocators.BASCKET_ADD_BUTTON)
        basket_button.click()
           
        
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.NOTE_ADDED_PRODUCT), "Success message is presented, but should not be"        
            
    def should_not_be_note_about_added_book(self): 
        assert self.is_not_element_present(*ProductPageLocators.NOTE_ADDED_PRODUCT), "No notification about adding product"        
        assert True
        
    def should_disappeared_be_note_about_added_book(self): 
        assert self.is_disappeared(*ProductPageLocators.NOTE_ADDED_PRODUCT), "No notification about adding product"        
        assert True
    
    def should_not_see_product_in_basket(self):
        assert self.open_basket_page(*MainPageLocators.VIEW_BASKET), "no basket page"
        assert self.is_not_element_present(*MainPageLocators.ITEM_BASKET), "No items to buy now"
        assert True
    
    def should_see_empty_basket_note(self):
        note= self.browser.find_element(*MainPageLocators.NOTE)
        assert self.is_element_present(*MainPageLocators.NOTE), "Basket is not empty notificaton"   
    