import time
import pytest

from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from test_session1.locators import MainPageLocators
from selenium.common.exceptions import NoAlertPresentException

# the class combines test for a user
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)       
    def setup(self,browser):    
        print("\nstart browser for test suite..")
        link= "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        page=LoginPage(browser,link)
        page.open()
        email = str(time.time()) + "@fakemail.org"
        page.register_new_user(email,"SRKqa123456")
        time.sleep(5)
        page.should_be_authorized_user()

#the test checks that a user see that there is no success message if he not adds a book to the basket       
    def test_user_cant_see_success_message(self, browser):
        link= "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/"
        page=BasketPage(browser, link)
        page.open()    
        page.should_not_be_note_about_added_book()
        
#the test checks that a user can add a book to the basket and see a success message. 
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.should_be_opened_book()   
        product_page.should_be_pushed_basket_button()        
        product_page.should_be_note_about_added_book()


        
        
#the test checks that a guest can see Login page 
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link

#the test checks that a guest can open Login page from Product page  
@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_go_to_login_page()

#the test checks that a guest can't see success message when he open book catalogue
def test_guest_cant_see_success_message(browser):
    link= "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/"
    page=BasketPage(browser, link)
    page.open()    
    page.should_not_be_note_about_added_book()

#the test checks that a guest can see the same book's name in according to selected book    
def test_guest_can_see_thesame_book(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_pushed_basket_button()  
    product_page.should_be_thesame_name_book()
    
#the test checks that a guest can see price of a book on a catalogue
def test_guest_can_see_price_of_book(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser, link)
    product_page.open() 
    product_page.should_be_price_for_book()

#the test checks that a guest can see the same book's price in according to selected book 
def test_guest_can_see_thesame_price(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_pushed_basket_button()  
    product_page.should_be_price_thesame_for_book()
    time.sleep(5)

#the test checks that a guest can't see success message when he added a book to the basket
@pytest.mark.xfail 
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link= "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/"
    page=BasketPage(browser, link)
    page.open()
    page.should_be_pushed_basket_button()
    page.should_not_be_success_message()

#the test checks that a guest can add a book to the basket
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser, link) 
    product_page.open()
    product_page.should_be_opened_book()   
    product_page.should_be_pushed_basket_button()        
    product_page.should_be_note_about_added_book()


#the test checks that a guest can see that success message about adding a book disappeared    
@pytest.mark.skip(reason="no way of currently testing this")    
def test_message_disappeared_after_adding_product_to_basket(browser):
    link= "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/"
    page=BasketPage(browser, link)
    page.open()
    page.should_be_pushed_basket_button()
    page.should_disappeared_be_note_about_added_book()


#the test checks that a guest can see Login in url
def test_guest_can_see_login_url(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_url()

#the test checks that a guest can see empty basket
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/"
    page=BasketPage(browser,link)
    page.open()
    time.sleep(5)
    page.should_not_see_product_in_basket()
    page.should_see_empty_basket_note()





        