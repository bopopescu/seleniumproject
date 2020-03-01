from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome(executable_path="C:\selenium\drivers\chromedriver.exe")
driver.get("http://newtours.demoaut.com")
print(driver.title)
time.sleep(3)

driver.get("http://pavantestingtools.blogspot.in")
print(driver.title)
time.sleep(3)

driver.back()
print(driver.title)
time.sleep(3)

driver.forward()
print(driver.title)

