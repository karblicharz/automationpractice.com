from Dictionary.Environments import Environment

def get_environment():
    return Environment['test']

def get_credentials_path():
    return open('D:\\automationpractice_pass\\Passwords', 'r')

def get_user_password(username):
    for line in get_credentials_path().readlines():
        if username in line:
            return line.split(',')[1]
