from selenium.webdriver.common.by import By
from .base_page import BasePage


class StatisticsPage(BasePage):
    NAVBAR = (By.XPATH, '//android.widget.TextView[@text="Statistics"]')
    ACTIVE_LABEL = (By.XPATH, '//android.widget.TextView[starts-with(@text, "Active tasks:")]')
    COMPLETED_LABEL = (By.XPATH, '//android.widget.TextView[starts-with(@text, "Completed tasks:")]')

    def get_active_percentage(self):
        el = self.driver.find_element(*self.ACTIVE_LABEL)
        return el.text

    def get_completed_percentage(self):
        el = self.driver.find_element(*self.COMPLETED_LABEL)
        return el.text

    def get_navbar_title(self):
        return self.driver.find_element(*self.NAVBAR).text
