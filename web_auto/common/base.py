from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

class Base():
    def __init__(self,driver:webdriver.Firefox):#加一个：号才能调，只是一个形参
        self.driver = driver
        self.timeout = 10
        self.t = 0.5
    def get_title(self):
        '''获取title'''
        return self.driver.title
    def get_text(self,locator):
        '''获取文本'''
        try:
            # t = self.findElement(locator).text
            ele = self.finElementNew(locator).text
            return ele
            # return t
        except:
            print("获取text文本失败，返回”")
            return ""
    def get_attribute(self,locator,name):
        '''获取属性'''
        try:
            element = self.findElement(locator)
            return element.get_attribute(name)
        except:
            print("获取t失败，返回”")
            return ""


    def finElementNew(self,locator):
        '''定位到元素，返回元素对象，没有定位到返回Timeeout异常'''
        ele = WebDriverWait(self.driver, self.timeout,self.t).until(EC.presence_of_element_located(locator))
        return ele

    def findElement(self,locator):
        ele = WebDriverWait(self.driver, self.timeout,self.t).until(lambda x: x.find_element(*locator))
        return ele
    def findElements(self,locator):
        try:
            eles = WebDriverWait(self.driver, self.timeout,self.t).until(lambda x: x.find_elements(*locator))
            return eles
        except:
            return []
    def sendKeys(self,locator,text):
        ele = self.findElement(locator)
        ele.send_keys(text)
    def click(self,locator):
        ele = self.findElement(locator)
        ele.click()
    def clear(self,locator):
        ele = self.findElement(locator)
        ele.clear()
    def isSelected(self,locator):
        '''判断元素是否被选中，返回bool值'''
        ele = self.findElement(locator)
        r = ele.is_selected()
        return r
    def isElementExist(self,locator):
        '''判断元素是否存在'''
        try:
            self.findElement(locator)
            return True
        except:
            return False
    def isElementsExist(self,locator):
        eles = self.findElements(locator)
        n = len(eles)
        if n == 0:
            return False
        elif n == 1:
            return True
        else:
            print("定位到元素的个数：%s"%n)
            return True
    def is_title(self,_title):
        '''返回bool值'''
        try:
            result = WebDriverWait(self.driver, self.timeout,self.t).until(EC.title_is(_title))
            return result
        except:
            return False
    def is_title_contains(self,_title):
        '''返回bool值'''
        try:
            result = WebDriverWait(self.driver, self.timeout,self.t).until(EC.title_contains(_title))
            return result
        except:
            return False
    def is_text_in_element(self,locator,_text):
        '''返回bool值'''
        if not isinstance(locator,tuple):
            print('locator参数类型错误，必须传元祖类型：loc = ("id","value1")')
        try:
            result = WebDriverWait(self.driver, self.timeout,self.t).until(EC.text_to_be_present_in_element(locator,_text))
            return result
        except:
            return False
    def is_value_in_element(self,locator,_value):
        '''返回bool值,value为空字符串返回False'''
        try:
            result = WebDriverWait(self.driver, self.timeout,self.t).until(EC.text_to_be_present_in_element_value(locator,_value))
            return result
        except:
            return False
    def is_alert(self):
        try:
            result = WebDriverWait(self.driver, self.timeout,self.t).until(EC.alert_is_present())
            return result
        except:
            return False
    def js_scroll_top(self):
        '''滚动到顶部'''
        js = "window.scrollTo(0,0)"
        self.driver.execute_script(js)
    def js_scroll_end(self):
        '''滚动到底部'''
        js = "window.scrollTo(0,document.body.scrollHeight))"
        self.driver.execute_script(js)
    def js_scroll_heng(self,x=0):
        '''横向滚动'''
        js = "window.scrollTo(%s,document.body.scrollHeight))"%x
        self.driver.execute_script(js)
    def js_focusing_element(self,locator):
        '''定位到特定元素'''
        target = self.finElement(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();",target)
    def select_by_index(self,locator,index=0):
        '''通过索引，index是索引第几个，从0开始'''
        element = self.findElement(locator)
        Select(element).select_by_index(index)

    def switch_handle(self,window_name):
        self.driver.switch_to.window(window_name)
    def switch_alert(self):
        r = self.is_alert()
        if not r:
            print("alert不存在")
        else:
            return r
    def move_to_element(self,locator):
        '''鼠标悬停操作'''
        ele = self.findElement(locator)
        ActionChains(driver).move_to_element(ele).perform()


if __name__ == "__main__":
    driver = webdriver.Firefox()
    driver.get("http://127.0.0.1/zentao/user-login.html")
    zentao = Base(driver)

    # loc2 = (By.NAME,"password")
    # loc3 = (By.ID,"submit")
    # loc1 = (By.ID,"account")
    # loc2 = (By.CSS_SELECTOR,"[name='password']")
    # loc3 = (By.XPATH,"//*[@id='submit']")
    loc1 = ("id","account")
    loc2 = ("css selector","[name='password']")
    loc3 = ("xpath","//*[@id='submit']")
    # loc4 = ("class name","xxx")
    # zentao.findElement(loc1).send_keys("admin")
    # zentao.findElement(loc2).send_keys("123456")
    # zentao.findElement(loc3).click()
    # driver.switch_to.frame()
    zentao.sendKeys(loc1,"admin")
    zentao.sendKeys(loc2,"123456")
    zentao.click(loc3)