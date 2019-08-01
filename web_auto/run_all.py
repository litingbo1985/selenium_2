import unittest
from common import HTMLTestRunner_cn
#用例路径
#匹配规则
casePath = "D:\soft\\web_auto\\case"
rule = "test*.py"
discover = unittest.defaultTestLoader.discover(start_dir=casePath,pattern=rule)
# discover = unittest.defaultTestLoader.discover()
print(discover)
reportPath = "D:\soft\\web_auto\\report\\"+"result.html"
fp = open(reportPath,"wb")
runner = HTMLTestRunner_cn.HTMLTestRunner(stream=fp,
                                       title="报告的title",
                                       description="描述你的报告干什么用",
                                       retry=1)
runner.run(discover)
fp.close()