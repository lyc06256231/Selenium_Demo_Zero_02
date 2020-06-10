# coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

gc = webdriver.Chrome()

gc.get(r"D:\PythonProjects\Selenium_Demo_Zero_02\Test_Selenium.html")
gc.maximize_window()
sleep(1)

gc.find_element(By.XPATH, "//input[@value='测试单击']").click()
sleep(0.5)
gc.find_element(By.XPATH, "//input[@value='测试单击']").click()
sleep(0.5)
gc.find_element(By.NAME, "t2").send_keys(Keys.CONTROL, "a")
sleep(1)
gc.find_element(By.NAME, "t2").send_keys(Keys.CONTROL, "x")
sleep(1)
gc.find_element(By.NAME, "t2").send_keys(Keys.CONTROL, "v")
gc.find_element(By.NAME, "t2").send_keys(Keys.CONTROL, "v")
gc.find_element(By.NAME, "t2").send_keys(Keys.CONTROL, "v")


