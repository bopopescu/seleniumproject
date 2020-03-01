from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
driver=webdriver.Chrome(executable_path="C:\selenium\drivers\chromedriver.exe")
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
print(driver.title)
count_textField=driver.find_elements_by_class_name("text_field")
print(len(count_textField))
driver.find_element_by_name("RESULT_TextField-1").send_keys("Hemraj")
driver.find_element_by_name("RESULT_TextField-2").send_keys("karuvinamane")
driver.find_element_by_name("RESULT_TextField-3").send_keys("9886585790")
driver.find_element_by_name("RESULT_TextField-4").send_keys("India")
driver.find_element_by_name("RESULT_TextField-5").send_keys("Banglore")
driver.find_element_by_name("RESULT_TextField-6").send_keys("hemraj_k07@yahoo.com")

#driver.find_element_by_id("RESULT_RadioButton-7_0").click()

#driver.find_element_by_id("RESULT_CheckBox-8_5").click()

#driver.find_element_by_css_selector("input[value=CheckBox-0]").click()

status=driver.find_element_by_id("RESULT_RadioButton-9")
drop_down=Select(status)
#drop_down.select_by_visible_text("Morning")
#drop_down.select_by_index(2)
drop_down.select_by_value("Radio-2")

print(len(drop_down.options))

options=drop_down.options

for option in options:
    print(option.text)
