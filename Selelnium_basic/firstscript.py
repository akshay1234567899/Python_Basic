from selenium import webdriver
from selenium.webdriver.chrome.service import Service




service_obj = Service("/Users/akshaydhiman/Desktop/chromedriver-mac-arm64")
# driver=webdriver.Chrome()  #
driver = webdriver.Chrome(service=service_obj)
driver.get("https://www.google.com/")

