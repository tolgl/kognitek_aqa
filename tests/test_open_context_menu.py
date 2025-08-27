from pages.base_page import BasePage
from pages.main_page import MainPageHelper


class TestOpenContextMenu:

    def test_open_context_menu(self, driver):
        base_page = BasePage(driver)
        base_page.go_to_page()
        main_page = MainPageHelper(driver)
        main_page.double_click_on_text()
        class_open_menu = main_page.get_class_context_menu()

        assert 'show' in class_open_menu
