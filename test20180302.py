# coding=utf-8
# 导入webdriver模块
from selenium import webdriver
import time

# 打开浏览器
driver = webdriver.Chrome()
# 打开工位系统
driver.get("http://sw.virsical.cn:8080/")
driver.find_element_by_xpath("//input[@class='ant-input inp mt28' and @type='text']").send_keys(
    "admin@wafersystems.com")
driver.find_element_by_xpath("//input[@class='ant-input inp mt28' and @type='password']").send_keys("WAferWp2017")
driver.find_element_by_xpath("//button[@class='ant-btn ant-btn-primary' and @type='button']").click()
driver.find_element_by_xpath("//div[@id='workstationIndex']/div/div/div/div/ul/li[4]/div/span/span").click()
driver.find_element_by_link_text(u"工位信息").click()
