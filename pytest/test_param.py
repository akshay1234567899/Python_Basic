import pytest
from selenium  import webdriver
from selenium.webdriver.common.by import By



class Testclass:
    @pytest.mark.parametrize("email,password", [("test9042@gmail.com", "test@12")])
    def test_credentials(self,email,password):
        driver=webdriver.Chrome()
        driver.get("http://www.automationpractice.pl/index.php?controller=authentication&back=my-account")
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.find_element(By.XPATH,"//input[@id='email']").send_keys(email)
        driver.find_element(By.XPATH,"//input[@id='passwd']").send_keys(password)
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH,"//span[normalize-space()='Sign in']").click()
        try:
            text=driver.find_element(By.XPATH,"//h1[contains(text(),'My account')]")
            assert  text=="MY ACCOUNT"
        finally:
            driver.close()