import pytest
import time

from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage

#the class checks login tests set
@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/"
        page = MainPage(browser, link)# инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        page.open()             # открываем страницу
        page.go_to_login_page()
        

    def test_guest_should_see_login_link(self, browser):    
        link = "http://selenium1py.pythonanywhere.com/en-gb/"
        page = MainPage(browser, link)
        page.open()   
        page.go_to_login_page()        
        page.should_be_login_url()

@pytest.mark.xfail    
def test_guest_check_wrong_link(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/"
    page = MainPage(browser, browser.current_url)
    page.open()
    page.should_be_login_link()


@pytest.mark.parametrize('link', [0, 1, 2, 3, 4, 5, 6,
                                   pytest.param(7, marks=pytest.mark.xfail), 8,9])
                             
def test_guest_can_add_product_to_basket(browser, link):
    product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    urls = [f"product_base_link/?promo=offer{link}" for link in range(10)]

#the test checks that there is no any selected books in the basket
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/"
        page=BasketPage(browser,link)
        page.open()
        page.should_not_see_product_in_basket()
        page.should_see_empty_basket_note()
        