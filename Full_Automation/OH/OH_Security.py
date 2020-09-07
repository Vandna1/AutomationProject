from Full_Automation.Locators.OH_Security_Locators import SecurityLocator
from Full_Automation.OH.User_Profile import Logi
from Full_Automation.OH.Webdriver_Get import Get_chrome_driver


class Security:
    driver = None

    def __init__(self, driver):
        self.driver = driver

    def Call_login_function5(self):
        Call_login = Logi(self.driver)
        Call_login.URL_file()
        Call_login.Llogin()
        Call_login.My_Profile()

    def Security_Check(self):
        security_btn_click = SecurityLocator(self.driver)
        security_btn_click.Click_On_Security_btn()

    def SSO(self):
        sso_click = SecurityLocator(self.driver)
        sso_click.Click_On_SSO()

    def Password_Policy(self):
        password_policy_click = SecurityLocator(self.driver)
        password_policy_click.Click_On_Password_Policy()

    def Account_Lookout_Policies(self):
        account_lookout_policy = SecurityLocator(self.driver)
        account_lookout_policy.Click_On_Account_Lookout_Policy()

    # def Session_Policies(self):
    #     session_policy_click = SecurityLocator(self.driver)
    #     session_policy_click.Click_On_Session_Policy()


if __name__ == "__main__":
    driver = Get_chrome_driver().launch_chrome()
    obj = Security(driver)
    obj.Call_login_function5()
    obj.Security_Check()
    obj.SSO()
    obj.Password_Policy()
    obj.Account_Lookout_Policies()
    # obj.Session_Policies()

