from selenium import webdriver
from selenium.webdriver.common.keys import  Keys
import time

driver=webdriver.Chrome(executable_path="C:\selenium\drivers\chromedriver.exe")
driver.get("https://www.youtube.com/")
driver.maximize_window()
print(driver.title)
time.sleep(3)
driver.find_element_by_id("search").send_keys("Python tutorial")
driver.find_element_by_id("search-icon-legacy").click()
#driver.close()