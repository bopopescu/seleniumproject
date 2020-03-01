from selenium import webdriver
driver=webdriver.Chrome(executable_path="C:\selenium\drivers\chromedriver.exe")
driver.get("https://www.facebook.com/")
status=driver.find_element_by_id('u_0_5').is_selected()
print(status)
#driver.find_element_by_id('u_0_5').click()
driver.find_element_by_id('u_0_7').click()