import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestParallel:
    def test_chrome(self):
        driver = webdriver.Chrome()
        try:
            driver.get("https://www.cit.com/cit-bank/resources/calculators/certificate-of-deposit-calculator")
            time.sleep(5)
            driver.find_element(By.XPATH, "//body//app-root//app-header//app-button//div[2]")
            page_title = driver.title
            assert driver.title == page_title
        finally:
            driver.quit()

    def test_edge(self):
        driver = webdriver.Edge()
        try:
            driver.get("https://www.cit.com/cit-bank/resources/calculators/certificate-of-deposit-calculator")
            time.sleep(5)
            driver.find_element(By.XPATH, "//body//app-root//app-header//app-button//div[2]")
            page_title = driver.title
            assert driver.title == page_title
        finally:
            driver.quit()

    def test_firefox(self):
        driver = webdriver.Firefox()
        try:
            driver.get("https://www.cit.com/cit-bank/resources/calculators/certificate-of-deposit-calculator")
            time.sleep(5)
            driver.find_element(By.XPATH, "//body//app-root//app-header//app-button//div[2]")
            page_title = driver.title
            assert driver.title == page_title
        finally:
            driver.quit()
# pytest -v -s /Users/akshaydhiman/PycharmProjects_SDET_08_01/pythonProject/pytest/test_parallel.py
# pytest -v -s -n=3 /Users/akshaydhiman/PycharmProjects_SDET_08_01/pythonProject/pytest/test_parallel.py ( thread count )

    