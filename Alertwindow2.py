from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="C:\selenium\drivers\chromedriver.exe")
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.find_element_by_xpath("//*[@id='HTML9']/div[1]/button").click()
#driver.switch_to_alert().accept()
driver.switch_to_alert().dismiss()
