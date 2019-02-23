# -*- coding: UTF-8 -*-
import time

from chrome import Chrome

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

url = 'http://admin.kingxin.top'

cr = Chrome(False)

def get_webmail_cookie(username, password):
    cr.driver.get(url)
    wait = WebDriverWait(cr.driver, 10)
    input_name = cr.driver.find_element_by_name('username')
    input_name.send_keys(username)
    input_pw = cr.driver.find_element_by_name('password')
    input_pw.send_keys(password)

    input_captcha = cr.driver.find_element_by_name('captcha')

    img = cr.driver.find_element_by_id('captcha')
    img_link = url + img.get_attribute('src')

    Image = Image.open(img_link)
    code = pytesseract.image_to_string(Image)
    print(code)
    input_captcha.send_keys(code)

    button_login = cr.driver.find_element_by_class_name('mysubmit')
    button_login.click()

    wait = WebDriverWait(cr.driver, 10)

    icon = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.bg-sub')))
    print(icon)

    cookies = cr.driver.get_cookies()

    print(cookies)

get_webmail_cookie("admin", "poiu0987")
cr.close()



