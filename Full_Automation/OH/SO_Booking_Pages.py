from Full_Automation.Locators.SO_Booking_Page_Locators import BookingPage
from Full_Automation.Locators.SO_Event_Type_Locators import SOEventType
from Full_Automation.OH.User_Profile import Logi
from Full_Automation.OH.Webdriver_Get import Get_chrome_driver


class BookingPages:
    driver = None

    def __init__(self, driver):
        self.driver = driver

    def Call_login_functionn(self):
        Call_login4 = Logi(self.driver)
        Call_login4.URL_file()
        Call_login4.Llogin()

    def Call_SO_Enter_Function(self):
        Call_SO = SOEventType(self.driver)
        Call_SO.Schedule_Once()

    def Call_Click_On_Triple_Dot(self):
        Call_triple_dot = BookingPage(self.driver)
        Call_triple_dot.Click_On_Triple_Dot()

    def Call_BookingPage_Overview(self):
        Call_bookingpage_overview = BookingPage(self.driver)
        Call_bookingpage_overview.BookingPage_Overview()

    # def Call_Back_Button(self):
    #     Call_back_button = BookingPage(self.driver)
    #     Call_back_button.Back_BUtton_Press()


if __name__ == "__main__":
    driver = Get_chrome_driver().launch_chrome()
    obj = BookingPages(driver)
    obj.Call_login_functionn()
    obj.Call_SO_Enter_Function()
    obj.Call_Click_On_Triple_Dot()
    obj.Call_BookingPage_Overview()