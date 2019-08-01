from selenium import webdriver
import time
driver = webdriver.Firefox()
# driver.get("https://blog.csdn.net/dengachao")
driver.get("http://sz.ganji.com/")
driver.maximize_window()
time.sleep(4)
#滚动到浏览器底部
# js = "window.scrollTo(0,document.body.scrollHeight)"
# driver.execute_script(js)
# time.sleep(4)
# #滚动到浏览器顶部
# js = "window.scrollTo(0,0)"
# driver.execute_script(js)
#滚动到元素出现的位置
ele = driver.find_element_by_link_text("新车")
driver.execute_script("arguments[0].scrollIntoView();",ele)


