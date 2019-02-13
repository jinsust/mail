# -*- coding: UTF-8 -*-
import time

from selenium import webdriver # 从selenium导入webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
driver = webdriver.Chrome(chrome_options=chrome_options)

driver.get('https://www.baidu.com') # 获取百度页面

driver.find_element_by_id("kw").send_keys("selenium")   # 定位输入框并输入关键字
driver.find_element_by_id("su").click()   #点击[百度一下]搜索
time.sleep(30)   #等待3秒
driver.quit()   #关闭浏览器
