#导入包
from selenium import  webdriver
import unittest
from pages.login_page import LoginPage,lgoing_url
from common.base import Base
import ddt
import os
import xlrd
from data.read_excel import ExcelUtil1

'''
先思考下手工操作顺序（主要流程）
第1个用例：输入admin,输入123456，点击登录
第2个用例步：输入admin,不输入，点击登录
第3个用例：输入111admin,输入123456，点击登录
'''
#用字典去存储
# testdates = [
#     {"user":"admin","psw":"123456","expect":"退出"},
#     {"user":"admin","psw":"","expect":""},
#     {"user":"admin1111","psw":"123456","expect":""}
# ]
propath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))#当前路径再到上一层路径
filepath = os.path.join(propath,"common","datas.xlsx")
print(filepath)
# filepath = "D:\\web_auto\\common\\datas.xlsx"
    # sheetName = "Sheet1"
data = ExcelUtil1(filepath)
testdates = data.dict_data()
print(testdates)
@ddt.ddt
class LoginPageCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()
        cls.loginpg = LoginPage(cls.driver)
        cls.driver.get(lgoing_url)
    def setUp(self):
            # self.driver.get(lgoing_url)
        self.loginpg.is_alert_exist()
        self.driver.delete_all_cookies()#清空cookies
        self.driver.refresh()
        self.driver.get(lgoing_url)
    def login_case(self,user,psw,expect):
        self.loginpg.login(user,psw)
        # self.loginpg.input_user(user)
        # self.loginpg.input_psw(psw)
        # self.loginpg.click_login_button()
        result = self.loginpg.get_login_name()
        print("测试结果：%s" % result)
        # print(result)
        self.assertTrue(result==expect)
    @ddt.data(*testdates)#分开传入，分三次，作为三个字典传过来
    # @ddt.data({"user":"admin","psw":"123456","expect":"退出"},
    #           {"user":"admin","psw":"","expect":""},
    #           {"user":"admin1111","psw":"123456","expect":""})
    #执行的时候不按顺序，这个没有关系
    def test_01(self,data):
        '''
        1 输入用户admin密码123456点击登录
        :return:
        '''
        print("------------------开始:---------------")
        print("测试数据：%s" % data)
        self.login_case(data["user"],data["psw"],data["expect"])
        print("------------------结束：end!---------------")
    # def tearDown(self):
    #     self.loginpg.is_alert_exist()
    #     self.driver.delete_all_cookies()#清空cookies
    #     self.driver.refresh()
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
if __name__ == "__main__":
    unittest.main()
