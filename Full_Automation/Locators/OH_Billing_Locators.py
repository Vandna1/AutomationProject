from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from Full_Automation.OH.SignUp import Signup


class BillingLocator:
    def __init__(self, driver):
        self.driver = driver

    def Click_On_Biiling_Butn(self):
        self.driver.implicitly_wait(20)
        time.sleep(10)
        self.driver.find_element(By.XPATH, value='//body/oh-root/div/sl-sidenav-container/sl-sidenav/div/perfect'
                                                 '-scrollbar '
                                                 '/div/div[3]/div[1]').send_keys(
            Keys.END)  # Use send_keys(Keys.HOME) to scroll up to the top of page
        self.driver.find_element(By.XPATH, value="//span[contains(text(),'Billing')]").click()

    def Click_On_Product(self):
        self.driver.implicitly_wait(20)
        time.sleep(10)
        self.driver.find_element(By.XPATH, value="//span[contains(text(),'Products')]").click()

        self.driver.find_element(By.XPATH, value="//span[contains(text(),'Purchase now')]").click()

        self.driver.find_element(By.XPATH, value="//div[@class='backButton']//a").click()

    def Click_On_Payment_Method(self):
        self.driver.implicitly_wait(20)
        time.sleep(2)
        self.driver.find_element(By.XPATH, value='//body/oh-root/div/sl-sidenav-container/sl-sidenav/div/perfect'
                                                 '-scrollbar '
                                                 '/div/div[3]/div[1]').send_keys(Keys.END)
        self.driver.find_element(By.XPATH, value="//span[contains(text(),'Payment methods')]").click()
        self.driver.find_element(By.XPATH, value="//span[contains(text(),'Purchase now')]").click()
        self.driver.find_element(By.XPATH, value="//div[@class='backButton']//a").click()

    def Click_On_Notification(self):
        self.driver.implicitly_wait(20)
        time.sleep(2)
        self.driver.find_element(By.XPATH, value='//body/oh-root/div/sl-sidenav-container/sl-sidenav/div/perfect'
                                                 '-scrollbar'                                   '/div/div[3]/div['
                                                 '1]').send_keys(Keys.END)
        self.driver.find_element(By.XPATH, value="//span[contains(text(),'Notifications')]").click()
        self.driver.find_element(By.XPATH, value="//span[contains(text(),'Purchase now')]").click()
        self.driver.find_element(By.XPATH, value="//div[@class='backButton']//a").click()

    def Click_On_Transcation(self):
        self.driver.implicitly_wait(20)
        time.sleep(2)
        self.driver.find_element(By.XPATH, value="//span[contains(text(),'Transactions')]").click()
