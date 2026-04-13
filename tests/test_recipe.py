import random
from pages.login_page import LoginPage
from pages.recipe_page import RecipePage
from data.data import Data
from urls import URLS
import time


class TestRecipe:

    def test_create_recipe(self, driver):
        login_page = LoginPage(driver)
        recipe_page = RecipePage(driver)

        login_page.open(URLS.SIGNIN_URL)
        login_page.login(
            Data.TEST_USER["email"],
            Data.TEST_USER["password"]
        )

        recipe_page.open_create_recipe()

        recipe_name = f"recipetest{random.randint(1,9999)}"

        recipe_page.fill_basic_info(
            name=recipe_name,
            description="Описание",
            time=random.randint(1,999)
        )

        recipe_page.add_ingredient("ван", 7)
        recipe_page.upload_image()
        recipe_page.submit()

        time.sleep(10)
        recipe_page.open(URLS.RECIPES_URL)
        
        time.sleep(5)
        assert recipe_page.is_recipe_card_present()
        assert recipe_page.is_recipe_with_name_present(recipe_name)