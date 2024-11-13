
import random
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.flipkart.com/")
driver.implicitly_wait(5)

driver.find_element(By.XPATH, "//input[@placeholder='Search for Products, Brands and More']").send_keys("laptop hp")


suggestion_list = driver.find_elements(By.XPATH, '//ul[@class="_1sFryS _2x2Mmc _3ofZy1"]/li')
print("Number of suggestions found:", len(suggestion_list))
driver.implicitly_wait(9)

# if suggestion_list:
#     random_suggestion = random.choice(suggestion_list)
#     print("Randomly selected suggestion:", random_suggestion.text)
#     random_suggestion.click()

for suggestion in suggestion_list:
        print("Selecting suggestion:", suggestion.text)
        suggestion.click()
        break
driver.implicitly_wait(10)

