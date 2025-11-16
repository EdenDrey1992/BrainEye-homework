from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator)).click()

    def send_keys(self, locator, text, timeout=10):
        el = WebDriverWait(self.driver, timeout).until(lambda d: d.find_element(*locator))
        el.clear()
        el.send_keys(text)

    def get_text(self, locator, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            lambda d: d.find_element(*locator)
        )
        return element.text