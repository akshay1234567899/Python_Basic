from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/#google_vignette")
min=driver.find_element(By.XPATH,'//*[@id="slider-range"]/span[1]')
max=driver.find_element(By.XPATH,'//*[@id="slider-range"]/span[2]')
print(min.location)
print(max.location)
driver.implicitly_wait(4)
act=ActionChains(driver)

act.drag_and_drop_by_offset(min,100,0).perform() # only x axis change
act.drag_and_drop_by_offset(max,-40,0).perform()
driver.implicitly_wait(4)

print(min.location)
print(max.location)