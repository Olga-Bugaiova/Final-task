from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    VIEW_BASKET= (By.CSS_SELECTOR, "[class='btn-group']>a")
    EMPTY_BASKET =(By.XPATH, "//*[@id='content_inner']/p/text()")
    ITEM_BASKET = (By.CSS_SELECTOR, "[class='row'] >h2")
    NOTE=(By.CSS_SELECTOR,"#content_inner>p")
	
class LoginPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")    
    REGISTR_FORM =(By.CSS_SELECTOR, "#register_form")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    USER_EMAIL = (By.CSS_SELECTOR, "[name='registration-email']")
    USER_PSW1 = (By.CSS_SELECTOR, "[name='registration-password1']")
    USER_PSW2 = (By.CSS_SELECTOR, "[name='registration-password2']")
    BUTTON_REG = (By.CSS_SELECTOR, "[name='registration_submit']")

class ProductPageLocators():
    BASKET_PAGE= (By.XPATH, "//*[@class='active']/text()")
    BASCKET_ADD_BUTTON = (By.CSS_SELECTOR, "[value='Add to basket']")
    NOTE_ADDED_PRODUCT = (By.CSS_SELECTOR, "#messages :nth-child(2) >strong") 
    SELECTED_BOOK = (By.CSS_SELECTOR, "[class ='col-sm-6 product_main']>h1")
    BOOK_PRICE = (By.CSS_SELECTOR, "[class='col-sm-6 product_main']>p") 
    SELECTED_BOOK_PRICE = (By.CSS_SELECTOR, ".alertinner >p >strong")