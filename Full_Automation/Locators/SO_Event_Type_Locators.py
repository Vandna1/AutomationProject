from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.common.keys import Keys

from Full_Automation.Locators.OH_User_Profile_Locators import UserProfileLocator
from Full_Automation.OH.User_Profile import Logi
from Full_Automation.OH.Webdriver_Get import Get_chrome_driver


class SOEventType:
    driver = None

    def __init__(self, driver):
        self.driver = driver

    def Schedule_Once(self):
        self.driver.implicitly_wait(20)
        time.sleep(5)
        self.driver.find_element(By.XPATH, value="//span[@class='product-link']").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, value="//a[contains(text(),'ScheduleOnce setup')]").click()
        time.sleep(10)
        print("in the SO")

    def Event_Type_Triple_Dots(self):
        self.driver.implicitly_wait(20)

        time.sleep(2)
        self.driver.find_element(By.XPATH, value="//div[@class='block eventsBlock ng-scope onboardingActive']//a["
                                            "@class='menuBtn']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, value="//a[@class='link newCat'][contains(text(),'New Category')]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, value="//input[@id='categoryName']").send_keys("Vanyaa")
        time.sleep(2)
        self.driver.find_element(By.XPATH, value="//div[@id='AddCategoryPopUp']//input[@class='btnLink']").click()

    def Edit_Triple_Dots(self):
        self.driver.implicitly_wait(20)
        time.sleep(2)
        self.driver.find_element(By.XPATH, value="//body/form/div/div[@class='draggedPage']/div[@class='container "
                                            "OuterContainer']/table/tbody/tr/td/table/tbody/tr/td/div["
                                            "@class='header-gap ng-scope']/div[@class='ng-scope']/div["
                                            "@class='mainSchePane ng-scope']/div[@class='selectServiceScreen']/div["
                                            "@class='blocksOuter']/div[@class='ng-scope']/div[@class='block "
                                            "eventsBlock ng-scope onboardingActive']/div["
                                            "@class='blockContent']/table[@class='eventTypelistTable']/tbody/tr["
                                            "@class='event-type-category ng-scope ng-isolate-scope']/td["
                                            "@class='no-paddingTD']/table/tbody/tr[1]/td[2]/div[1]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, value="//tr[@class='event-type-category ng-scope ng-isolate-scope']//tr[1]//td["
                                            "2]//div[1]//div[1]//div[2]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, value="//form[@name='EventTypeForm']//input[@name='name']").send_keys(
            "this duplicate")
        time.sleep(2)
        self.driver.find_element(By.XPATH, value="//body/form/div/div[@class='draggedPage']/div[@class='container "
                                            "OuterContainer']/table/tbody/tr/td/table/tbody/tr/td/div["
                                            "@class='header-gap ng-scope']/div[@class='ng-scope']/div["
                                            "@class='mainSchePane ng-scope']/div[@class='selectServiceScreen']/div["
                                            "@class='blocksOuter']/div[7]/div[1]/form[1]/div[2]/input[1]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, value="//div[@class='backButton']//a").click()

    def Event_Types(self):
        self.driver.implicitly_wait(20)
        time.sleep(2)
        self.driver.find_element(By.XPATH, value="//div[@class='block eventsBlock ng-scope onboardingActive']//a["
                                            "@class='addNew'][contains(text(),'+')]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, value="//input[@id='etName']").send_keys("Discussion")
        time.sleep(2)
        self.driver.find_element(By.XPATH, value="//div[@id='AddEventTypePopUp']//input[@class='btn']").click()

    def Overview(self):
        self.driver.implicitly_wait(20)
        time.sleep(10)
        self.driver.find_element(By.XPATH, value="//body//div//div//div//div//div//div//div//div//div//div//div//div"
                                                 "//div//div//div//div//div[1]//div[1]//span[2]//a[1]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, value="//label[contains(text(),'05')]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, value="// label[contains(text(), '10')]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, value="//label[contains(text(),'20')]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, value="//div[@class='ng-scope']//div[@class='ng-scope']//div["
                                                 "@class='ng-scope']//input[@class='btn']").click()
        # time.sleep(2)
        # self.driver.find_element(By.XPATH, value="//*[@id='UnsavedChangesPopUp']/div/div[3]/input[1]").click()
        time.sleep(20)

    def Scheduling_Options(self):
        self.driver.implicitly_wait(30)
        time.sleep(5)
        element = self.driver.find_element(By.XPATH, value="//a[contains(text(),'Scheduling options')]").send_keys(Keys.PAGE_UP)

        self.driver.find_element(By.XPATH, value="//a[contains(text(),'Scheduling options')]").click()
        print("INside")
        time.sleep(2)
        self.driver.find_element(By.XPATH, value="//body/form/div/div[@class='draggedPage']/div[@class='container "
                                                 "OuterContainer']/table/tbody/tr/td/table/tbody/tr/td/div["
                                                 "@class='header-gap ng-scope']/div[@class='ng-scope']/div["
                                                 "@class='ng-scope']/div[@class='ng-isolate-scope']/div/ng-form["
                                                 "@name='form']/div[@class='ng-scope']/div[@class='navafterBox "
                                                 "ng-scope']/div[@class='ng-scope']/div[@class='ng-scope']/div["
                                                 "@class='ng-scope']/div[@class='schOPtions']/div["
                                                 "@class='bottom-border-sec']/ul[@class='block-list "
                                                 "number-padding']/li[@class='BookWithApprove']/label[1]").click()

        # "//input[@name='schedulingMode' and @type='radio' and "
        #                                          "@id='schedulingModeMe']").click()
        time.sleep(2)

        self.driver.find_element(By.XPATH, value="//input[@id='soclose']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, value="//input[@type='button' and @value='Save' and "
                                                 "@ng-click='saveShedulingOptionsData()' and @class='btn' and "
                                                 "@title='Click to save']").click()
        time.sleep(10)

    def Booking_Form_And_Redirect(self):
        self.driver.implicitly_wait(20)
        time.sleep(10)
        ele12 = self.driver.find_element(By.XPATH, value="//a[contains(text(),'Booking form and redirect')]").send_keys(Keys.PAGE_UP)
        self.driver.find_element(By.XPATH, value="//a[contains(text(),'Booking form and redirect')]").click()
        # time.sleep(2)

    def Customer_Notificatio(self):
        self.driver.implicitly_wait(20)
        # time.sleep(10)
        ele4 = self.driver.find_element(By.XPATH, value="//a[contains(text(),'Customer notifications')]").send_keys(Keys.PAGE_UP)
        self.driver.find_element(By.XPATH, value="//a[contains(text(),'Customer notifications')]").click()

    def Payment_And_Reschedule_Option(self):
        self.driver.implicitly_wait(20)
        time.sleep(10)
        self.driver.find_element(By.XPATH, value="//a[contains(text(),'Payment and cancel')]").send_keys(Keys.PAGE_UP)
        self.driver.find_element(By.XPATH, value="//a[contains(text(),'Payment and cancel')]").click()

    def Public_Content(self):
        self.driver.implicitly_wait(20)
        time.sleep(10)
        self.driver.find_element(By.XPATH, value="//a[contains(text(),'Public content')]").send_keys(Keys.PAGE_UP)
        self.driver.find_element(By.XPATH, value="//a[contains(text(),'Public content')]").click()


# if __name__ == "__main__":
#     driver = Get_chrome_driver().launch_chrome()
#     obj = SOEventType(driver)
#     obj.Schedule_Once()
#     # obj.Event_Type_Triple_Dots()
#     # obj.Edit_Triple_Dots()
#     obj.Event_Types()
#     obj.Overview()
#     obj.Scheduling_Options()
#     obj.Booking_Form_And_Redirect()
#     obj.Customer_Notificatio()
#     obj.Payment_And_Reschedule_Option()
#     obj.Public_Content()
