from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, url):
        self.driver.get(url)

    def find(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        self.find(locator).click()

    def click_action(self, locator):
        element = self.find(locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()

    def send_keys(self, locator, value):
        self.find(locator).send_keys(value)

    def select_ingredient(self, locator, text):
        element = self.find(locator)
        actions = ActionChains(self.driver)

        actions.click(element)
        actions.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL)
        actions.send_keys(Keys.DELETE)

        actions.send_keys(text)
        actions.perform()

    def click_first_dropdown_item(self, locator):
        items = self.wait.until(
            EC.visibility_of_all_elements_located(locator))
        items[0].click()

    def upload_file(self, locator, file_path):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(locator)
        )
        element.send_keys(file_path)
        
    def is_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def is_displayed(self, locator):
        try:
            return self.is_visible(locator).is_displayed()
        except:
            return False
