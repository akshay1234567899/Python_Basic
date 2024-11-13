# //[start-with(@name,'s') and @class='btn btn-default button-search']

# xpath example:
# self Node
# //*[contains(text(),'JSW Energy Ltd.')]/self::a
# //*[contains(text(),'JSW Energy Ltd.')]/parent::td

# find elements: return list of webelements
# find element : return webelement
# example : # //*[contains(text(),'JSW Energy Ltd.')]/ancestor::td
# //*[contains(text(),'JSW Energy Ltd.')]/ancestor::*

# how to locate the child
# //*[contains(text(),'JSW Energy Ltd.')]/ancestor::tr/child::td

# decendent node
# //*[contains(text(),'JSW Energy Ltd.')]/ancestor::tr/descendant::td

# following::
# //*[contains(text(),'JSW Energy Ltd.')]/ancestor::tr/following::*



# relative locator: introduce in selenium 4.o
# driver.find_element(locate_with(By.Tag_Name,"li").to_right_of(book2)).text
# driver.find_element(locate_with(By.Tag_Name,"li").to_left_of(book2)).text


# descendant :


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with

# Initialize the WebDriver
driver = webdriver.Chrome()

# Open the page where the elements exist
driver.get("https://automationbookstore.dev/")

# Find the reference element 'book2' (you need to replace 'your_book2_locator' with the actual locator)
book2 = driver.find_element(By.ID, "book2")  # Example: locating by ID, adjust as needed

# Locate the element to the right of 'book2' (assuming it's an 'li' tag)
element_to_right = driver.find_element(locate_with(By.TAG_NAME, "li").to_right_of(book2))

# Print the text of the located element
print(element_to_right.text)

# Close the driver
driver.quit()
