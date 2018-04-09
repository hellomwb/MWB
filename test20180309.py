# coding=utf-8
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://bj.ganji.com/")
driver.implicitly_wait(10)
# 获取当前 窗口句柄
h = driver.current_window_handle
print h
driver.find_element_by_link_text("工作").click()
all_h = driver.window_handles
print all_h
driver.close()
driver.switch_to.window(h)
print driver.title
