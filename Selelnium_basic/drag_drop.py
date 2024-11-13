import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")

rome=driver.find_element(By.XPATH,"//div[@id='box6']")
italy=driver.find_element(By.XPATH,"//div[@id='box106']")
act=ActionChains(driver)
act.drag_and_drop(rome,italy).perform()

washington=driver.find_element(By.XPATH,"//div[@id='box3']")
swiden=driver.find_element(By.XPATH,"//div[@id='box102']")
act.drag_and_drop(washington,swiden).perform()

time.sleep(6)
assert "box6" in italy.get_attribute("innerHTML"), "Rome was not dropped in Italy"
print("Rome was successfully dropped in Italy.")
time.sleep(6)
assert "box6" in washington.get_attribute("innerHTML"),"washington was not dropeed in swiden"
print("washington was not successfully dropped in Italy.")




