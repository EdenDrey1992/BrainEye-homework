import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from .base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait

class MainPage(BasePage):
    NAVBAR = (By.XPATH, '//android.widget.TextView[@text="Todo"]')
    ADD_BUTTON = (By.XPATH, '//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[2]/android.widget.Button')
    HAMBURGER = (By.XPATH, '//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[1]/android.view.View[1]/android.widget.Button')
    NO_TASKS_LABEL = (By.XPATH, '//android.widget.TextView[@text="You have no tasks!"]')
    FILTER_BUTTON = (By.XPATH, '//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[2]/android.view.View[2]/android.widget.Button')
    ALL_FILTER = (By.XPATH, '//android.widget.ScrollView/android.view.View[1]')
    ACTIVE_FILTER = (By.XPATH, '//android.widget.TextView[@text="Active"]')
    COMPLETED_FILTER = (By.XPATH, '//android.widget.TextView[@text="Completed"]')
    THREE_DOTS_BUTTON = (By.XPATH, '//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[2]/android.view.View[3]/android.widget.Button')
    CLEAR_COMPLETED = (By.XPATH, '//android.widget.TextView[@text="Clear completed"]')
    REFRESH = (By.XPATH, '//android.widget.TextView[@text="Refresh"]')
    COMPLETE_MSG = (By.XPATH, '//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[3]/android.view.View')
    FILTER_BUTTON_BASE = '//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[{}]/android.view.View[2]/android.widget.Button'
    HAMBURGER_BASE = '//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[{}]/android.view.View[1]/android.widget.Button'

    def get_hamburger(self, index=1):
        xpath = self.HAMBURGER_BASE.format(index)
        return (By.XPATH, xpath)

    def open_menu(self, index=1):
        self.click(self.get_hamburger(index))

    def tap_add_task(self):
        self.click(self.ADD_BUTTON)

    def open_task(self, index=1):
        task_xpath = f'//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[1]/android.view.View[{index}]'
        self.click((By.XPATH, task_xpath))

    def complete_task(self, index=1):
        checkbox_xpath = f'//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[1]/android.view.View[{index}]/android.widget.CheckBox'
        self.click((By.XPATH, checkbox_xpath))

    def get_task_title(self, index=1, timeout=10):
        task_xpath = f'//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[1]/android.view.View[{index}]/android.widget.TextView'

        def element_present(driver):
            try:
                el = driver.find_element(By.XPATH, task_xpath)
                text = el.text.strip()
                return text if text else False
            except:
                return False

        return WebDriverWait(self.driver, timeout, 0.5).until(element_present)

    def get_all_tasks(self):
        tasks_xpath = '//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[1]/android.view.View'
        elements = self.driver.find_elements(By.XPATH, tasks_xpath)
        return [el.text.strip() for el in elements if el.text.strip()]

    # Filtering

    def get_filter_button(self, index=2):
        """
        index: אם לא נשלח, ברירת מחדל היא 2 (כמו קודם)
        """
        xpath = self.FILTER_BUTTON_BASE.format(index)
        return (By.XPATH, xpath)

    # Filtering

    def filter_all(self, filter_index=None, timeout=10):
        idx = filter_index if filter_index else 2
        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(self.get_filter_button(idx))
        ).click()
        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(self.ALL_FILTER)
        ).click()

    def filter_active(self, filter_index=None, timeout=10):
        idx = filter_index if filter_index else 2
        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(self.get_filter_button(idx))
        ).click()
        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(self.ACTIVE_FILTER)
        ).click()

    def filter_completed(self, filter_index=None, timeout=10):
        idx = filter_index if filter_index else 2
        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(self.get_filter_button(idx))
        ).click()
        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(self.COMPLETED_FILTER)
        ).click()

    # Three dots menu

    def clear_completed_tasks(self):
        self.click(self.THREE_DOTS_BUTTON)
        self.click(self.CLEAR_COMPLETED)

    def refresh_tasks(self):
        self.click(self.THREE_DOTS_BUTTON)
        self.click(self.REFRESH)

    def get_complete_message(self, timeout=10):
        try:
            el = WebDriverWait(self.driver, timeout).until(lambda d: d.find_element(*self.COMPLETE_MSG))
            return "Task marked complete" in el.text
        except:
            return False

    def wait_for_text(self, text, timeout=5):
        end = time.time() + timeout
        while time.time() < end:
            if text in self.driver.page_source:
                return True
            time.sleep(0.5)
        return False


