from pages.base_page import BasePage
from urls import URLS
from locators.register_page_locators import RegisterPageLocators

class RegisterPage(BasePage):

    def open(self):
        self.driver.get(URLS.MAIN_URL)

    def click_create_account(self):
        self.click(RegisterPageLocators.CREATE_ACCOUNT_BUTTON)

    def fill_form(self, first_name, last_name, username, email, password):
        self.send_keys(RegisterPageLocators.FIRST_NAME_INPUT, first_name)
        self.send_keys(RegisterPageLocators.LAST_NAME_INPUT, last_name)
        self.send_keys(RegisterPageLocators.USERNAME_INPUT, username)
        self.send_keys(RegisterPageLocators.EMAIL_INPUT, email)
        self.send_keys(RegisterPageLocators.PASSWORD_INPUT, password)

    def submit(self):
        self.click(RegisterPageLocators.SUBMIT_BUTTON)

    def is_redirected_to_login(self):
        return self.wait.until(lambda d: "signin" in d.current_url)