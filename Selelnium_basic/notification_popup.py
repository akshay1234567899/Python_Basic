from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

ops=webdriver.ChromeOptions()
ops.add_argument("--disable-notificatioin")

driver=webdriver.Chrome()
driver.get("https://whatmylocation.com/#google_vignette")
driver.maximize_window()

