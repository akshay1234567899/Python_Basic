import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

# Set up WebDriver
driver = webdriver.Edge()
driver.implicitly_wait(10)

# Navigate to the website
driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_ev_ondblclick3")
time.sleep(7)

# Maximize the window
driver.maximize_window()

# Switch to the iframe where the input field is located
driver.switch_to.frame("iframeResult")

# Initialize ActionChains
act = ActionChains(driver)

# Find the input field
box = driver.find_element(By.XPATH, "//input[@id='field1']")

# Clear any existing text and input new text
box.clear()
box.send_keys("Test python")

# Wait for a few seconds to observe
time.sleep(2)

# Select all text (Ctrl + A) and copy it (Ctrl + C)
act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()  # Ctrl + A
time.sleep(1)
act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()  # Ctrl + C

# Wait for a few seconds to observe
time.sleep(2)

# Instead of using Tab, click on the same input field again (simulating focus)
box.click()

# Clear the field again before pasting
box.clear()

# Paste the copied text (Ctrl + V)
act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()  # Ctrl + V

# Wait to observe the pasted result
time.sleep(5)

# Close the WebDriver
driver.quit()
