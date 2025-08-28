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

    def test_click_gmail_context_menu(self, driver):
        base_page = BasePage(driver)
        base_page.go_to_page()
        main_page = MainPageHelper(driver)
        main_page.double_click_on_text()
        main_page.click_link_gmail_context_menu()
        current_url = base_page.get_current_url()

        assert 'accounts.google.com' in current_url

    def test_return_previous_page(self, driver):
        base_page = BasePage(driver)
        base_page.go_to_page()
        main_page = MainPageHelper(driver)
        main_page.double_click_on_text()
        main_page.click_link_gmail_context_menu()
        base_page.return_previous_page()
        current_url = base_page.get_current_url()

        assert 'omayo.blogspot.com' in current_url
