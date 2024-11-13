import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(5)
driver.find_element(By.XPATH,"//a[contains(text(),'OrangeHRM, Inc')]").click()

# switch to window()
parent=driver.current_window_handle
print("Print window handle:",parent)
# get the window id for multiple window

mul_win=driver.window_handles
print(mul_win)
for win_handle in mul_win:
    if win_handle != parent:
        driver.switch_to.window(win_handle)
        print(driver.title)
        break
    if driver.title=="Human Resources Management Software" or "OrangeHRM":
        driver.close()


# driver.switch_to.window(parent)
