from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def open(self, url):
        self.driver.get(url)

    def find(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def click_action(self, locator):
        element = self.find(locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()

    def send_keys(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def text_input(self, locator, text):
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

    def wait_for_text_to_be_present(self, locator, text):
        try:
            self.wait.until(
                EC.text_to_be_present_in_element(locator, text)
            )
            return True
        except TimeoutException:
            return False
        
    def refresh(self):
        self.driver.refresh()

    def select_from_dropdown(self, input_locator, item_locator, text):

        self.click(input_locator)
        self.send_keys(input_locator, text)
        self.wait.until(EC.visibility_of_any_elements_located(item_locator))
        self.click(item_locator)

    def wait_for_text_in_elements(self, locator, text):
        try:
            self.wait.until(
                lambda driver: any(text in el.text for el in driver.find_elements(*locator))
            )
            return True
        except TimeoutException:
            self.driver.refresh()
            return False