from selenium import webdriver
from Full_Automation.Locators.OH_SignUp_Locator import SignUpLocator
from Full_Automation.OH.Webdriver_Get import Get_chrome_driver


class Signup:

    def __init__(self, driver):
        self.driver = driver

    def Get_Url_Inbox(self):
        """
        This function will Copy the sample email from Inbox.staticso2.com and then go to the
        Team server site after completing the authentication process sucessfully.
        """
        get_url_from_inbox = SignUpLocator(self.driver)
        get_url_from_inbox.Call_Get_URL_Inbox()

    def Get_URL_Server(self):
        get_url_server = SignUpLocator(self.driver)
        get_url_server.Call_Get_URL_Server()

    def SignUpp(self):

        """
        This function will create a new user successfully.
        """
        signup = SignUpLocator(self.driver)
        signup.Call_SignUp_function()

    def ScheduleOnce(self):

        """
        This funciton will go to the Schedule Once Module.
        """
        Get_started_SO = SignUpLocator(self.driver)
        Get_started_SO.call_SO_Get_Started()

    def Set_Availability(self):
        """
        In this function the avalability will be selected from the avalability Section.
        """
        set_availability = SignUpLocator(self.driver)
        set_availability.Call_Set_Availability()

    def Calendar(self):
        """
        This function will help to connect to the Exchange Calendar successfully. and then will continue the
        process and skip the all other option till the OH module. In OH module it will go to the Profile and
        then will do the logout activity.
        """
        connect_calendar = SignUpLocator(self.driver)
        connect_calendar.Call_Calendar_Connect()

    def logout(self):
        llogout = SignUpLocator(self.driver)
        llogout.Logout()


if __name__ == "__main__":
    driver = Get_chrome_driver().launch_chrome()
    obj = Signup(driver)
    obj.Get_Url_Inbox()
    obj.Get_URL_Server()
    obj.SignUpp()
    obj.ScheduleOnce()
    obj.Set_Availability()
    obj.Calendar()
    obj.logout()
