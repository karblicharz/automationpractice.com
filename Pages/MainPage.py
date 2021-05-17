class MainPage:
    def __init__(self, driver):
        self.driver = driver

        self.log_in_class = 'login'

    def click_log_in_button(self):
        self.driver.find_element_by_class_name(self.log_in_class).click

