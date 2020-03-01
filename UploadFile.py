from selenium import webdriver
driver=webdriver.Chrome(executable_path="C:\selenium\drivers\chromedriver.exe")

driver.get('https://testautomationpractice.blogspot.com')
driver.maximize_window()
driver.switch_to_frame(0)
driver.find_element_by_id('RESULT_FileUpload-11').send_keys('C:/Users/amruth/Desktop/Ramesh/SSLC.pdf')