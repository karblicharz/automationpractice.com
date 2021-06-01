import softest
from Tests.BaseTest import BaseTest
from Utils.Settings import screen_shot

class Test_Log_In(BaseTest, softest.TestCase):

    def test_Log_In(self):
        self.step1()
        self.step2()
        self.step3()
        self.step4()

    def step1(self):
        self.header_page.click_sign_in()

    def step2(self):
        self.sign_in_page.type_credentials('tenono9329@o3live.com')
        self.sign_in_page.click_login()

    def step3(self):
        self.assertTrue(self.header_page.verify_is_first_name_right('TestFirstName'), 'First name is wrong')
        self.assertTrue(self.header_page.verify_is_last_name_right('TestLastName'), 'First name is wrong')

        screen_shot(self)

    def step4(self):
        self.header_page.click_sign_out()