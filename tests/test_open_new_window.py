from pages.main_page import MainPageHelper
from pages.base_page import BasePage
from pages.popup_window_page import PopupWindowPageHelper


class TestCheckStatusCheckbox:

    def test_open_new_window(self, driver):
        base_page = BasePage(driver)
        base_page.go_to_page()
        main_page = MainPageHelper(driver)
        main_page.click_button_open_new_window()
        base_page.switch_to_window(count=2, index_win=1)
        popup_window = PopupWindowPageHelper(driver)
        text_h3_new_window = popup_window.get_text_h3()

        assert text_h3_new_window == "New Window"

    def test_close_new_window(self, driver):
        base_page = BasePage(driver)
        base_page.go_to_page()
        main_page = MainPageHelper(driver)
        main_page.click_button_open_new_window()
        base_page.switch_to_window(count=2, index_win=1)
        base_page.close_window(count=2, index_win=1)

        assert base_page.count_window() == 1
