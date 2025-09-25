from selenium.common import TimeoutException
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPageHelper(BasePage):

    def check_status_checkbox_orange(self):
        return self.find_element(MainPageLocators.checkbox_orange).is_selected()

    def click_checkbox_blue(self):
        self.find_element(MainPageLocators.checkbox_blue).click()

    def check_status_checkbox_blue(self):
        return self.find_element(MainPageLocators.checkbox_blue).is_selected()

    def click_button_open_new_window(self):
        self.find_element(MainPageLocators.button_open_new_window).click()

    def double_click_on_text(self):
        element = self.find_element(MainPageLocators.text_double_click)
        self.double_click(element)

    def get_class_context_menu(self):
        return self.find_element(MainPageLocators.context_menu).get_attribute("class")

    def click_link_gmail_context_menu(self):
        self.find_element(MainPageLocators.context_menu_link_gmail).click()

    def click_button_click_to_get_alert(self):
        self.find_element(MainPageLocators.button_click_to_get_alert).click()

    def check_alert(self):
        try:
            self.accept_alert()
            return "alert accepted"
        except TimeoutException:
            return "no alert"

    def get_list_other_sites_to_practice_automation(self):
        list_sites = []
        for site in self.find_elements(MainPageLocators.widget_other_sites_to_practice_automation):
            list_sites.append(site.text)
        return list_sites

    def filling_field_search(self, query):
        self.find_element(MainPageLocators.field_search).send_keys(query)

    def click_button_search(self):
        self.find_element(MainPageLocators.button_search).click()

    def get_text_result_search(self):
        return self.find_element(MainPageLocators.text_result_search).text

    def select_element_by_multi_selection_box(self, start_index, final_index):
        self.select_element(locator=MainPageLocators.select_element, start_index=start_index, final_index=final_index)