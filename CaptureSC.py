from selenium import webdriver
driver=webdriver.Chrome(executable_path='C:\selenium\drivers\chromedriver.exe')
driver.get('http://newtours.demoaut.com/mercurywelcome.php')
#driver.save_screenshot('C:/Users/amruth/Desktop/Hemraj/Screeshot/scree.png')
driver.get_screenshot_as_file('C:/Users/amruth/Desktop/Hemraj/Screeshot/screen.png')