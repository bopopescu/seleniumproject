from selenium import webdriver
driver=webdriver.Chrome(executable_path="C:\selenium\drivers\chromedriver.exe")
driver.get('https://www.amazon.in/')
driver.maximize_window()

cookie=driver.get_cookies()
print(cookie)
print(len(cookie))

cookies={'name':'hemraj','value':'8095789449'}
driver.add_cookie(cookies)

cookie=driver.get_cookies()
print(cookie)
print(len(cookie))

driver.delete_cookie('hemraj')
cookies=driver.get_cookies()
print(cookies)
print(len(cookies))

driver.delete_all_cookies()
cookie=driver.get_cookies()
print(len(cookie))