# coding=utf-8

from selenium import webdriver

gc = webdriver.Chrome()
gc.get("https://baidu.com")

gc.execute_script("alert('hello')")