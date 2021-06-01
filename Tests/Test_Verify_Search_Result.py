import softest
from Tests.BaseTest import BaseTest
from Utils.Settings import screen_shot

class Test_Verify_Search_Result(BaseTest, softest.TestCase):

    def test_Verify_Search_Result(self):
        self.step1()
        self.step2()

    def step1(self):
        self.header_page.type_search('dress')
        self.header_page.click_search()

    def step2(self):
