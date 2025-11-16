from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from .base_page import BasePage


class StatsPage(BasePage):
    NAVBAR = (By.XPATH, '//android.widget.TextView[@text="Statistics"]')
    ACTIVE_LABEL = (By.XPATH, '//android.widget.TextView[contains(@text,"Active tasks")]')
    COMPLETED_LABEL = (By.XPATH, '//android.widget.TextView[contains(@text,"Completed tasks")]')

    def get_active_percentage(self):
        label = WebDriverWait(self.driver, 10).until(lambda d: d.find_element(*self.ACTIVE_LABEL))
        return label.text

    def get_completed_percentage(self):
        label = WebDriverWait(self.driver, 10).until(lambda d: d.find_element(*self.COMPLETED_LABEL))
        return label.text
