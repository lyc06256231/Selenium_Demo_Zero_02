# coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By

gc = webdriver.Chrome()

# implicitly_wait : 设置全局隐式等待（秒）
gc.implicitly_wait(10)

gc.get(r"D:\PythonProjects\Selenium_Demo_Zero_02\Test_Selenium.html")
gc.maximize_window()

gc.find_element(By.XPATH, "//input[@value='测试等待']").click()
gc.find_element(By.ID, "test_input_01").send_keys("66666")