import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
time.sleep(5)
driver.execute_script("window.scrollBy(0,1800)","")
value=driver.execute_script("return window.pageYOffset;")
driver.find_element(By.XPATH,'//*[@id="select2-billing_state-container"]').click()
states=driver.find_elements(By.XPATH,'//*[@id="billing_state"]/option')
time.sleep(5)
for state in states:
    if state.text=="Chandigarh":
        state.click()
        time.sleep(5)
        break
