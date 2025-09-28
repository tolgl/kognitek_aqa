from pages.main_page import MainPageHelper


class TestCheckStatusRadio:

    def test_check_status_radio_male(self, driver):
        main_page = MainPageHelper(driver)
        main_page.go_to_page()
        main_page.click_radio_male()
        status_radio_male = main_page.check_status_radio_male()

        assert status_radio_male is True
