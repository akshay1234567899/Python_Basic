import time

import pytest
from pexpect import expect
from selenium import webdriver
from selenium.webdriver.common.by import By



@pytest.fixture()
def setup(browser):
   if browser=='chrome':
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    return driver
   elif browser=='edge':
       driver = webdriver.Edge()
       driver.implicitly_wait(10)
       driver.maximize_window()
       return driver
   elif browser=="firefox":
       driver = webdriver.Firefox()
       driver.implicitly_wait(10)
       driver.maximize_window()
       return driver


def pytest_addoption(parser):    # This will get the value from CLI
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):       # This will return the Browser value to setup method
    return request.config.getoption("--browser")

# # It is hook for Adding Environment info to HTML Report
# def pytest_configure(config):
#     config._metadata['Project Name'] = 'Orange HRM'
#     config._metadata['Module Name'] = 'Login Module'
#     config._metadata['Tester Name'] = 'Pavan'

# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

class TestLogin:
    def test_login(self, setup):
        driver = setup
        driver.get("http://www.automationpractice.pl/index.php?controller=authentication&back=my-account")
        driver.find_element(By.XPATH, "//input[@id='email']").send_keys("sdetsdet12@gmail.com")
        driver.find_element(By.ID, "passwd").send_keys("test123")
        driver.find_element(By.ID, "SubmitLogin").click()

        heading = driver.find_element(By.XPATH, "//h1[@class='page-heading']").text
        time.sleep(5)
        assert heading == "MY ACCOUNT"
# pytest -v -s /Users/akshaydhiman/PycharmProjects_SDET_08_01/pythonProject/pytest/conftest.py --browser chrome