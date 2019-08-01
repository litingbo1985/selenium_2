# coding:utf-8
from selenium import webdriver
import time
import unittest
class LoginTest(unittest.TestCase):
        @classmethod
        def setUpClass(cls):
            print("用例前执行一次")
            cls.driver = webdriver.Firefox()
        @classmethod
        def tearDownClass(cls):
            print("用例后，只调用一次")
            cls.driver.quit()
        def setUp(self):
            self.driver.get("http://127.0.0.1/zentao/user-login.html")
            self.driver.delete_all_cookies()#清空cookies
            self.driver.refresh()
        # def tearDown(self):
        #     self.driver.delete_all_cookies()#清空cookies
        #     self.driver.refresh()
            # self.driver.quit()
        def get_login_username(self):
             try:
                 t = self.driver.find_element_by_css_selector("#userMenu>a").text
                 print(t)
                 return t
             except:
                 return ""
        def is_alert_exist(self):
            '''判断alert是不是在'''
            try:
                time.sleep(2)
                alert = self.driver.switch_to.alert
                text = alert.text
                alert.accept()#用alert点alert
                return text
            except:
                return ""
                pass

        # def tearDown(self):
        #     self.driver.delete_all_cookies()#清空cookies
        #     self.driver.refresh()
        def login(self,user,psw):
            time.sleep(2)
            self.driver.find_element_by_id("account").send_keys(user)
            self.driver.find_element_by_name("password").send_keys(psw)
            self.driver.find_element_by_id("submit").click()
        def test_01(self):
            '''用例说明：用例登录成功'''
            self.login("admin","123456")
            #判断是否登录成功
            time.sleep(3)
            t = self.get_login_username()
            print("获取的结果：%s"%t)
            self.assertTrue(t=="admin")
        def test_02(self):
            '''用例说明：用例登录失败'''
            self.login("admin1","")
            # time.sleep(2)
            # self.driver.find_element_by_id("account").send_keys("admin11")
            # self.driver.find_element_by_name("password").send_keys("11123456")
            # self.driver.find_element_by_id("submit").click()
            #判断是否登录成功
            time.sleep(3)
            t = self.get_login_username()
            print("登录失败，获取结果：%s"%t)
            # self.assertTrue(t=="")
            self.assertTrue(1==2)#断言失败截图
            time.sleep(6)
            # if t == "admin":
            #     print("pass")
            # else:
            #     print("fail")
# if __name__ == "__mian__":
#     unittest.main()
# def tearDown(self):
#     self.is_alert_exit()
#     self.driver.delete_all_cookies()#退出登录
#     self.driver.refresh()
#     self.driver.quit()
    # @classmethod
    # def tearDownClass(cls):
    #     print("关闭浏览器")
    #     cls.driver.quit()#编辑器问题

if __name__ == '__main__':
    unittest.main()




