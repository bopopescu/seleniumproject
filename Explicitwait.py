from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver=webdriver.Chrome(executable_path="C:\selenium\drivers\chromedriver.exe")
driver.implicitly_wait(5)
driver.maximize_window()

driver.get("https://www.expedia.com")
driver.find_element_by_id('tab-flight-tab-hp').click()
time.sleep(4)

driver.find_element_by_id('flight-origin-hp-flight').send_keys("SFO")
time.sleep(5)

driver.find_element_by_id("flight-destination-hp-flight").send_keys("NYC")

driver.find_element_by_id('flight-departing-hp-flight').clear()
driver.find_element_by_id('flight-departing-hp-flight').send_keys("10/10/2019")

driver.find_element_by_id("flight-returning-hp-flight").send_keys('11/11/2019')

driver.find_element_by_xpath("//*[@id='gcw-flights-form-hp-flight']/div[7]/label/button").click()

wait=WebDriverWait(driver,10)
element=wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='stopFilter_stops-0']")))

element.click()
time.sleep(3)
driver.quit()