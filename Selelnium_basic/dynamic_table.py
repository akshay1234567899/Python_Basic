# # dynamic table:
# from docutils.nodes import tbody
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
#
#
# driver=webdriver.Chrome()
# driver.get("https://testautomationpractice.blogspot.com/")
# driver.maximize_window()
#
# rows=driver.find_elements(By.XPATH,'//*[@id="HTML1"]/div[1]/table/tbody/tr[1]')
# print("the numbers of rows",len(rows))
#
#
# column=driver.find_element(By.XPATH,'//*[@id="HTML1"]/div[1]/table/tbody/tr[5]/td[1]').text
# print("number of column:",column)
#
# # read all the rows anc column
# for r in range(2,len(rows)+1):
#     for c in range(1,len(column)+1):
#         data = driver.find_element(By.XPATH, '//*[@id="HTML1"]/div[1]/table/tbody/tr[r]/td[c]').text
#         print(data, end='  ')
# print()


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

rows = driver.find_elements(By.XPATH, '//*[@id="HTML1"]/div[1]/table/tbody/tr')
print("The number of rows:", len(rows))

columns = driver.find_elements(By.XPATH, '//*[@id="HTML1"]/div[1]/table/tbody/tr[1]/th')
print("The number of columns:", len(columns))

for r in range(2, len(rows) + 1):
    for c in range(1, len(columns) + 1):
        data = driver.find_element(By.XPATH, f'//*[@id="HTML1"]/div[1]/table/tbody/tr[{r}]/td[{c}]').text
        print(data, end='  ')
    print()

