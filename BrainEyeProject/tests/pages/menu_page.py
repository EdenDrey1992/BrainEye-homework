from selenium.webdriver.common.by import By
from .base_page import BasePage


class MenuPage(BasePage):
    TASK_LIST_BUTTON = (By.XPATH, '//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.Button')
    STATISTICS_BUTTON = (By.XPATH, '//android.widget.TextView[@text="Statistics"]')

    def go_to_task_list(self):
        self.click(self.TASK_LIST_BUTTON)

    def go_to_statistics(self):
        self.click(self.STATISTICS_BUTTON)
