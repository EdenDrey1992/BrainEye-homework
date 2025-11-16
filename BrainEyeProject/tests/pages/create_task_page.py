from selenium.webdriver.common.by import By
from .base_page import BasePage

class CreateTaskPage(BasePage):
    NAVBAR = (By.XPATH, '//android.widget.TextView[@text="New Task"]')
    TITLE_INPUT = (By.XPATH, '//android.widget.ScrollView/android.widget.EditText[1]')
    DESCRIPTION_INPUT = (By.XPATH, '//android.widget.ScrollView/android.widget.EditText[2]')
    SAVE_BUTTON = (By.XPATH, '//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[2]/android.widget.Button')

    def create_task(self, title, description):
        self.send_keys(self.TITLE_INPUT, title)
        self.send_keys(self.DESCRIPTION_INPUT, description)
        self.click(self.SAVE_BUTTON)
