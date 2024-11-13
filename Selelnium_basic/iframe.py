# there are four method
# locate the drop down which is available inside the frame (VISIBLE BY TEXT)
# name of the frame
# name of the id
# name of the frame by index
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()

driver.get("https://www.hyrtutorials.com/p/frames-practice.html")
driver.maximize_window()

driver.find_element(By.XPATH,'//*[@id="name"]').send_keys("Hello Frames")

# laocate the drop down which is avaiable inside the frame
# name of the frame
# id of the frame
# Webelement
# Index-- when we have less no of frames

##laocating the frame with its id/name attribute
driver.switch_to.frame("frm1")

drp1=Select(driver.find_element(By.XPATH,'//*[@id="selectnav2"]'))
drp1.select_by_visible_text("Home")

driver.switch_to.default_content() # driver is pointing on degault location ie web page

#locating the frame with web element

frame2=driver.find_element(By.XPATH,'//*[@id="frm2"]')
driver.switch_to.frame(frame2)

driver.find_element(By.XPATH,'//*[@id="firstName"]').send_keys("David")

# driver is pointing on degault location ie web page
driver.switch_to.default_content()
frame3=driver.find_element(By.XPATH,'//*[@id="frm3"]')
driver.switch_to.frame(frame3)


drp3=Select(driver.find_element(By.XPATH,'//*[@id="selectnav1"]'))
drp3.select_by_visible_text("-- XPath")
