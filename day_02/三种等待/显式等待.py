# coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

gc = webdriver.Chrome()

gc.get(r"D:\PythonProjects\Selenium_Demo_Zero_02\Test_Selenium.html")
gc.maximize_window()

gc.find_element(By.XPATH, "//input[@value='测试等待']").click()

# 显式等待 lambda表达式写法（匿名函数）
# WebDriverWait(gc, 10, 0.5).until(lambda gc: gc.find_element(By.ID, "test_input_01"))

# 显式等待 利用selenium内置的expected_conditions
WebDriverWait(gc, 10, 0.1).until(EC.presence_of_element_located((By.ID, "test_input_01")))

gc.find_element(By.ID, "test_input_01").send_keys("66666")

# print((lambda x, y: x + y)(1, 3))
# print((lambda x: x ** 3)(9))