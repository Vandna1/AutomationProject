from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.common.keys import Keys

from Full_Automation.Locators.OH_User_Profile_Locators import UserProfileLocator
from Full_Automation.Locators.SO_Event_Type_Locators import SOEventType
from Full_Automation.OH.User_Profile import Logi
from Full_Automation.OH.Webdriver_Get import Get_chrome_driver


class SOMasterPages:
    driver = None

    def __init__(self, driver):
        self.driver = driver

    def login_function_calling_Now(self):
        Call1 = Logi(self.driver)
        Call1.URL_file()
        Call1.Llogin()

    def Calling_Schedule_Once_Function(self):
        Call_SO1 = SOEventType(self.driver)
        Call_SO1.Schedule_Once()

    def Click_On_Add_Master_Page_Btn(self):
        self.driver.implicitly_wait(20)
        time.sleep(5)
        self.driver.find_element(By.XPATH, value="//div[@class='block mbpBlock ng-scope']//a[@class='addNew']["
                                                 "contains(text(),'+')]").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, value="//input[@id='mbpPublicName']").send_keys("MasterPage123")
        time.sleep(3)
        self.driver.find_element(By.XPATH, value="//input[@id='mbpName']").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, value="//input[@id='mbpLinkName']").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, value="//label[contains(text(),'Rule-based assignment (supports one-time "
                                                 "links)')]").click()
        time.sleep(3)
        # self.driver.find_element(By.XPATH, value="//div[@id='AddMasterBookingPagePopUp']//label[@class='sBtn']["
        #                                          "contains(text(),'Choose file')]").click()
        # # time.sleep(3)
        # self.driver.find_element(By.XPATH, value="//div[@id='AddMasterBookingPagePopUp']//label[@class='sBtn']["
        #                                          "contains(text(),'Choose file')]").send_keys(
        #     "C:/Users/VandanaThakur/Downloads/vanya.jpg")
        time.sleep(3)
        self.driver.find_element(By.XPATH, value="//div[@id='AddMasterBookingPagePopUp']//input[@class='btn']").click()
        time.sleep(3)

    def Click_On_Assignment_Btn(self):
        self.driver.implicitly_wait(20)
        time.sleep(5)
        self.driver.find_element(By.XPATH, value="//a[contains(text(),'Assignment')]").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, value="//input[@class='sBtn add-rule-btn ng-scope']").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, value="//td[2]//div[1]//div[1]//button[1]").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, value="//div[contains(text(),'15-minute meeting')]").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, value="//button[contains(text(),'Please Select')]").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, value="//div[contains(text(),'Booking_nature')]").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, value="//button[@class='dropdown-field ng-binding']").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, value="//label[contains(text(),'Raksh452')]").click()
        time.sleep(4)
        self.driver.find_element(By.XPATH, value="//div[@class='ng-scope']//div[@class='ng-scope']//input[@class='btn']").click()
        time.sleep(4)

    def Click_On_Label_Btn(self):
        self.driver.implicitly_wait(20)
        time.sleep(5)
        self.driver.find_element(By.XPATH, value="//a[contains(text(),'Labels and instructions')]").click()
        time.sleep(2)

    def Click_On_Public_Content(self):
        self.driver.implicitly_wait(20)
        time.sleep(5)
        self.driver.find_element(By.XPATH, value="//a[contains(text(),'Public content')]").click()
        time.sleep(2)

    def Click_On_Overview_Button(self):
        self.driver.implicitly_wait(20)
        time.sleep(5)
        self.driver.find_element(By.XPATH, value="//a[contains(text(),'Overview')]").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, value="//a[contains(text(),'https://go3.onceplatform.com/')]").click()
        self.driver.switch_to_window(self.driver.window_handles[1])
        time.sleep(3)
        
        
if __name__ == "__main__":
    driver = Get_chrome_driver().launch_chrome()
    obj = SOMasterPages(driver)
    obj.login_function_calling_Now()
    obj.Calling_Schedule_Once_Function()
    obj.Click_On_Add_Master_Page_Btn()
    obj.Click_On_Assignment_Btn()
    obj.Click_On_Label_Btn()
    obj.Click_On_Public_Content()
    obj.Click_On_Overview_Button()

