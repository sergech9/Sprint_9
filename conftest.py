import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options 
import allure
import os

@pytest.fixture
def driver():
    selenoid_url = "http://127.0.0.1:4444/wd/hub"
    
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.set_capability("browserName", "chrome")
    options.set_capability("browserVersion", "128.0")
    
    #driver = webdriver.Chrome(options=options)

    driver = webdriver.Remote(command_executor=selenoid_url, options=options)
    yield driver
    driver.quit()

