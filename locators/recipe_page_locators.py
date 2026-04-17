from selenium.webdriver.common.by import By

class RecipePageLocators:
    CREATE_RECIPE_TAB = (By.XPATH, "//a[contains(text(),'Создать рецепт')]")
    
    RECIPE_NAME = (By.XPATH, "//label[.//div[text()='Название рецепта']]//input")
    INGREDIENT_NAME = (By.XPATH, "//div[contains(text(),'Ингредиенты')]/ancestor::label//input")
    INGREDIENT_DROPDOWN_ITEM = (By.CSS_SELECTOR, ".styles_container__3ukwm div")
    INGREDIENT_AMOUNT = (By.XPATH, "//input[contains(@class,'ingredientsAmountValue')]")
    ADD_INGREDIENT_BUTTON = (By.XPATH, "//div[text()='Добавить ингредиент']")
    COOKING_TIME = (By.XPATH, "//div[text()='Время приготовления']/ancestor::label//input")
    DESCRIPTION = (By.XPATH, "//textarea")
    FILE_INPUT = (By.XPATH, "//input[@type='file']")

    CREATE_RECIPE_BUTTON = (By.XPATH, "//button[text()='Создать рецепт']")
    RECIPE_TITLE = (By.XPATH, "//h1")
    
    RECIPE_CARDS = (By.CSS_SELECTOR, "a[href^='/recipes/']")