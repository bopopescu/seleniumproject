from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome(executable_path="C:\selenium\drivers\chromedriver.exe")
driver.get("https://www.facebook.com/")
driver.find_element_by_name('firstname').send_keys('Hemraj')
driver.find_element_by_name('lastname').send_keys('K')
driver.find_element_by_name('reg_email__').send_keys('8095789449')
driver.find_element_by_name('reg_passwd__').send_keys('Raj@2019')
time.sleep(3)
