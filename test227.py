from selenium import webdriver
import time
driver =webdriver.Chrome()
driver.get('http://www.baidu.com')
time.sleep(5)
driver.get('http://testerhome.com')
time.sleep(3)
driver.back()
time.sleep(3)
driver.forward()
driver.refresh()
print(driver.title)