# application command :
# conditioanl command:
# Browser command:
# Navigation command:

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
time.sleep(5)
# driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# print("The tile of the page is ",driver.title)
# print("the url of the page is ",driver.current_url)
# # page source get source code
# print("the source code of the page is",driver.page_source)




# conditioanl command:
driver.get("https://demo.nopcommerce.com/register?returnUrl=%2Fregister")
Application_logo=driver.find_element(By.XPATH,"//img[@alt='nopCommerce demo store']")
print(Application_logo.is_displayed())
enter_query=driver.find_element(By.XPATH,"//input[@id='small-searchterms']")
enter_query.send_keys("phone")
print(enter_query.get_attribute("value"))
Click_on_Search_icon=driver.find_element(By.XPATH,"//button[contains(text(),'Search')]")

time.sleep(5)
# Click_on_Search_icon.click()

# is_enabled ----- is check the enabled feature of the webelement
rd_male=driver.find_element(By.XPATH,"//input[@id='gender-male']")
rd_male.click()
print("Male radio Button Status",rd_male.is_selected())
rd_femail=driver.find_element(By.XPATH,'//input[@id="gender-female"]')

# driver.close()
# able to close where driver focused
