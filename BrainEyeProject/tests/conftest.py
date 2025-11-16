import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
import os
import time


@pytest.fixture(scope="session")
def app_path():
    """
    Fixture that provides the path to the APK of the Todo app.

    - Checks if an environment variable 'TODO_APP_APK' is set and uses it.
    - Otherwise, uses the default absolute path to the APK in the project.
    - Scope 'session' means this is evaluated once per test session.
    """
    return os.environ.get(
        "TODO_APP_APK",
        os.path.abspath(
            r"C:\Users\eden0\architecture-samples\app\build\outputs\apk\debug\app-debug.apk"
        )
    )


@pytest.fixture(scope="function")
def driver(app_path):
    """
    Fixture that initializes and provides an Appium WebDriver for each test function.

    Steps:
    1. Configures UiAutomator2Options for Android:
       - Sets the app APK path.
       - Sets device name (emulator-5554).
       - Sets automation engine (UiAutomator2).
       - Automatically grants app permissions.
       - Sets new command timeout to 600 seconds.
       - no_reset = False and full_reset = False for app state handling.
    2. Creates the Appium driver by connecting to the Appium server at localhost:4723.
    3. Pauses briefly to allow the app to load.
    4. Yields the driver to the test function.
    5. Quits the driver after the test completes (cleanup).

    Scope 'function' means a fresh driver is created for each test.
    """
    options = UiAutomator2Options()
    options.app = app_path
    options.device_name = "emulator-5554"
    options.automation_name = "UiAutomator2"
    options.auto_grant_permissions = True
    options.new_command_timeout = 600
    options.no_reset = False
    options.full_reset = False

    # Create the Appium driver
    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    driver.implicitly_wait(5)
    # Small wait to allow the app to initialize
    time.sleep(1)

    # Provide the driver to the test
    yield driver

    # Cleanup: quit the driver after test
    driver.quit()
