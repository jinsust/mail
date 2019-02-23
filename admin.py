# -*- coding: UTF-8 -*-
import time

from chrome import Chrome

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PIL import Image
import pytesseract

import os

pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

url = 'http://admin.kingxin.top'

cr = Chrome(True)
def save_image(image_url):
    file_name = 'code.png'
    cmd = 'wget %s -O %s' %(image_url, file_name)
    os.system(cmd)
    return file_name

def image_orc(image_path):
    im = Image.open(image_path)
    '''
    im=im.convert('L')#图片转换为灰色图
    im=im.convert('RGBA')#图片转换成RGBA模式
    pixdata = im.load()

    for y in range(im.size[1]):
	for x in range(im.size[0]):
	#循环图像里的每一个像素。每个像素为一个长度为4的列表。因为图片转换成RGBA模式，所以列表长度为4，A就是透明度
	    if pixdata[x,y][0]>170 and pixdata[x,y][1]>170 and pixdata[x,y][2]>170 and pixdata[x,y][3]>170:
		pixdata[x,y]=(255, 255, 255, 0)
	    else:  
		pixdata[x,y]=(0, 0, 0, 0)
								
    im.save(image_path)
    '''
    code = pytesseract.image_to_string(im,  config="-psm 8 ")
    print("image code  ===== ", code)
    return code

def get_webmail_cookie(username, password):
    cr.driver.get(url)
    input_name = cr.driver.find_element_by_name('username')
    input_name.send_keys(username)
    input_pw = cr.driver.find_element_by_name('password')
    input_pw.send_keys(password)

    input_captcha = cr.driver.find_element_by_name('captcha')

    img = cr.driver.find_element_by_id('captcha')
    img_link = img.get_attribute('src')
    img_path = save_image(img_link)
    code = image_orc(img_path)
    input_captcha.send_keys(code)

    button_login = cr.driver.find_element_by_id('mysubmit')
    button_login.click()

    wait = WebDriverWait(cr.driver, 10)

    icon = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.bg-sub')))
    print(icon)

    cookies = cr.driver.get_cookies()

    print(cookies)

#image_orc('code.png')
try:
    get_webmail_cookie("admin", "poiu0987")
finally:
    cr.close()



