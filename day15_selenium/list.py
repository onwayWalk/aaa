from selenium import webdriver
import  time
webdriver=webdriver.Chrome()
webdriver.get(r"C:\Users\lenovo\Desktop\搭建7\练习的html\上传文件和下拉列表\autotest.html")
webdriver.maximize_window()
webdriver.find_element_by_xpath("//*[@id='accountID']").send_keys('111')
webdriver.find_element_by_xpath("//*[@id='passwordID']").send_keys('111')
webdriver.find_element_by_xpath("//*[@id='areaID']").send_keys('北京市')
webdriver.find_element_by_xpath("//*[@id='sexID1']").click()
webdriver.find_element_by_xpath("//*[@value='spring']").click()
webdriver.find_element_by_xpath("//*[@name='file'and @type='file']").send_keys(r'C:\Users\Public\Pictures\Sample Pictures\1.jpg')
time.sleep(4)
webdriver.quit()