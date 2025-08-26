from pages.main_page import MainPageHelper
from pages.base_page import BasePage


class TestCheckStatusCheckbox:

    def test_check_status_checkbox_orange(self, driver):
        base_page = BasePage(driver)
        base_page.go_to_page()
        main_page = MainPageHelper(driver)
        status_checkbox_orange = main_page.check_status_checkbox_orange()

        assert status_checkbox_orange is True
