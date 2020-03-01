from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="C:\selenium\drivers\chromedriver.exe")
driver.get("http://newtours.demoaut.com")
user_ele=driver.find_element_by_name('userName')
print(user_ele.is_displayed())
print(user_ele.is_enabled())

pwd_ele=driver.find_element_by_name('password')
print(pwd_ele.is_enabled())
print(pwd_ele.is_displayed())

user_ele.send_keys('mercury')
pwd_ele.send_keys('mercury')
driver.find_element_by_name('login').click()

roundtrip_radio=driver.find_element_by_css_selector("input[value=roundtrip]")
print(roundtrip_radio.is_selected())

oneway_radio=driver.find_element_by_css_selector("input[value=oneway]")
print(oneway_radio.is_selected())