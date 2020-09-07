from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class PrivacyLocator:
    def __init__(self, driver):
        self.driver = driver

    def Click_On_Privacy_Module(self):
        self.driver.implicitly_wait(20)
        time.sleep(10)
        self.driver.find_element(By.XPATH, value='//body/oh-root/div/sl-sidenav-container/sl-sidenav/div/perfect'
                                                 '-scrollbar '
                                                 '/div/div[3]/div[1]').send_keys(Keys.END)

        self.driver.find_element(By.XPATH,
                                 value="//span[@class='sl-sidenav-category-text'][contains(text(),'Privacy')]").click()

    def Click_On_Privacy_Shield(self):
        self.driver.implicitly_wait(20)
        time.sleep(2)
        self.driver.find_element(By.XPATH, value="//span[contains(text(),'Privacy shield')]").click()

    def Click_On_GDPR_Info(self):
        self.driver.implicitly_wait(20)
        time.sleep(2)
        self.driver.find_element(By.XPATH, value="//span[contains(text(),'GDPR information')]").click()

    def Click_On_GDPR_Compliance(self):
        self.driver.implicitly_wait(20)
        time.sleep(2)
        self.driver.find_element(By.XPATH, value='//body/oh-root/div/sl-sidenav-container/sl-sidenav/div/perfect'
                                                 '-scrollbar '
                                                 '/div/div[3]/div[1]').send_keys(Keys.END)
        self.driver.find_element(By.XPATH, value="//span[contains(text(),'GDPR compliance')]").click()
