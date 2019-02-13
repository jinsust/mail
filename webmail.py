# -*- coding: UTF-8 -*-
import time

from chrome import Chrome

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = 'webmail.kingxin.top'

cr = Chrome(False)

def get_webmail_cookie(username, password):
    cr.driver.get(url)
    input_mail = cr.driver.find_elements_by_class_name('inputMail')[0]
    input_mail.send_keys(username)
    input_pw = cr.driver.find_elements_by_class_name('inputPassword')[0]
    input_pw.send_keys(password)

    button_login = cr.driver.find_element_by_class_name('buttonLogin')[0]

    button_login.click()

    wait = WebDriverWait(cr.driver, 10)

    icon = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.icon-user')))

    print(icon)

    cookies = cr.driver.get_cookies()

    print(cookies)



