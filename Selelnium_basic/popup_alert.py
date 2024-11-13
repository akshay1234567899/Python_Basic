import requests as requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()

# driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.get("https://mypage.rediff.com/login/dologin")
driver.maximize_window()
driver.find_element(By.XPATH,"//input[@value='Login']").click()
alert_window=driver.switch_to.alert
# alert_window.send_keys("Welcome to the world of alerts")
# actual=driver.find_element(By.XPATH,'//*[@id="result"]').text
# validation :
# exp="You entered: welcome"
# if (exp==actual):
#     print("Test Passed")
# else:
#     print("Test Passed")

# print("the textof the alert window is",alert_window)
alert_window.accept()
# click on ok option from alert window
# alert_window.dismiss()
# click on cancel option from alert window