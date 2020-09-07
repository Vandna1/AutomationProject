from Full_Automation.Locators.OH_User_Profile_Locators import UserProfileLocator
from Full_Automation.OH.Webdriver_Get import Get_chrome_driver


class Logi:
    driver = None

    def __init__(self, driver):
        self.driver = driver

    def URL_file(self):
        get_url = UserProfileLocator(self.driver)
        get_url.Call_URL()

    def Llogin(self):
        logn = UserProfileLocator(self.driver)
        logn.Call_Login()

    def My_Profile(self):
        my_profile = UserProfileLocator(self.driver)
        my_profile.Goto_My_Profile()

    def Edit_profile(self):
        edit_profile = UserProfileLocator(self.driver)
        edit_profile.Goto_Edit_Profile()

    def Calendar_Connection(self):
        calendar_connection = UserProfileLocator(self.driver)
        calendar_connection.Goto_Calendar_Connection()

    def Email_Notfication(self):
        email_notification = UserProfileLocator(self.driver)
        email_notification.Goto_Email_notification()

    def SMS_Notification(self):
        sms_notification = UserProfileLocator(self.driver)
        sms_notification.Goto_SMS_Notification()

    def Date_And_Time(self):
        date_and_time = UserProfileLocator(self.driver)
        date_and_time.Goto_Date_And_Time()

    def Password(self):

        password = UserProfileLocator(self.driver)
        password.Goto_Password()

    def Authentication(self):
        authentication = UserProfileLocator(self.driver)
        authentication.Goto_Authentication()

    def ScheduleOnce(self):
        scheduleonce = UserProfileLocator(self.driver)
        scheduleonce.Goto_ScheduleOnce()


if __name__ == "__main__":
    driver = Get_chrome_driver().launch_chrome()
    obj = Logi(driver)
    obj.URL_file()
    obj.Llogin()
    obj.My_Profile()
    obj.Edit_profile()
    obj.Calendar_Connection()
    obj.Email_Notfication()
    obj.SMS_Notification()
    obj.Date_And_Time()
    obj.Password()
    obj.Authentication()
    obj.ScheduleOnce()
