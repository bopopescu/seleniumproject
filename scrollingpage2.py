from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="C:\selenium\drivers\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
flag=driver.find_element_by_xpath("//*[@id='content']/div[2]/div[2]/table[1]/tbody/tr[86]/td[1]/img")
driver.execute_script("arguments[0].scrollIntoView();",flag)