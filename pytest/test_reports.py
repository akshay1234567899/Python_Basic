import time

import pytest
from selenium.webdriver.common.by import By


class TestLogin:
    def test_login(self, setup):
        self.driver = setup
        self.driver.get("http://www.automationpractice.pl/index.php?controller=authentication&back=my-account")
        self.driver.find_element(By.XPATH, "//input[@id='email']").send_keys("sdetsdet12@gmail.com")
        self.driver.find_element(By.ID, "passwd").send_keys("test123")
        self.driver.find_element(By.ID, "SubmitLogin").click()

        heading = self.driver.find_element(By.XPATH, "//h1[@class='page-heading']").text
        time.sleep(5)
        assert heading == "MY ACCOUNT"
        self.driver.close()

# pytest -v -s /Users/akshaydhiman/PycharmProjects_SDET_08_01/pythonProject/pytest/testfixture.py --browser chrome --html=report.html
