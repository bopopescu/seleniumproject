from selenium import webdriver
from selenium.webdriver import ActionChains

driver=webdriver.Chrome(executable_path="C:\selenium\drivers\chromedriver.exe")

driver.get("https://opensource-demo.orangehrmlive.com")

driver.find_element_by_name("txtUsername").send_keys("Admin")
driver.find_element_by_name("txtPassword").send_keys("admin123")
driver.find_element_by_name("Submit").click()

admin=driver.find_element_by_xpath("//*[@id='menu_admin_viewAdminModule']/b")
user_mgmt=driver.find_element_by_xpath("//*[@id='menu_admin_UserManagement']")
users=driver.find_element_by_xpath("//*[@id='menu_admin_viewSystemUsers']")

actions=ActionChains(driver)
actions.move_to_element(admin).move_to_element(user_mgmt).move_to_element(users).click().perform()