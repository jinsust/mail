# -*- coding: UTF-8 -*-

from selenium import webdriver # 从selenium导入webdriver
from selenium.webdriver.chrome.options import Options

class Chrome:
    def __init__(self, headless):
        chrome_options = Options()
        if headless:
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--disable-gpu')
            chrome_options.add_argument('--no-sandbox')
        self.driver = webdriver.Chrome(chrome_options=chrome_options)

    def close(self):
        self.driver.quit()


    def scrapy(self, url):
        self.driver.get(url)