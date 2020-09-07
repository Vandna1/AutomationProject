from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from Full_Automation.OH.User_Profile import Logi
from Full_Automation.OH.Webdriver_Get import Get_chrome_driver


class COBots:
    driver = None

    def __init__(self, driver):
        self.driver = driver

    def login_function_Make_Call(self):
        Call_log = Logi(self.driver)
        Call_log.URL_file()
        Call_log.Llogin()

    def Click_On_Chat_Once_Option(self):
        self.driver.implicitly_wait(20)
        time.sleep(5)
        self.driver.find_element(By.XPATH, value="//span[@class='product-link']").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, value="//a[contains(text(),'ChatOnce setup')]").click()

    def Create_Bot(self):
        self.driver.implicitly_wait(20)
        time.sleep(5)
        self.driver.find_element(By.XPATH, value="//span[contains(text(),'Create bot')]").click()

    def Create_Bot_Template_From_Scratch(self):
        self.driver.implicitly_wait(20)
        time.sleep(5)
        self.driver.find_element(By.XPATH, value="//a[@id='createBotFromScratch']//span[@class='oui-button-wrapper']["
                                                 "contains(text(),'Create')]").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, value="//input[@id='botNameTxt']").send_keys("ChattingBot")
        time.sleep(3)
        self.driver.find_element(By.XPATH, value="//button[@class='oui-button oui-primary']//span["
                                                 "@class='oui-button-wrapper'][contains(text(),'Create')]").click()

    def Add_Interaction(self):
        self.driver.implicitly_wait(20)
        time.sleep(3)
        self.driver.find_element(By.XPATH, value="//strong[contains(text(),'Single select')]").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, value="//input[@id='interactionName']").send_keys("Lets have a discussion")
        time.sleep(3)
        self.driver.find_element(By.XPATH, value="//textarea[@id='interactionText']").send_keys("Hello, how are you?")

        time.sleep(3)
        # self.driver.find_element(By.XPATH, value="//div[@class='right-conversation ng-untouched ng-pristine "
        #                                          "ng-invalid']//input[@placeholder='Type answer option "
        #                                          "here']").send_keys(Keys.PAGE_DOWN)
        print("yo")
        self.driver.find_element(By.XPATH, value="//div[@class='right-conversation ng-untouched ng-pristine "
                                                 "ng-invalid']//input[@placeholder='Type answer option "
                                                 "here']").send_keys("lWell how to schedule meeting")
        print("No")
        time.sleep(3)
        # self.driver.find_element(By.XPATH, value="//li[1]//div[1]//div[2]//div[1]//div[2]//a[1]").click()
        # time.sleep(3)
        # self.driver.find_element(By.XPATH, value="//div[@class='right-conversation ng-pristine ng-invalid "
        #                                          "ng-touched']//input[@placeholder='Type bot response "
        #                                          "here']").send_keys("yYes we can schedule it")
        time.sleep(3)
        self.driver.find_element(By.XPATH, value="//textarea[@id='interactionBotResponse']").send_keys("Noppps")
        time.sleep(3)
        self.driver.find_element(By.XPATH, value="//span[contains(text(),'Save')]").click()
        time.sleep(3)

    def Click_On_messages(self):
        self.driver.implicitly_wait(20)
        time.sleep(3)
        self.driver.find_element(By.XPATH, value="//button[@class='back_btn capitalize oui-icon-button "
                                                 "oui-primary']//oui-icon[@class='oui-icon']").click()
        self.driver.find_element(By.XPATH, value="//li[contains(text(),'Messages')]").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, value="//strong[contains(text(),'Text message')]").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, value="//input[@id='interactionName']").send_keys("Hey pro")
        time.sleep(3)
        self.driver.find_element(By.XPATH, value="//textarea[@id='interactionText']").send_keys("i am here")
        time.sleep(3)
        self.driver.find_element(By.XPATH, value="//span[contains(text(),'Save')]").click()

    def Preview(self):
        self.driver.implicitly_wait(20)
        time.sleep(3)
        self.driver.switch_to_frame()
        self.driver.find_element(By.XPATH, value="//span[contains(text(),'Preview')]").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, value="//div[@id='message-scroll-container']/div/div/ul/li/ul/li").click()


if __name__ == "__main__":
    driver = Get_chrome_driver().launch_chrome()
    obj = COBots(driver)
    obj.login_function_Make_Call()
    obj.Click_On_Chat_Once_Option()
    obj.Create_Bot()
    obj.Create_Bot_Template_From_Scratch()
    obj.Add_Interaction()
    obj.Click_On_messages()
    obj.Preview()