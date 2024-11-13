import time
import pytest
from selenium.webdriver.common.by import By

# from pytest.conftest import browser


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
        driver.close()

# pytest -v -s /Users/akshaydhiman/PycharmProjects_SDET_08_01/pythonProject/pytest/testfixture.py --browser chrome