from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from test_session1.locators import MainPageLocators
from .login_page import LoginPage

class MainPage(BasePage):
    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click() 
    
    def should_be_login_link(self):
        assert self.is_element_present(By.CSS_SELECTOR, "#login_link"), "Login link is not presented"
    
    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "login isn't present in url"  
        assert True    
