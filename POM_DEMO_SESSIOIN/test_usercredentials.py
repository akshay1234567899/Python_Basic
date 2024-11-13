import pytest

from selenium import webdriver
from LoginPageConcept import LoginPage


class TestLogin:
    def test_login(self):
        driver=webdriver.Chrome()
        driver.get("http://www.automationpractice.pl/index.php?controller=authentication&back=my-account")
        driver.implicitly_wait(5)
        driver.maximize_window()

        lp=LoginPage(driver)
        lp.setuserName("sdetsdet12@gmail.com")
        lp.setuserPassword("test123")
        lp.clicklogin()

        driver.implicitly_wait(5)
        actual=driver.title
        assert actual== "My account - My Shop"
