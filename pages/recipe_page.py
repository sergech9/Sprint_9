from pages.base_page import BasePage
from locators.recipe_page_locators import RecipePageLocators
from pathlib import Path

class RecipePage(BasePage):

    def open_create_recipe(self):
        self.click(RecipePageLocators.CREATE_RECIPE_TAB)

    def fill_basic_info(self, name, description, time):
        self.send_keys(RecipePageLocators.RECIPE_NAME, name)
        self.send_keys(RecipePageLocators.DESCRIPTION, description)
        self.send_keys(RecipePageLocators.COOKING_TIME, time)

    def add_ingredient(self, name, amount):
        self.text_input(RecipePageLocators.INGREDIENT_NAME, name)
        self.click_first_dropdown_item(RecipePageLocators.INGREDIENT_DROPDOWN_ITEM)
        self.send_keys(RecipePageLocators.INGREDIENT_AMOUNT, amount)
        self.click(RecipePageLocators.ADD_INGREDIENT_BUTTON)

    def upload_image(self):
        file_path = Path(__file__).resolve().parent.parent / "data" / "image.jpg"
        self.upload_file(RecipePageLocators.FILE_INPUT, str(file_path))

    def submit(self):
        self.click(RecipePageLocators.CREATE_RECIPE_BUTTON)

    def is_recipe_card_present(self):
        return self.is_displayed(RecipePageLocators.RECIPE_CARDS)

    def is_recipe_with_name_present(self, name):
        return self.wait_for_text_in_elements(RecipePageLocators.RECIPE_CARDS, name)