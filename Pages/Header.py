from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import softest

class HeaderPage:
    def __init__(self, driver):
        self.driver = driver

        self.sign_in_class = 'login'
        self.my_account_name_css = '.account > span:nth-child(1)'
        self.sign_out_class = 'logout'
        self.search_field_id = 'search_query_top'
        self.search_button_class = 'btn btn-default button-search'

    def click_sign_in(self):
        try:
            WebDriverWait(self.driver, timeout=20).until(
                expected_conditions.presence_of_element_located((By.CLASS_NAME, self.sign_in_class)))
            self.driver.execute_script("arguments[0].click();",
                                       self.driver.find_element_by_class_name(self.sign_in_class))
        except TimeoutException:
            print("Can not click 'Sign In' button")

    # def get_logged_user_first_name(self):
    #     return [self.driver.find_element_by_css_selector(self.my_account_name_css).text.split(' ')[0]]
    #
    # def get_logged_user_last_name(self):
    #     name = self.driver.find_element_by_css_selector(self.my_account_name_css).text()
    #     lastname = name.split(' ')[1]
    #     return lastname

    def verify_is_first_name_right(self, firstname):
        is_name_right = False
        first = self.driver.find_element_by_css_selector(self.my_account_name_css).text.split(' ')[0]
        if first == firstname:
            is_name_right = True

        return is_name_right

    def verify_is_last_name_right(self, firstname):
        is_name_right = False
        first = self.driver.find_element_by_css_selector(self.my_account_name_css).text.split(' ')[1]
        if first == firstname:
            is_name_right = True

        return is_name_right

    def click_sign_out(self):
        self.driver.find_element_by_class_name(self.sign_out_class).click()

    def click_search(self):
        try:
            WebDriverWait(self.driver, timeout=20).until(
                expected_conditions.presence_of_element_located((By.CLASS_NAME, self.search_button_class)))
            self.driver.execute_script("arguments[0].click();",
                                       self.driver.find_element_by_class_name(self.search_button_class))
        except TimeoutException:
            print("Can not click 'Search' button")

    def type_search(self, search_text):
        self.driver.find_element_by_id(self.search_field_id).send_keys(search_text)
