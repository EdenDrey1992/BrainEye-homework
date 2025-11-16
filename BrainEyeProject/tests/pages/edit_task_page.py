from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage


class EditTaskPage(BasePage):
    NAVBAR = (By.XPATH, '//android.widget.TextView[@text="Edit Task"]')
    TITLE_INPUT = (By.CLASS_NAME, "android.widget.EditText")
    APPROVE_BUTTON = (By.XPATH, '//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[2]/android.widget.Button')

    def edit_task_title(self, new_title):
        self.send_keys(self.TITLE_INPUT, new_title)
        self.click(self.APPROVE_BUTTON)

    def append_to_task_title(self, additional_text):
        title_input = (By.XPATH, '//android.widget.EditText[@text="Task edit"]')
        el = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(title_input))
        current_text = el.text
        el.clear()
        el.send_keys(current_text + " " + additional_text)
        self.click(self.APPROVE_BUTTON)
