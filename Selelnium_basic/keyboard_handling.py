import time

from selenium import webdriver
from selenium.webdriver import ActionChains,Keys
# from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.implicitly_wait(10)

driver.get("https://text-compare.com/")
# driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_ev_ondblclick3")
time.sleep(7)
take_currentURL=driver.current_url
# driver.get_screenshot_as_file("")
print(take_currentURL)
driver.maximize_window()
# ctrl+A,ctrl+c,Tab and ctrl+v
# driver.switch_to.frame("iframeResult")
act=ActionChains(driver)
driver.find_element(By.XPATH,"//*[@id='inputText1']").send_keys("Test selenium with python :)")
# box=driver.find_element(By.XPATH,"//input[@id='field1']")
# box.clear()
# box.send_keys("Test selenium with python :)")

# input box-1
act.key_down(Keys.CONTROL)
act.send_keys("a")
act.key_up(Keys.CONTROL)
act.perform()
time.sleep(7)

act.key_down(Keys.CONTROL)
act.send_keys("c")
act.key_up(Keys.CONTROL)
act.perform()

# press the tab button
act.send_keys(Keys.TAB).perform()
time.sleep(7)

# paste text box-2
driver.find_element(By.XPATH,"//*[@id='inputText2']").send_keys("Test selenium with python :)")
act.key_down(Keys.CONTROL)
act.send_keys("V")
act.key_up(Keys.CONTROL)
act.perform()

time.sleep(7)
driver.quit()

