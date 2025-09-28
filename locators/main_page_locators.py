from selenium.webdriver.common.by import By


class MainPageLocators:
    checkbox_orange = (By.XPATH, ".//div[@class='widget-content']/input[@value='orange']")
    checkbox_blue = (By.XPATH, ".//div[@class='widget-content']/input[@value='blue']")
    button_open_new_window = (By.XPATH, ".//a[text()='Open a popup window']")
    text_double_click = (By.ID, "testdoubleclick")
    context_menu = (By.ID, "myDropdown")
    context_menu_link_gmail = (By.XPATH, ".//div[@id='myDropdown']/a[contains(@href, 'gmail.com')]")
    button_click_to_get_alert = (By.XPATH, ".//input[@value='ClickToGetAlert']")
    widget_other_sites_to_practice_automation = (By.XPATH, ".//h2[text()='Other Sites to Practice Automation']/../div[@class='widget-content']/ul/li/a")
    field_search = (By.XPATH, ".//td[@class='gsc-input']/input[@title='search']")
    button_search = (By.XPATH, ".//td[@class='gsc-search-button']/input[@title='search']")
    text_result_search = (By.XPATH, ".//div[@class='status-msg-wrap']/div[@class='status-msg-body']")
    select_element = (By.ID, "multiselect1")
    radio_male = (By.XPATH, ".//div[@class='widget-content']/input[@id='radio1']")
    un_ordered_list = (By.XPATH, ".//h2[text()='UnOrdered list']/../div/ul/li")
