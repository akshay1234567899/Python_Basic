import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()
driver.switch_to.frame(0)
driver.find_element(By.XPATH,'//input[@id="datepicker"]').click()

year='2020'
month='May'
date='10'
while True:
    mon=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text
    yr=driver.find_element(By.XPATH,'//span[@class="ui-datepicker-year"]').text

    if (mon==month and yr==year):
        break
    else:
        # driver.find_element(By.XPATH,'//span[@class="ui-icon ui-icon-circle-triangle-e"]').click()
        driver.find_element(By.XPATH, '//span[@class="ui-icon ui-icon-circle-triangle-w"]').click()

# select date:
dates=driver.find_elements(By.XPATH,'//div[@id="ui-datepicker-div"]/table/tbody/tr/td/a')
for i in dates:
    if i.text == date:
        i.click()
        break
time.sleep(5)
