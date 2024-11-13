# Mouse hover
# Right click
# double click
# Drag and Drop

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()

driver.get("https://demo.nopcommerce.com/register")
driver.maximize_window()
Header_computer=driver.find_element(By.XPATH,'//a[contains(text(),"Computers ")]')
notbook=driver.find_element(By.XPATH,"//ul[@class='top-menu notmobile']//a[normalize-space()='Notebooks']")

act=ActionChains(driver)
act.move_to_element(Header_computer).move_to_element(notbook).click().perform()
elctronic=driver.find_element(By.XPATH,'/html[1]/body[1]/div[6]/div[2]/ul[1]/li[2]/a[1]')
not_book=driver.find_element(By.XPATH,"(//a[normalize-space()='Notebooks'])[1]")
act.move_to_element(elctronic).move_to_element(not_book).click().perform()