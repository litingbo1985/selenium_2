#导入包
from selenium import  webdriver
import unittest
from pages.login_page import LoginPage,lgoing_url
from common.base import Base
'''
先思考下手工操作顺序（主要流程）
第1个用例：输入admin,输入123456，点击登录
第2个用例步：输入admin,不输入，点击登录
第3个用例：输入admin,输入123456，点记住登录按钮，点击登录
第4个用例：点击忘记密码
'''
class LoginPageCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()
        cls.loginpg = LoginPage(cls.driver)
    def setUp(self):
            self.driver.get(lgoing_url)
            self.loginpg.is_alert_exist()
            self.driver.delete_all_cookies()#清空cookies
            self.driver.refresh()
    def test_01(self):
        '''
        输入用户密码点击登录
        :return:
        '''
        self.loginpg.input_user("admin")
        self.loginpg.input_psw("123456")
        self.loginpg.click_login_button()
        result = self.loginpg.get_login_name()
        print(result)
        self.assertTrue(result=="退出")
        #断言
    def test_02(self):
        ''''''
        self.loginpg.input_user("admin")
        self.loginpg.click_login_button()
        result = self.loginpg.get_login_name()
        self.assertTrue(result=="")
        #断言
    def test_03(self):
        ''''''
        self.loginpg.input_user("admin")
        self.loginpg.input_psw("123456")
        self.loginpg.click_keep_login()
        self.loginpg.click_login_button()
        result = self.loginpg.get_login_name()
        self.assertTrue(result=="退出")
        #断言
    def test_04(self):
        '''忘记密码'''
        self.loginpg.click_forget_psw()
        result = self.loginpg.is_refrest_exist()
        self.assertTrue(result)
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
if __name__ == "__main__":
    unittest.main()
