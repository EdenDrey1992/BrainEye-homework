from selenium.webdriver.common.by import By
from .base_page import BasePage


class TaskDetailPage(BasePage):
    TITLE = (By.XPATH, '//android.widget.TextView[@text="Task Details"]')
    CHECKBOX = (By.XPATH, '//android.widget.CheckBox')
    DELETE_BUTTON = (By.XPATH, '//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[1]/android.view.View[2]/android.widget.Button')
    EDIT_BUTTON = (By.XPATH, '//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[2]/android.widget.Button')

    def toggle_complete(self):
        self.click(self.CHECKBOX)

    def delete_task(self):
        self.click(self.DELETE_BUTTON)

    def edit_task(self):
        self.click(self.EDIT_BUTTON)



