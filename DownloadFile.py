from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
chromeoptions=Options()
chromeoptions.add_experimental_option("prefs",{"download.default_directory": "C:/Users/amruth/Desktop/Hemraj/Mumbai"})
driver=webdriver.Chrome(executable_path='C:\selenium\drivers\chromedriver.exe',options=chromeoptions)
driver.get('http://demo.automationtesting.in/FileDownload.html')

driver.find_element_by_id('textbox').send_keys('Hi hemraj')
driver.find_element_by_id('createTxt').click()
driver.find_element_by_id('link-to-download').click()
time.sleep(3)

driver.find_element_by_id('pdfbox').send_keys('Hello hemraj')
driver.find_element_by_id('createPdf').click()
driver.find_element_by_id('pdf-link-to-download').click()

time.sleep(3)

#driver.close()

