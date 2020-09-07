from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class SecurityLocator:
    def __init__(self, driver):
        self.driver = driver

    def Click_On_Security_btn(self):
        self.driver.implicitly_wait(20)
        time.sleep(5)
        self.driver.find_element(By.XPATH, value='//body/oh-root/div/sl-sidenav-container/sl-sidenav/div/perfect'
                                                 '-scrollbar '
                                                 '/div/div[3]/div[1]').send_keys(Keys.END)
        self.driver.find_element(By.XPATH, value="//span[contains(text(),'Security')]").click()

    def Click_On_SSO(self):
        self.driver.implicitly_wait(20)
        time.sleep(5)
        self.driver.find_element(By.XPATH, value="//span[contains(text(),'SSO')]").click()

    def Click_On_Password_Policy(self):
        self.driver.implicitly_wait(20)
        time.sleep(5)
        self.driver.find_element(By.XPATH, value="//span[contains(text(),'Password policies')]").click()
        self.driver.find_element(By.XPATH, value="//span[@class='oui-select-value-text ng-star-inserted']").click()
        self.driver.find_element(By.XPATH, value="//span[@class='oui-option-text'][contains(text(),'8')]").click()
        self.driver.find_element(By.XPATH, value="//oui-checkbox[@id='specialcharacterCB']//div["
                                                 "@class='oui-checkbox-background']//*[local-name()='svg']").click()
        self.driver.find_element(By.XPATH, value="//span[contains(text(),'Discard')]").click()

    def Click_On_Account_Lookout_Policy(self):
        self.driver.implicitly_wait(20)
        time.sleep(10)
        self.driver.find_element(By.XPATH, value='//body/oh-root/div/sl-sidenav-container/sl-sidenav/div/perfect'
                                                 '-scrollbar '
                                                 '/div/div[3]/div[1]').send_keys(Keys.END)
        self.driver.find_element(By.XPATH, value="//span[contains(text(),'Account lockout policies')]").click()
        print("Account lookout button pressed")
        # driver.find_element(By.XPATH, value="//oui-radio-button[@id='accountEnabled']//div[
        # @class='oui-radio-outer-circle']").click() time.sleep(2) print("Checkbox selected") driver.find_element(
        # By.XPATH, value="//span[contains(text(),'Discard')]").click() print("Discarded")

    def Click_On_Session_Policy(self):
        self.driver.implicitly_wait(20)
        time.sleep(2)
        self.driver.find_element(By.XPATH, value='//body/oh-root/div/sl-sidenav-container/sl-sidenav/div/perfect'
                                                 '-scrollbar '
                                                 '/div/div[3]/div[1]').send_keys(Keys.END)
        self.driver.find_element(By.XPATH, value="//span[contains(text(),'Session policies')]").click()
        print("In the session policies")
        time.sleep(4)
        self.driver.find_element(By.XPATH, value="//oui-radio-button[@id='signOut']//div["
                                                 "@class='oui-radio-outer-circle']").click()
        time.sleep(4)
        self.driver.find_element(By.XPATH, value="//span[contains(text(),'Discard')]").click()