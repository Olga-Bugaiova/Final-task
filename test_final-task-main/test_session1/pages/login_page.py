from .base_page import BasePage
from test_session1.locators import LoginPageLocators
from test_session1.locators import MainPageLocators
from test_session1.locators import ProductPageLocators
from selenium.common.exceptions import NoSuchElementException

import time
class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()
        self.register_new_user()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "login isn't present in url"  
        assert True

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "No login form form is presented"
        assert True

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTR_FORM), "No registr form is not presented"
        assert True
       
    def register_new_user(self, email_str, pwd_str):
        try:
            email=self.browser.find_element(*LoginPageLocators.USER_EMAIL)
            email.send_keys(email_str)
            password=self.browser.find_element(*LoginPageLocators.USER_PSW1)
            password.send_keys(pwd_str)
            password2=self.browser.find_element(*LoginPageLocators.USER_PSW2)
            password2.send_keys(pwd_str)
            button=self.browser.find_element(*LoginPageLocators.BUTTON_REG)
            button.click()
            time.sleep(15)
        except (NoSuchElementException):
            return False
        return True
  