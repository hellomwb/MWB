# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class Untitled(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://change-this-to-the-site-you-are-testing/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_untitled(self):
        driver = self.driver
        driver.get("http://sw.virsical.cn:8080/")
        self.assertEqual(u"智能工位管理系统", driver.title)
        driver.find_element_by_css_selector("button.ant-btn.ant-btn-primary").click()
        driver.find_element_by_css_selector("div.ant-menu-submenu-title").click()
        driver.find_element_by_link_text(u"用户信息").click()
        driver.find_element_by_css_selector("div.page-pointer").click()
        driver.find_element_by_css_selector("div[name=\"user.ip.id\"] > input.ant-input").clear()
        driver.find_element_by_css_selector("div[name=\"user.ip.id\"] > input.ant-input").send_keys(
            "admin@wafersystems.com")
        driver.find_element_by_css_selector("div[name=\"user,ip.password\"] > input.ant-input").clear()
        driver.find_element_by_css_selector("div[name=\"user,ip.password\"] > input.ant-input").send_keys("WAferWp2017")
        driver.find_element_by_css_selector("button.ant-modal-close").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
