import softest
from Tests.BaseTest import BaseTest

class Test_Log_In(BaseTest, softest.TestCase):

    def test_Log_In(self):
        self.step1()
        self.step2()

    def step1(self):
        self.main_page.click_log_in_button()

    def step2(self):
        self.sign_in_page.log_into_app('tenono9329@o3live.com')