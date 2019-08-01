import time
import unittest

from selenium import webdriver

from pages.add_bug_page import ZenTaoBug
from pages.login_page import Login


class Test_Add_Bug(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()#打开浏览器
        cls.zentao = ZenTaoBug(cls.driver)
        cls.l = Login(cls.driver)
        cls.l.login()#登录
    def test_add_bug(self):
        timestr = time.strftime("%Y_%m_%d_%H_%M_%S")
        title = "第一次提交BUG"+timestr#按时年月日时分秒拼BUG的标题
        self.zentao.add_bug(title)
        result = self.zentao.is_new_bug_suc(title)#新增成功后，获取BUG的标题并打印出来
        print(result)
        self.assertTrue(result)
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()#退出浏览器
if __name__ == "__main__":
    unittest.main()




