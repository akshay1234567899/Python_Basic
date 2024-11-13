import time

from docutils.nodes import option
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php")
time.sleep(5)
driver.find_element(By.XPATH,'//input[@id="name"]').send_keys("demo test")

driver.find_element(By.XPATH,'//input[@id="email"]').send_keys("demotest123@gmail.com")
radio_button = driver.find_element(By.XPATH, '//input[@name="gender"]')
radio_button.click()

driver.find_element(By.XPATH,'//input[@id="mobile"]').send_keys("9084848293")
time.sleep(9)
driver.find_element(By.XPATH,'//input[@id="dob"]').send_keys("04/05/2000")
driver.find_element(By.XPATH,'//input[@id="subjects"]').send_keys("subject for testing")
driver.find_element(By.XPATH,'//input[@id="hobbies"]').click()
file_path = r"/Users/akshaydhiman/Desktop/Manual Interview Questions_pdf.pdf"
driver.find_element(By.XPATH, '//input[@id="picture"]').send_keys(file_path)

driver.find_element(By.XPATH,'//textarea[@id="picture"]').send_keys("Testing area ")
time.sleep(9)

driver.find_element(By.XPATH, '//select[@id="state"]').click()
dropdown_options = driver.find_elements(By.XPATH, '//select[@id="state"]/option')
for option in dropdown_options:
    if option.text == "Uttar Pradesh":
        option.click()
        break

time.sleep(9)

driver.find_element(By.XPATH,'//select[@id="city"]').click()
select_city=driver.find_elements(By.XPATH,'//select[@id="city"]/option')
for city in select_city:
    if city.text=='Lucknow':
        city.click()
        break

driver.find_element(By.XPATH,'//input[@type="submit"]').click()









# driver.find_element(By.XPATH,'//*[@id="select2-billing_state-container"]').click()
# states=driver.find_elements(By.XPATH,'//*[@id="billing_state"]/option')
# time.sleep(5)
# for state in states:
#     if state.text=="Chandigarh":
#         state.click()
#         time.sleep(5)
#         break