from Dictionary.Environments import Environment
from datetime import datetime

def current_date_time(date_format):
    return datetime.now().strftime(date_format)

def get_environment():
    return Environment['test']

def get_credentials_path():
    return open('D:\\automationpractice_pass\\Passwords', 'r')

def get_user_password(username):
    for line in get_credentials_path().readlines():
        if username in line:
            return line.split(',')[1]

def screen_shot(self):
    file_name = 'D:/automationpractice/Screenshots/' + current_date_time('%Y-%m-%d %H-%M-%S') + '.png'
    self.driver.get_screenshot_as_file(file_name)
