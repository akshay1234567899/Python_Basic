from selenium.webdriver.common.by import By

from Selelnium_basic.python_basic import driver


class LoginPage:
    # locators
    email_address = "//input[@id='email']"
    user_Password = "//input[@id='passwd']"
    Sign_in = "//span[normalize-space()='Sign in']"

    # constructor
    def __init__(self, driver):
        self.driver = driver

    # Actions:

    def setuserName(self, username):
        usertxt = self.driver.find_element(By.XPATH,self.email_address)
        usertxt.send_keys(username)

    def setuserPassword(self, pwd):
        passtext = self.driver.find_element(By.XPATH, self.user_Password)
        passtext.send_keys(pwd)

    def clicklogin(self):
        button = self.driver.find_element(By.XPATH,self.Sign_in)
        button.click()
