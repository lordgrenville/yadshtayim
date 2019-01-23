import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

usernameStr = 'xxxx@xxxxx.com'
passwordStr = 'xxxxxxxxxx'

options = webdriver.ChromeOptions()
options.add_argument('--headless')
browser = webdriver.Chrome('C:\Program Files\chromedriver', options=options)
browser.get('https://my.yad2.co.il/login.php')
time.sleep(11)
browser.find_element_by_id('userName').send_keys(usernameStr)
browser.find_element_by_id('password').click()
browser.find_element_by_id('password').send_keys(passwordStr)
browser.find_element_by_id('submitLogonForm').click()
time.sleep(11)
browser.find_element_by_link_text('נדלן דירות להשכרה (1)').click()
browser.get('https://my.yad2.co.il/newOrder/index.php?action=personalAreaViewDetails&CatID=2&SubCatID=2&OrderID=37750519')
time.sleep(11)
browser.find_element_by_id('bounceRatingOrderBtn').click()
browser.quit()
