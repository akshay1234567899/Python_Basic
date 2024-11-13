import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
button=driver.find_element(By.XPATH,'/html/body/div/section/div/div/div/p/span')

act=ActionChains(driver)
act.context_click(button).perform()
copy=driver.find_element(By.XPATH,'/html/body/ul/li[3]/span')
copy.click()
# driver.switch_to.alert.accept()
alert = driver.switch_to.alert
actual = alert.text
expected="clicked: copy"
if actual==expected:
    print("text equal to expected result")
else:
    print("text not equal to expected result")
alert.accept()
time.sleep(6)

