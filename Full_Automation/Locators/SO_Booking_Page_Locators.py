from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from Full_Automation.OH.User_Profile import Logi
from Full_Automation.OH.Webdriver_Get import Get_chrome_driver


class BookingPage:
    driver = None

    def __init__(self, driver):
        self.driver = driver

    def Click_On_Triple_Dot(self):
        self.driver.implicitly_wait(20)
        time.sleep(2)
        # booking_xpath = self.driver.find_element(By.XPATH, value="//span[contains(text(),'Booking_nature')]")
        # if booking_xpath in booking:

        self.driver.find_element(By.XPATH, value="//div[@class='borderBlock']//a[@class='menuBtn']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, value="// a[contains(text(), 'New Booking page')]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, value="//input[@id='bpPublicName']").send_keys("Raksh452")
        # self.driver.find_element(By.XPATH, value="//input[@id='bpPublicName']").send_keys(Keys.CONTROL + "v")

        time.sleep(4)
        self.driver.find_element(By.XPATH, value="//input[@id='bpName']").click()

        time.sleep(6)
        self.driver.find_element(By.XPATH, value="//input[@id='bpLinkName']").click()

        # time.sleep(2)
        # self.driver.find_element(By.XPATH, value="//div[@id='eventTypeSelect_chosen']//ul[@class='chosen-choices']").click()
        # time.sleep(2)
        # self.driver.find_element(By.XPATH, value="//div[@id='AddBookingPagePopUp']//div[@class='imageThumbHolderOuter ng-isolate-scope']//span[1]").click()
        time.sleep(4)
        self.driver.find_element(By.XPATH, value="//div[@id='AddBookingPagePopUp']//input[@class='btn']").click()
        print("Working till here")
        time.sleep(10)

    def BookingPage_Overview(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element(By.XPATH, value="//a[contains(text(),'https://go3.onceplatform.com/')]").click()
        self.driver.switch_to_window(self.driver.window_handles[1])
        time.sleep(15)
        self.driver.find_element(By.XPATH, value="//a[@title='Edit your time zone']").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, value="//input[@id='input_country']").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, value="//span[contains(text(),'India')]").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, value="//button[@id='tzConfirmBtn']").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//button[@id='NextPeriod']").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, value="//button[@title='Show available time slots for 21 September 2020']").click()
        time.sleep(3)

        self.driver.find_element(By.XPATH, value="//sotimeslot[contains(@class,'ng-scope ng-isolate-scope')]//button["
                                                 "contains(@class,'timeSlotSingle ng-pristine ng-untouched ng-valid "
                                                 "ng-binding ng-not-empty')][contains(text(),'4:00 PM')]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, value="//button[@id='bookSlot']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, value="//input[@name='customer_name']").send_keys("vanya")
        time.sleep(2)
        self.driver.find_element(By.XPATH, value="//input[@name='customer_email']").send_keys("mailtest469@gmail.com")
        time.sleep(2)
        self.driver.find_element(By.XPATH, value="//button[@class='sBtn CustomButtonColor formSubmitBtm']").click()

    # def Back_BUtton_Press(self):
    #     self.driver.implicitly_wait(20)
    #     time.sleep(3)
    #     self.driver.find_element(By.XPATH, "//div[@class='backButton']//a").click()

