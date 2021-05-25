from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from Utils.Settings import get_user_password

class SignInPage:
    def __init__(self, driver):
        self.driver = driver

        self.email_address_id = 'email'
        self.password_id = 'passwd'
        self.login_button_id = 'SubmitLogin'

    def type_username(self, login):
        try:
            WebDriverWait(self.driver, timeout=20).until(
                expected_conditions.presence_of_element_located(
                    (By.ID, self.password_id)))
            self.driver.execute_script("arguments[0].click();", self.driver.find_element_by_id(self.email_address_id))
        except TimeoutException:
            print("Can not find 'Email address' field")

        self.driver.find_element_by_id(self.email_address_id).send_keys(login)

    def type_password(self, password):
        self.driver.find_element_by_id(self.password_id).clear()
        self.driver.find_element_by_id(self.password_id).send_keys(password)

    def log_into_app(self, username):
        self.type_username(username)
        self.type_password(get_user_password(username))

    def click_login_button(self):
        self.driver.find_element_by_id(self.login_button_id).click()