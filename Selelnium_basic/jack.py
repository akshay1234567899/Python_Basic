from selenium import webdriver
from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager

# Set up the WebDriver with WebDriver Manager
driver = webdriver.Chrome()

# Navigate to the target URL
driver.get("http://www.automationpractice.pl/index.php")

# Find the first <h1> element and print its text content
h1_element = driver.find_element(By.TAG_NAME, "h1")
print("First <h1> Text:", h1_element.text)

# Close the browser
driver.quit()
