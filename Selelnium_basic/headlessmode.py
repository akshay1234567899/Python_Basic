from selenium import webdriver

def headlessEdge():

    ops = webdriver.EdgeOptions()
    ops.add_argument("--headless")
    driver = webdriver.Edge(options=ops)
    return driver


def headlessChrome():
    ops = webdriver.ChromeOptions()
    ops.add_argument("--headless")
    driver = webdriver.Chrome(options=ops)
    return driver

driver = headlessChrome()
# driver = headlessEdge()
driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/#google_vignette")
print(driver.title)
print(driver.current_url)

