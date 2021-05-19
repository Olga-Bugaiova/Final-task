from .base_page import BasePage
from test_session1.locators import ProductPageLocators
from test_session1.locators import MainPageLocators
from test_session1.locators import LoginPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math
import time
 
class ProductPage(BasePage):
    def should_be_basket_page(self):        
        self.should_go_to_login_page()
        self.should_be_opened_book()   
        self.should_be_pushed_basket_button()        
        self.should_be_note_about_added_book()
        self.should_be_thesame_name_book()
        self.should_be_price_for_book()
        self.should_be_price_thesame_for_book()
        #self.solve_quiz_and_get_code()
    
    def should_go_to_login_page(self):
        login_form=self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_form.click()
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "No login link is presented"
   
        
    def should_be_opened_book(self):
        basket_button = self.browser.find_element(*ProductPageLocators.SELECTED_BOOK)         
        assert self.is_element_present(*ProductPageLocators.SELECTED_BOOK),"No any book opened" 
        
    def should_be_pushed_basket_button(self):
        basket_button = self.browser.find_element(*ProductPageLocators.BASCKET)
        basket_button.click()         
        assert True       

    def should_be_note_about_added_book(self): 
        assert self.is_element_present(*ProductPageLocators.NOTE_ADDED_PRODUCT), "No notification about adding product"        
        assert True
        
    def should_be_thesame_name_book(self):
        book = self.browser.find_element(*ProductPageLocators.NOTE_ADDED_PRODUCT)    
        book_name=book.text
        assert book_name in self.browser.find_element(*ProductPageLocators.SELECTED_BOOK).text, "The book is dif"
        assert True       
    
    def should_be_price_for_book(self):
        price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE)    
        assert self.is_element_present(*ProductPageLocators.BOOK_PRICE), "No book price"
        assert True
    
    def should_be_price_thesame_for_book(self):
        selected_price = self.browser.find_element(*ProductPageLocators.SELECTED_BOOK_PRICE)    
        price_text=selected_price.text
        assert price_text in self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text, "Price isn't the same"
        assert True
    
        
    # def solve_quiz_and_get_code(self):
        # alert = self.browser.switch_to.alert
        # x = alert.text.split(" ")[2]
        # answer = str(math.log(abs((12 * math.sin(float(x))))))
        # alert.send_keys(answer)
        # alert.accept()
        # time.sleep(2)
        # try:
            # alert = self.browser.switch_to.alert
            # alert_text = alert.text
            # print(f"Your code: {alert_text}")
            # alert.accept()
        # except NoAlertPresentException:
            # print("No second alert presented")
        # time.sleep(2)