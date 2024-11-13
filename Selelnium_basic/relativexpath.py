from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with

driver = webdriver.Chrome()
driver.get("https://automationbookstore.dev/")
book2 = driver.find_element(By.XPATH, "//h2[@id='pid2_title']")
element_to_right = driver.find_element(locate_with(By.TAG_NAME, "li").to_right_of(book2))
print(element_to_right.text)

driver.quit()