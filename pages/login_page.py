from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators


class LoginPage(BasePage):

    def click_login(self):
        self.click(LoginPageLocators.LOGIN_BUTTON)

    def fill_form(self, email, password):
        self.send_keys(LoginPageLocators.EMAIL_INPUT, email)
        self.send_keys(LoginPageLocators.PASSWORD_INPUT, password)

    def submit(self):
        self.click(LoginPageLocators.SUBMIT_BUTTON)

    def is_login_form_visible(self):
        return self.find(LoginPageLocators.LOGIN_FORM).is_displayed()
    
    def login(self, email, password):
        self.click(LoginPageLocators.LOGIN_BUTTON)
        self.fill_form(email, password)
        self.submit()