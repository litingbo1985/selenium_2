# coding:utf-8
from selenium import webdriver
from common.base import Base
import time
#继承，写法就像自己的写的方法，可以直接使用
class AddBugPage(Base):#继承
    # #定位登录时候的元素
    # loc1 = ("id","account")
    # loc2 = ("css selector","[name='password']")
    # loc3 = ("xpath","//*[@id='submit']")
    #增加BUG
    loc_test1 = ("link text","测试")#点击测试标签
    loc_test2 = ("link text","Bug")#点击Bug按钮
    loc_test3 = ("xpath",'.//*[@id="createActionMenu"]/a[1]')#点击提交BUG
    loc_test4 = ("xpath",'//*[@id="openedBuild_chosen"]/ul')#点击truck输入框
    loc_test5 = ("xpath",'//*[@id="openedBuild_chosen"]/div/ul/li')#点击truck
    loc_test6 = ("id",'title')#输入标题
    #loc_test7 = ("xpath",'//*[@id="openedBuild_chosen"]/div/ul/li')#输入正文
    #需要先切换iframe
    loc_input_body = ("class name","article-content")#定位到富文本
    loc_submit_save = ("css selector","#submit")
    #新增bug，获取第一个BUG
    loc_new_add = ("xpath",'.//*[@id="bugList"]/tbody/tr[1]/td[4]/a')
    # def __init__(self,driver):
    #     self.driver = driver
    #     self.zentao = Base(self.driver)
    # def login(self,user="admin",psw="123456"):
    #     self.driver.get("http://127.0.0.1/zentao/user-login.html")
    #     self.driver.maximize_window()#最大化浏览器
    #     self.sendKeys(self.loc1,user)
    #     self.sendKeys(self.loc2,psw)
    #     self.click(self.loc3)
    def add_bug(self,title="测试提交BUG"):
        self.click(self.loc_test1)
        self.click(self.loc_test2)
        self.click(self.loc_test3)
        self.click(self.loc_test4)
        self.click(self.loc_test5)

        self.sendKeys(self.loc_test6,title)
        #切换iframe,并输入BUG正文
        frame = self.findElement(("class name","ke-edit-iframe"))
        self.driver.switch_to.frame(frame)#self.driver.switch_to.frame(1)也可以
        # self.clear(self.loc_input_body)#富文本不能clear
        body = '''【测试步骤】xxx
        【实际结果】111
        【预期结果】2222
        '''
        self.sendKeys(self.loc_input_body,body)
        self.driver.switch_to.default_content()
        #点击保存，提交BUG
        self.click(self.loc_submit_save)
    def is_new_bug_suc(self,_text):
        return self.is_text_in_element(self.loc_new_add,_text)
# if __name__ == "__main__":注意缩进

if __name__ == "__main__":
    driver = webdriver.Firefox()#全局参数
    zentao = AddBugPage(driver)
    from pages.login_page import LoginPage#导入
    a = LoginPage(driver)#实例化对象
    a.login()#调用方法
    # zentao.login()
    timestr = time.strftime("%Y_%m_%d_%H_%M_%S")
    title = "第一次提交BUG"+timestr
    zentao.add_bug(title)
    result = zentao.is_new_bug_suc(title)
    print(result)
    # zentao.add_bug("第一次提交BUG"+timestr)

