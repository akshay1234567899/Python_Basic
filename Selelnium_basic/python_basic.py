# https://www.example.com.

from selenium import webdriver
# launch browser
driver=webdriver.Chrome()

# Nevigate to the website
driver.get("https://www.example.com")
driver.implicitly_wait(5)

# get title of the page
title=driver.title
print(title)

# close driver
driver.close()