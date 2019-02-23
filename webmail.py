# -*- coding: UTF-8 -*-
import time

from chrome import Chrome

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = 'http://webmail.kingxin.top'

cr = Chrome(False)

def get_webmail_cookie(username, password):
    cr.driver.get(url)
    wait = WebDriverWait(cr.driver, 10)
    input_mail = wait.until(EC.element_to_be_clickable((By.ID, 'RainLoopEmail')))
    input_mail.send_keys(username)
    input_pw = cr.driver.find_element_by_id('RainLoopPassword')
    input_pw.send_keys(password)

    button_login = cr.driver.find_element_by_class_name('buttonLogin')

    button_login.click()

    wait = WebDriverWait(cr.driver, 10)

    icon = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.icon-user')))

    print(icon)

    cookies = cr.driver.get_cookies()

    print(cookies)

get_webmail_cookie("jinsu@kingxin.top", "poiu0987")
cr.close()



