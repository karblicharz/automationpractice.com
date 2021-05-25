from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from Pages.Header import HeaderPage
from Pages.SignInPage import SignInPage
from Utils.Settings import get_environment

class BaseTest:

    def setUp(self):
        self.options = Options()
        self.options.headless = False
        self.options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome('../resources/chromedriver.exe', options=self.options)
        self.driver.get(get_environment())

        self.header_page = HeaderPage(self.driver)
        self.sign_in_page = SignInPage(self.driver)
