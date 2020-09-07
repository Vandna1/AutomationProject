from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from Full_Automation.Locators.OH_Privacy_Locators import PrivacyLocator
from Full_Automation.OH.User_Profile import Logi
from Full_Automation.OH.Webdriver_Get import Get_chrome_driver
import time


class Privacy:
    driver = None

    def __init__(self, driver):
        self.driver = driver

    def Call_login_function2(self):
        Call_login12 = Logi(self.driver)
        Call_login12.URL_file()
        Call_login12.Llogin()
        Call_login12.My_Profile()

    def Privacy_Check(self):
        privacy_click = PrivacyLocator(self.driver)
        privacy_click.Click_On_Privacy_Module()

    def Privacy_Shield(self):
        privacy_shield = PrivacyLocator(self.driver)
        privacy_shield.Click_On_Privacy_Shield()

    def GDPR_Info(self):
        gdpr_info = PrivacyLocator(self.driver)
        gdpr_info.Click_On_GDPR_Info()

    def GDPR_Compliance(self):
        gdpr_compliance = PrivacyLocator(self.driver)
        gdpr_compliance.Click_On_GDPR_Compliance()


if __name__ == "__main__":
    driver = Get_chrome_driver().launch_chrome()
    obj = Privacy(driver)
    obj.Call_login_function2()
    obj.Privacy_Check()
    obj.Privacy_Shield()
    obj.GDPR_Info()
    obj.GDPR_Compliance()
