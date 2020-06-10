# coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
# from time import sleep
import time

driver = webdriver.Chrome() # 实例化一个浏览器对象
driver.get("https://baidu.com")
# driver.get(r"file:///E:/RF_Project/RF_Demo_02/Test_Selenium.html")

driver.maximize_window() # 最大化浏览器
time.sleep(1)

# id定位
# driver.find_element_by_id("kw").send_keys("嘻嘻") # send_keys 给输入框发送内容

# name 定位
# driver.find_element_by_name("wd").clear() # clear 清空输入框中的内容

# xpath 定位
# driver.find_element_by_xpath("//input[@id='kw']").send_keys("xpath")

# css_selector 定位
# driver.find_element_by_css_selector("input[id='kw']").send_keys("css_selector")

# tag_name （标签）定位
# print(driver.find_element_by_tag_name("body").size)

# class_name （类名）定位
# driver.find_element_by_class_name("s_ipt").send_keys("class_name")

# link_text （链接文本）定位
# driver.find_element_by_link_text("设为首页").click()

# partial_link_text （链接文本包含）定位
# driver.find_element_by_partial_link_text("为首").click()

# find_elements 复数形式，定位多个元素，八种
# list_a = driver.find_elements_by_tag_name("a")
# print(len(list_a))

# size 获取元素的大小（宽高）
# bd_input_size = driver.find_element_by_id("kw").size
# print(bd_input_size)

# text 获取元素的文本内容
# list_a = driver.find_elements_by_tag_name("a")
# for i in list_a:
#     print(list_a.index(i), i.text)

# location 获取元素的坐标
# print(driver.find_element_by_xpath("//*[@value='测试等待']").location)

# 获取元素（特性）属性
# print(driver.find_element_by_xpath("//*[@value='测试等待']").get_attribute("onclick"))
# print(driver.find_element_by_xpath("//*[@value='测试等待']").get_property("value"))

driver.find_element(By.ID, 'kw').send_keys('hhhhhh')