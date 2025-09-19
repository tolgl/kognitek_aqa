from pages.base_page import BasePage
from pages.main_page import MainPageHelper


class TestCheckSiteListSitesToAutomation:

    def test_check_site_list_sites_to_automation(self, driver):
        base_page = BasePage(driver)
        base_page.go_to_page()
        main_page = MainPageHelper(driver)
        list_sites = main_page.get_list_other_sites_to_practice_automation()

        assert "testwisely" in list_sites
