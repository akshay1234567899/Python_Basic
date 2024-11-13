from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()

driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()
driver.find_element(By.XPATH,"//a[contains(text(),'Iframe with in an Iframe')]").click()

frame1=driver.find_element(By.XPATH,'//div[@id="Multiple"]/iframe')
driver.switch_to.frame(frame1)
#
driver.switch_to.frame(0)
driver.find_element(By.XPATH,'//input[@type="text"]').send_keys("Hello")


