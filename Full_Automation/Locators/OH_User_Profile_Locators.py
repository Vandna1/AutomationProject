import time

from selenium.webdriver.common.by import By

from Full_Automation.OH.SignUp import Signup


class UserProfileLocator:
    driver = None

    def __init__(self, driver):
        self.driver = driver

    def Call_URL(self):
        call_url = Signup(self.driver)
        call_url.Get_URL_Server()

    def Call_Login(self):
        self.driver.implicitly_wait(15)
        # time.sleep(2)
        # self.driver.get(
        #     "http://app3.onceplatform.com/")  # will go to the Oncehub login screen after authentication pass.
        # print("Get the URL")
        self.driver.maximize_window()  # It will maximize the size of the window.
        print("Maximized successfully")
        self.driver.find_element(By.XPATH, value="//input[@id='email']").send_keys("bite-idea-88@staticso2.com")
        time.sleep(5)
        self.driver.find_element(By.XPATH, value="//input[@id='password']").send_keys("testing@123")
        time.sleep(5)
        self.driver.find_element(By.XPATH, value="//button[@id='signIn']").click()
        print("signin button has been pressed")
        time.sleep(5)

    def Goto_My_Profile(self):
        self.driver.implicitly_wait(40)
        self.driver.find_element(By.ID, value="rAccountIcon").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, value="//span[contains(text(),'My profile')]").click()

    def Goto_Edit_Profile(self):
        self.driver.implicitly_wait(40)
        time.sleep(2)
        self.driver.find_element(By.XPATH, value="//span[contains(text(),'Users')]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, value="//div[@class='usersName']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,
                                 value="//div[@class='list-data']//button[@class='oui-icon-button "
                                       "oui-primary']//oui-icon[@class='oui-icon']").click()
        time.sleep(2)
        self.driver.find_element(By.ID, value="lastNameTxt3").clear()
        self.driver.find_element(By.ID, value="lastNameTxt3").send_keys("Thakurrrrrrrrr")
        time.sleep(5)
        self.driver.find_element(By.XPATH, value="//span[contains(text(),'Save')]").click()

    def Goto_Calendar_Connection(self):
        self.driver.implicitly_wait(30)
        time.sleep(10)
        self.driver.find_element(By.XPATH,
                                 value="//span[contains(text(),'Calendar connection')]").click()
        self.driver.find_element(By.XPATH, value="//a[@id='disconnectAnchor']").click()
        time.sleep(5)
        print("yes")
        self.driver.find_element(By.XPATH, value="//*[@id='connectToSameCalendar']").click()
        time.sleep(2)
        print("Yoo")
        self.driver.find_element(By.XPATH, value="//span[contains(text(),'Disconnect anyway')]").click()

        time.sleep(5)
        self.driver.find_element(By.XPATH, value="//button[@id='ExchangeCalendarConnectBtn']//span["
                                                 "@class='oui-button-wrapper'][contains(text(),"
                                                 "'Connect')]").click()
        print("Exchange calendar button has been pressed")
        self.driver.find_element(By.XPATH, value="//*[@id='email']").send_keys(
            "amit.singh@devsunil.onmicrosoft.com")
        time.sleep(5)
        self.driver.find_element(By.XPATH, value="//*[@id='password']").send_keys("schEdu1e@1234")
        time.sleep(5)
        self.driver.find_element(By.XPATH,
                                 value="//*[@id='oui-dialog-1']/div[3]/div[2]/button/span").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, value="//oui-select[@placeholder='Duration']//div["
                                                 "@class='oui-select-value']").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, value="//span[contains(text(),'30 minutes')]").click()
        print("working till here")

    def Goto_Email_notification(self):
        self.driver.implicitly_wait(30)
        time.sleep(10)
        self.driver.find_element(By.XPATH,
                                 value="//span[contains(text(),'Email notifications')]").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, value="//div[@class='form-inline']//input["
                                                 "@class='oui-input-element oui-input oui-primary "
                                                 "cdk-text-field-autofill-monitored ng-untouched "
                                                 "ng-pristine ng-valid']").send_keys("vanii")
        time.sleep(3)
        self.driver.find_element(By.XPATH, value="//span[contains(text(),'Discard')]").click()
        time.sleep(3)

    def Goto_SMS_Notification(self):
        self.driver.implicitly_wait(30)
        self.driver.find_element(By.XPATH, value="//span[contains(text(),'SMS notifications')]").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, value="//span[@class='oui-slider round']").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, value="//span[contains(text(),'Discard')]").click()
        time.sleep(3)

    def Goto_Date_And_Time(self):
        self.driver.implicitly_wait(30)
        time.sleep(10)
        self.driver.find_element(By.XPATH, value="//span[contains(text(),'Date and time')]").click()
        print("Click on DAte and Time")
        time.sleep(3)
        self.driver.find_element(By.XPATH, value="//label[contains(text(), 'Default time "
                                                 "zone')]//following-sibling::div[@class='form-control "
                                                 "ng-star-inserted']")
        time.sleep(3)
        # selected_country = driver.find_element(By.XPATH, value="//*[@id='oui-option-10203']/span").click()
        # time.sleep(3)
        self.driver.find_element(By.XPATH, value="//span[contains(text(),'Save')]").click()
        time.sleep(3)

    def Goto_Password(self):
        self.driver.implicitly_wait(30)
        self.driver.find_element(By.XPATH, value="//li[@class='sl-sidenav-link ng-star-inserted']//span["
                                                 "@class='sl-sidenav-link-text'][contains(text(),"
                                                 "'Password')]").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, value="//input[@id='current-password']").send_keys("testing@123")
        time.sleep(2)
        self.driver.find_element(By.XPATH, value="//input[@id='new-password']").send_keys("test@123")
        time.sleep(2)
        self.driver.find_element(By.XPATH, value="//input[@id='re-type-password']").send_keys("test@123")
        time.sleep(2)
        self.driver.find_element(By.XPATH, value="//span[contains(text(),'Discard')]").click()

    def Goto_Authentication(self):
        self.driver.implicitly_wait(30)
        time.sleep(5)
        self.driver.find_element(By.XPATH, value="//span[contains(text(),'Authentication')]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, value="//span[@class='oui-slider round']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, value="//input[@id='current-password']").send_keys("testing@123")
        time.sleep(2)
        self.driver.find_element(By.XPATH, value="//span[contains(text(),'Submit')]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, value="//input[@placeholder='Include area code or any "
                                                 "other prefix']").send_keys("8628077343")
        self.driver.find_element(By.XPATH, value="//span[contains(text(),'Discard')]").click()

    def Goto_ScheduleOnce(self):
        self.driver.implicitly_wait(30)
        time.sleep(5)
        self.driver.find_element(By.XPATH, value="//span[contains(text(),'ScheduleOnce')]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, value="//oui-checkbox[@id='pay-setup']//div["
                                                 "@class='oui-checkbox-background']//*["
                                                 "local-name()='svg']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, value="//span[contains(text(),'Discard')]").click()
