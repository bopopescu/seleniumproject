import XLUtils
from selenium import webdriver
driver=webdriver.Chrome(executable_path="C:\selenium\drivers\chromedriver.exe")
driver.get('http://newtours.demoaut.com')
driver.maximize_window()
path="C:/Users/amruth/Desktop/Hemraj/Login1.xlsx"
rows=XLUtils.getRowCount(path,'Sheet1')

for r in range(2,rows+1):
    username=XLUtils.readData(path,'Sheet1',r,1)
    password=XLUtils.readData(path,'Sheet1',r,2)

    driver.find_element_by_name('userName').send_keys(username)
    driver.find_element_by_name('password').send_keys(password)
    driver.find_element_by_name('login').click()

    if driver.title=='Find a Flight: Mercury Tours:':
        print("Test passed")
        XLUtils.writeData(path,'Sheet1',r,3,"Test passed")
    else:
        print("Test failed")
        XLUtils.writeData(path,'Sheet1',r,3,'Test failed')

    driver.find_element_by_link_text('Home').click()


