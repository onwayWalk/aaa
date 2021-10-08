from HTMLTestRunner import HTMLTestRunner
import unittest
tests=unittest.defaultTestLoader.discover(r"C:\Users\lenovo\PycharmProjects\pythonProject1\day11",pattern='Test*.py')

html=HTMLTestRunner.HTMLTestRunner(
    title="计算机测试报告",
    description="这是计算机的算法测试",
    verbosity=1,
    stream=open(file="计算机测试报告.html",mode="w+",encoding='utf-8')
)
html.run(tests)
