import random
from pages.register_page import RegisterPage
from pages.login_page import LoginPage


class TestRegister:

    def test_success_register_redirect(self, driver):
        register_page = RegisterPage(driver)

        register_page.open()
        register_page.click_create_account()

        register_page.fill_form(
            first_name=f"test{random.randint(1,999)}",
            last_name=f"test{random.randint(1,999)}",
            username=f"test{random.randint(1,999)}",
            email=f"test{random.randint(1,999)}@test.com",
            password=f"password{random.randint(1,999)}"
        )

        register_page.submit()

        assert register_page.is_redirected_to_login()


    def test_success_register_login_form_visible(self, driver):
        register_page = RegisterPage(driver)
        login_page = LoginPage(driver)

        register_page.open()
        register_page.click_create_account()

        register_page.fill_form(
            first_name=f"test{random.randint(1,999)}",
            last_name=f"test{random.randint(1,999)}",
            username=f"test{random.randint(1,999)}",
            email=f"test{random.randint(1,999)}@test.com",
            password=f"password{random.randint(1,999)}"
        )

        register_page.submit()

        assert login_page.is_login_form_visible()
