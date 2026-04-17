from pages.login_page import LoginPage
from pages.main_page import MainPage
from data.data import Data
from urls import URLS


class TestLogin:

    def test_login_redirect(self, driver):
        login_page = LoginPage(driver)
        main_page = MainPage(driver)

        login_page.open(URLS.SIGNIN_URL)
        login_page.login(
            Data.TEST_USER["email"],
            Data.TEST_USER["password"]
        )

        assert main_page.is_main_page()


    def test_login_logout_button(self, driver):
        login_page = LoginPage(driver)
        main_page = MainPage(driver)

        login_page.open(URLS.SIGNIN_URL)
        login_page.login(
            Data.TEST_USER["email"],
            Data.TEST_USER["password"]
        )

        assert main_page.is_logout_button_visible()