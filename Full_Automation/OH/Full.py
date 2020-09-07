from Full_Automation.OH.OH_Privacy import Privacy
from Full_Automation.OH.SO_Booking_Pages import BookingPages
from Full_Automation.OH.SO_Event_Type import EventTypes
from Full_Automation.OH.SignUp import Signup
from Full_Automation.OH.User_Profile import Logi
from Full_Automation.OH.Webdriver_Get import Get_chrome_driver
from Full_Automation.OH.OH_Billing import Billing
from Full_Automation.OH.OH_Security import Security


class CompleteAutomation:
    driver = None

    def __init__(self, driver):
        self.driver = driver

    def Call_SignUp_Module(self):
        calling_SignUp = Signup(driver)
        calling_SignUp.Get_Url_Inbox()
        calling_SignUp.Get_URL_Server()
        calling_SignUp.SignUpp()
        calling_SignUp.ScheduleOnce()
        calling_SignUp.Set_Availability()
        calling_SignUp.Calendar()
        calling_SignUp.logout()

    def Call_Login_Functionality_first(self):
        calling_Login = Logi(driver)
        calling_Login.URL_file()
        calling_Login.Llogin()
        calling_Login.My_Profile()
        calling_Login.Edit_profile()
        calling_Login.Calendar_Connection()
        calling_Login.Email_Notfication()
        calling_Login.SMS_Notification()
        calling_Login.Date_And_Time()
        calling_Login.Password()
        calling_Login.Authentication()
        calling_Login.ScheduleOnce()
    #
    def Call_Biiling_Functionality(self):
        calling_Billing = Billing(driver)
        # calling_Billing.login_function_cal()
        calling_Billing.Biling_Check()
        calling_Billing.Product()
        calling_Billing.Payment_Method()
        calling_Billing.Notification()
        calling_Billing.Transaction()

    def Call_Security_Functionality(self):
        calling_Security = Security(driver)
        # calling_Security.Call_login_function5()
        calling_Security.Security_Check()
        calling_Security.SSO()
        calling_Security.Password_Policy()
        calling_Security.Account_Lookout_Policies()
        # calling_Security.Session_Policies()

    def Call_Privacy_Functionality(self):
        calling_Privacy = Privacy(driver)
        # calling_Privacy.Call_login_function2()
        calling_Privacy.Privacy_Check()
        calling_Privacy.Privacy_Shield()
        calling_Privacy.GDPR_Info()
        calling_Privacy.GDPR_Compliance()

    def Call_So_Event_Types(self):
        Calling_EventTypes = EventTypes(driver)
        # Calling_EventTypes.Call_login_function123()
        Calling_EventTypes.Call_Schedule_Once_Function()
        Calling_EventTypes.Call_Event_Type_Triple_Dots()
        Calling_EventTypes.Call_Edit_Triple_Dots()
        Calling_EventTypes.Call_Event_Types()
        Calling_EventTypes.Call_Overview()
        Calling_EventTypes.Call_Scheduling_Options()
        Calling_EventTypes.Call_Booking_Form_And_Redirect()
        Calling_EventTypes.Call_Customer_Notificatio()
        Calling_EventTypes.Call_Public_Content()

    def Call_SO_Booking_Pages(self):
        Calling_BookingPages = BookingPages(driver)
        Calling_BookingPages.Call_login_functionn()
        Calling_BookingPages.Call_SO_Enter_Function()
        Calling_BookingPages.Call_Click_On_Triple_Dot()
        Calling_BookingPages.Call_BookingPage_Overview()
        # Calling_BookingPages.Call_Back_Button()


if __name__ == "__main__":
    driver = Get_chrome_driver().launch_chrome()
    obj = CompleteAutomation(driver)
    obj.Call_SignUp_Module()
    obj.Call_Login_Functionality_first()
    obj.Call_Biiling_Functionality()
    obj.Call_Security_Functionality()
    obj.Call_Privacy_Functionality()
    obj.Call_So_Event_Types()
    obj.Call_SO_Booking_Pages()
