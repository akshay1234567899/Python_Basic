# declare
# usage

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.wait import  WebDriverWait

driver=webdriver.Chrome()
driver.maximize_window()
# wait_for_page=WebDriverWait(driver,10)
# polling wait
class SuchElementException:
    pass


mywait=WebDriverWait(driver,10,poll_frequency=2,ignored_exceptions=[Exception])
driver.get("https://www.google.com")
exception=driver.find_element(By.XPATH,"//textarea[@id='APjFqb']")
exception.send_keys("selinium")
exception.submit()
# user explicit condition
link = mywait.until(EC.presence_of_element_located((By.XPATH, "//h3[text()='Selenium']")))
link.click()