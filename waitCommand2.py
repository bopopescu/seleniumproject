from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="C:\selenium\drivers\chromedriver.exe")
driver.get("http://newtours.demoaut.com")
driver.implicitly_wait(6)
print(driver.title)
driver.find_element_by_name("userName").send_keys("mercury")
driver.find_element_by_name("password").send_keys("mercury")
driver.find_element_by_name("login").click()
driver.quit()