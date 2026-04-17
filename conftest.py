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

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    
    # Нас интересует только момент падения самого теста (этап call)
    if rep.when == 'call' and rep.failed:
        try:
            # Пытаемся взять драйвер из теста
            driver = item.funcargs.get('driver')
            if driver:
                # 1. Прикрепляем в Allure
                allure.attach(
                    driver.get_screenshot_as_png(),
                    name=f"failure_{item.name}",
                    attachment_type=allure.attachment_type.PNG
                )
                
                # 2. Сохраняем как файл (для GitHub Actions Artifacts)
                # Создаем папку, если ее нет
                if not os.path.exists("screenshots"):
                    os.makedirs("screenshots")
                driver.save_screenshot(f"screenshots/fail_{item.name}.png")
        except Exception as e:
            print(f"Не удалось сделать скриншот: {e}")