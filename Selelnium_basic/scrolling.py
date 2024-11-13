import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# usage of javascript executor class in selenium....................
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://demo.nopcommerce.com/register")
driver.maximize_window()

# scroll down page
time.sleep(5)
driver.execute_script("window.scrollBy(0,3000)","")
value=driver.execute_script("return window.pageYOffset;")
print("number of pixels moved :",value)

register=driver.find_element(By.XPATH,'//button[@name="register-button"]')
time.sleep(5)
driver.execute_script("arguments[0].scrollIntoView();", register)
value=driver.execute_script("return window.pageYOffset;")
print("number of pixels moved :",value)

driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
value=driver.execute_script("return window.pageYOffset;")
print("number of pixels moved :",value)

