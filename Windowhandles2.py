from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome(executable_path="C:\selenium\drivers\chromedriver.exe")
driver.get("http://demo.automationtesting.in/Windows.html")
time.sleep(2)
driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()
time.sleep(2)
#print(driver.current_window_handle)
handles=driver.window_handles

for handle in handles:
    driver.switch_to.window(handle)
    print(handle)
    print(driver.title)
    if driver.title=="Sakinalium | Home":
        driver.close()
