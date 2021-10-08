from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get(r'C:\Users\lenovo\Desktop\搭建7\练习的html\frame.html')
driver.find_element_by_xpath("//*[@id='input1']").send_keys('aaa')
time.sleep(4)
driver.quit()