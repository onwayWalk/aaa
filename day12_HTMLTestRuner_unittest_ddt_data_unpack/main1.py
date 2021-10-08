from HTMLTestRunner import HTMLTestRunner
import unittest
import os

tests=unittest.defaultTestLoader.discover(os.getcwd(),pattern="Test*.py")

html=HTMLTestRunner.HTMLTestRunner(
    title="计算器测试报告（自动化）",
    description="这是计算器测试报告的自动化断言",
    verbosity=1,
    stream=open(file="计算机测试报告(自动化断言).html",mode="w+",encoding='utf-8')
)
html.run(tests)