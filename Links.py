from selenium import webdriver

driver=webdriver.Chrome(executable_path='C:\selenium\drivers\chromedriver.exe')
driver.get('http://newtours.demoaut.com')
links=driver.find_elements_by_tag_name('a')
print(len(links))
for link in links:
    print(link.text)

driver.find_element_by_link_text('Hotels').click()