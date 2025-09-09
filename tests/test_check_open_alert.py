from pages.main_page import MainPageHelper


class TestCheckOpenAlert:

    def test_check_open_alert(self, driver):
        main_page = MainPageHelper(driver)
        main_page.go_to_page()
        main_page.click_button_click_to_get_alert()

        assert main_page.check_alert() == 'alert accepted'
