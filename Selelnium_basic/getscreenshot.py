import os

from selenium import webdriver


driver = webdriver.Chrome()
driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/#google_vignette")
# driver.save_screenshot(r"/Users/akshaydhiman/Desktop/BTES\ assignment ")
# driver.save_screenshot(os.getcwd()+"\\homepage.png")
# driver.get_screenshot_as_file(os.getcwd()+"HomePage.png")
screenshot_path = os.path.join(os.getcwd(), "HomePage.png")
driver.get_screenshot_as_file(screenshot_path)
driver.close()