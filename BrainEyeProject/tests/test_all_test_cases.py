from selenium.webdriver.support.wait import WebDriverWait
from tests.pages.main_page import MainPage
from tests.pages.create_task_page import CreateTaskPage
from tests.pages.task_detail_page import TaskDetailPage
from tests.pages.edit_task_page import EditTaskPage
from tests.pages.menu_page import MenuPage
from tests.pages.statistics_page import StatisticsPage

# --- Helper Functions ---


def create_task(main, title, description):
    """
    Create a new task using the CreateTaskPage.

    Args:
        main (MainPage): Instance of MainPage.
        title (str): Task title.
        description (str): Task description.
    """
    main.tap_add_task()
    create = CreateTaskPage(main.driver)
    create.create_task(title, description)


def open_and_edit_task(main, append_title=None):
    """
    Open the first task in the main list, edit it, and optionally append text to its title.

    Args:
        main (MainPage): Instance of MainPage.
        append_title (str, optional): Text to append to task title. Defaults to None.
    """
    main.open_task(1)
    detail = TaskDetailPage(main.driver)
    detail.edit_task()
    if append_title:
        edit = EditTaskPage(main.driver)
        edit.append_to_task_title(append_title)


def open_menu_and_go_to_statistics(main, menu_index=None):
    """
    Open the main menu and navigate to the Statistics page.

    Args:
        main (MainPage): Instance of MainPage.
        menu_index (int, optional): Index of the menu to open. Defaults to None.

    Returns:
        StatisticsPage: Instance of StatisticsPage.
    """
    if menu_index is None:
        main.open_menu()
    else:
        main.open_menu(menu_index)
    menu = MenuPage(main.driver)
    menu.go_to_statistics()
    return StatisticsPage(main.driver)

# --- Tests ---


def test_create_new_task(driver):
    """
    Test that a new task can be created successfully.

    Steps:
        1. Tap 'Add Task'.
        2. Fill task title and description.
        3. Verify that the task appears in the main list with the correct title.
    """
    main = MainPage(driver)
    create_task(main, "Task create", "Creating test case")
    title = main.get_task_title(1)
    assert title == "Task create"


def test_complete_task(driver):
    """
    Test completing a task and clearing completed tasks.

    Steps:
        1. Create a new task.
        2. Mark the task as complete.
        3. Clear completed tasks.
        4. Verify that the main list shows 'You have no tasks!'.
    """
    main = MainPage(driver)
    create_task(main, "Task complete", "completing test case")
    main.complete_task(1)
    main.clear_completed_tasks()
    assert main.wait_for_text("You have no tasks!") is True


def test_delete_task(driver):
    """
    Test deleting a task.

    Steps:
        1. Create a new task.
        2. Open the task detail page.
        3. Delete the task.
        4. Verify that the main list shows 'You have no tasks!'.
    """
    main = MainPage(driver)
    create_task(main, "Task delete", "deleting test case")
    main.open_task(1)
    TaskDetailPage(driver).delete_task()
    WebDriverWait(driver, 10).until(lambda d: main.wait_for_text("You have no tasks!") is True)
    assert main.wait_for_text("You have no tasks!") is True


def test_edit_task(driver):
    """
    Test editing a task's title.

    Steps:
        1. Create a new task.
        2. Open task detail and edit the task.
        3. Append 'completed' to the task title.
        4. Verify that the main list shows the updated task title.
    """
    main = MainPage(driver)
    create_task(main, "Task edit", "editing test case")
    open_and_edit_task(main, "completed")
    title = main.get_task_title(1)
    assert title == "Task edit completed"


def test_navigate_to_statistics(driver):
    """
    Test navigation to the Statistics page.

    Steps:
        1. Open the main menu.
        2. Navigate to the Statistics page.
        3. Verify that the navbar title is 'Statistics'.
    """
    main = MainPage(driver)
    stats = open_menu_and_go_to_statistics(main)
    assert stats.get_navbar_title() == "Statistics"


def test_filter(driver):
    """
    Test filtering tasks by completed and active.

    Steps:
        1. Create a new task.
        2. Filter completed tasks and verify no tasks appear.
        3. Filter active tasks and verify the task appears in the list.
    """
    main = MainPage(driver)
    create_task(main, "Task filter", "filtering test case")
    main.filter_completed()
    assert main.wait_for_text("You have no completed tasks!") is True
    main.filter_active(1)
    title = main.get_task_title(1)
    assert title == "Task filter"


def test_statistics_count_validation(driver):
    """
    Test that the statistics page correctly shows percentages.

    Steps:
        1. Create a new task.
        2. Open menu and navigate to Statistics page.
        3. Verify that the active tasks percentage is 100% and completed tasks percentage is 0%.
    """
    main = MainPage(driver)
    create_task(main, "Task statistics", "Statistics count test case")
    stats = open_menu_and_go_to_statistics(main, menu_index=2)
    assert stats.get_active_percentage() == "Active tasks: 100.0%"
    assert stats.get_completed_percentage() == "Completed tasks: 0.0%"
