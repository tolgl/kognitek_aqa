from selenium.webdriver.common.by import By


class MainPageLocators:
    checkbox_orange = (By.XPATH, ".//div[@class='widget-content']/input[@value='orange']")
    checkbox_blue = (By.XPATH, ".//div[@class='widget-content']/input[@value='blue']")
    button_open_new_window = (By.XPATH, ".//a[text()='Open a popup window']")
    text_double_click = (By.ID, "testdoubleclick")
    context_menu = (By.ID, "myDropdown")
