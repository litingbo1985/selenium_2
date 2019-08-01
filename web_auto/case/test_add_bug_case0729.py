from selenium import webdriver
import unittest
from pages.login_page import LoginPage
from pages.add_bug_page import AddBugPage
import time
my = "http://127.0.0.1/zentao/my/"
class AddBugCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.zentao = AddBugPage(cls.driver)
        a = LoginPage(cls.driver)#实例化对象
        a.login()#调用方法
        #另外一个新增页面写
        # cls.xxx = XxPage(cls.driver)
    def setUp(self):
        '''
        每个用例都回到我的地盘页面
        :return:
        '''
        self.driver.get(my)
    def test_add_bug(self):
        '''添加BUG'''
        timestr = time.strftime("%Y_%m_%d_%H_%M_%S")
        title = "第一次提交BUG"+timestr
        self.zentao.add_bug(title)
        result = self.zentao.is_new_bug_suc(title)
        print(result)
        self.assertTrue(result)
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
if __name__ == "__main__":
    unittest.main()