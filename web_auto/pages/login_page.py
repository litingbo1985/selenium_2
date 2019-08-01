# coding:utf-8
from selenium import webdriver
from common.base import Base
import time
#全局参数
lgoing_url = "http://127.0.0.1/zentao/user-login-L3plbnRhby8=.html"
#继承，写法就像自己的写的方法，可以直接使用
class LoginPage(Base):#继承
    #定位登录时候的元素
    loc_user = ("id","account")
    loc_psw = ("css selector","[name='password']")
    loc_button = ("xpath","//*[@id='submit']")
    loc_keep_login = ("id","keepLoginon")
    loc_forget_psw_page = ("xpath","/html/body/div/div/div[2]/p/a")
    #userMenu>a
    loc_forget_psw = ("link text","忘记密码")
    # loc_get_user = ("css selector","#userMenu>a")
    # loc_get_user = ("xpath",'/html/body/header/div/div/a[1]')
    loc_get_user = ("xpath","/html/body/header/div/div/div[1]/a")
    def input_user(self,text):
        self.sendKeys(self.loc_user,text)
    def input_psw(self,text):
        self.sendKeys(self.loc_psw,text)
    def click_login_button(self):
        self.click(self.loc_button)
    def click_keep_login(self):
        self.click(self.loc_keep_login)
    def click_forget_psw(self):
        self.click(self.loc_forget_psw)
    def login(self,user="admin",psw="123456",keep_login=False):
        '''封装登录流程'''
        self.driver.get(lgoing_url)
        self.driver.maximize_window()
        self.input_user(user)
        self.input_psw(psw)
        if keep_login:self.click_keep_login()
        time.sleep(2)
        self.click_login_button()

    # def login(self,user="admin",psw="123456"):
    #     self.driver.get("http://127.0.0.1/zentao/user-login.html")
    #     self.driver.maximize_window()#最大化浏览器
    #     self.sendKeys(self.loc1,user)
    #     self.sendKeys(self.loc2,psw)
        # self.click(self.loc3)
    def get_login_name(self):
        # try:
        #     time.sleep(5)
        #     user = self.get_text(self.loc_get_user)
        #     return user
        # except:
        #     print("没有获取到")
        try:
             t = self.findElement(self.loc_get_user).text
             # t = self.findElement("#userMenu>a").text
             print(t)
             return t
        except:
             return ""
    def get_login_result(self,user):
        result = self.is_text_in_element(self.loc_get_user,user)
        return result
    # def is_alert_exist(self):
    #         '''判断alert是不是在'''
    #         try:
    #             time.sleep(2)
    #             alert = self.driver.switch_to.alert
    #             text = alert.text
    #             alert.accept()#用alert点alert
    #             return text
    #         except:
    #             return ""
    #             pass
    def is_alert_exist(self):
        '''判断alert是不是在'''
        a = self.is_alert()
        # if not a:
        if  a:
            print(a.text)
            a.accept()
    def is_refrest_exist(self):
        '''判断忘记密码页面，刷新按钮是否存在'''
        try:
            r = self.isElementExist(self.loc_forget_psw_page)
            return r
        except:
            return ""

if __name__ == "__main__":
    driver = webdriver.Firefox()
    login_page = LoginPage(driver)
    # login_page.login(keep_login=True)
    login_page.login()
    # driver.get(lgoing_url)
    # login_page.input_user("admin")
    # login_page.input_psw("123456")
    # login_page.click_keep_login()
    # login_page.click_login_button()