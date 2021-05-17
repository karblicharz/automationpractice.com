from Utils.Settings import get_user_password

class SignInPage:
    def __init__(self, driver):
        self.driver = driver

        self.email_address_id = 'email'
        self.password_id = 'passwd'

    def type_username(self, login):
        self.driver.find_element_by_id(self.email_address_id).clear()
        self.driver.find_element_by_id(self.email_address_id).send_keys(login)

    def type_password(self, password):
        self.driver.find_element_by_id(self.password_id).clear()
        self.driver.find_element_by_id(self.password_id).send_keys(password)

    def log_into_app(self, username):
        self.type_username(username)
        self.type_password(get_user_password(username))