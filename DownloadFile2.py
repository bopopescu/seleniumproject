from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:\selenium\drivers\chromedriver.exe")
driver.get("http://demo.automationtesting.in/FileDownload.html")

driver.maximize_window()

driver.find_element_by_id("textbox").send_keys("Testing form")

driver.find_element_by_id("createTxt").click()

driver.find_element_by_id("link-to-download").click()



