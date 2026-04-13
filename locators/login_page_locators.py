from selenium.webdriver.common.by import By

class LoginPageLocators:
    LOGIN_FORM = (By.XPATH, "//form")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "a[href='/signin']")
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    SUBMIT_BUTTON = (By.XPATH, "//button[contains(text(),'Войти')]")