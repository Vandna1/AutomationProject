from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


class URL:
    def url(self):
        driver.get("http://app3.onceplatform.com/")
        # return driver


obj1 = URL()
obj1.url()
