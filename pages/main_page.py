from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    def is_logout_button_visible(self):
        return self.find(MainPageLocators.LOGOUT_BUTTON).is_displayed()
    
    def is_main_page(self):
        return self.wait.until(lambda d: "/recipes" in d.current_url)