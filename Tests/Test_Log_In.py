import softest
import time
from Tests.BaseTest import BaseTest

class Test_Log_In(BaseTest, softest.TestCase):

    def test_Log_In(self):
        self.step1()
        self.step2()
        self.step3()

    def step1(self):
        self.header_page.click_sign_in_button()

    def step2(self):
        self.sign_in_page.log_into_app('tenono9329@o3live.com')
        self.sign_in_page.click_login_button()

    def step3(self):
        self.assertTrue(self.header_page.verify_is_first_name_right('TestFirstName1'), 'First name is wrong')
        self.assertTrue(self.header_page.verify_is_last_name_right('TestLastName2'), 'First name is wrong')
