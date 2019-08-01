#导入包
from selenium import  webdriver
import unittest
from pages.login_page import LoginPage,lgoing_url
from common.base import Base
'''
先思考下手工操作顺序（主要流程）
第1个用例：输入admin,输入123456，点击登录
第2个用例步：输入admin,不输入，点击登录
第3个用例：输入111admin,输入123456，点击登录
'''
#用字典去存储
testdates = [
    {"user":"admin","psw":"123456","expect":"退出"},
    {"user":"admin","psw":"","expect":""},
    {"user":"admin1111","psw":"123456","expect":""}
]
class LoginPageCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()
        cls.loginpg = LoginPage(cls.driver)
    def setUp(self):
            self.driver.get(lgoing_url)
            # self.loginpg.is_alert_exist()
            # self.driver.delete_all_cookies()#清空cookies
            # self.driver.refresh()
    def login_case(self,user,psw,expect):
        self.loginpg.login(user,psw)
        # self.loginpg.input_user(user)
        # self.loginpg.input_psw(psw)
        # self.loginpg.click_login_button()
        result = self.loginpg.get_login_name()
        print("测试结果：%s" % result)
        # print(result)
        self.assertTrue(result==expect)
    def test_01(self):
        '''
        1 输入用户admin密码123456点击登录
        :return:
        '''
        print("------------------开始测试：test_01---------------")
        data1 = testdates[0]
        print("测试数据：%s" % data1)
        self.login_case(data1["user"],data1["psw"],data1["expect"])
        print("------------------结束测试：end!---------------")
    def test_02(self):
        '''用户名输入admin,密码不输入，点击登录'''
        print("------------------开始测试：test_02---------------")
        data2 = testdates[1]
        print("测试数据：%s" % data2)
        self.login_case(data2["user"],data2["psw"],data2["expect"])
        print("------------------结束测试：end!---------------")
    def test_03(self):
        '''输入用户admin1111,输入密码123456，点击登录'''
        print("------------------开始测试：test_03---------------")
        data3 = testdates[2]
        print("测试数据：%s" % data3)
        self.login_case(data3["user"],data3["psw"],data3["expect"])
        print("------------------结束测试：end!---------------")
    def tearDown(self):
        self.loginpg.is_alert_exist()
        self.driver.delete_all_cookies()#清空cookies
        self.driver.refresh()
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
if __name__ == "__main__":
    unittest.main()
