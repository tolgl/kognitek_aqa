from pages.base_page import BasePage
from pages.main_page import MainPageHelper


class TestCheckUnOrderedList:

    def test_check_un_ordered_list(self, driver):
        base_page = BasePage(driver)
        base_page.go_to_page()
        main_page = MainPageHelper(driver)
        un_ordered_list = main_page.get_un_ordered_list()

        assert "Banana" in un_ordered_list
