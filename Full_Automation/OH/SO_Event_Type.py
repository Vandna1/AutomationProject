from Full_Automation.Locators.SO_Event_Type_Locators import SOEventType
from Full_Automation.OH.User_Profile import Logi
from Full_Automation.OH.Webdriver_Get import Get_chrome_driver


class EventTypes:
    driver = None

    def __init__(self, driver):
        self.driver = driver

    def Call_login_function123(self):
        Call_login1 = Logi(self.driver)
        Call_login1.URL_file()
        Call_login1.Llogin()

    def Call_Schedule_Once_Function(self):
        Call_SO = SOEventType(self.driver)
        Call_SO.Schedule_Once()

    def Call_Event_Type_Triple_Dots(self):
        Call_event_type_triple_dots = SOEventType(self.driver)
        Call_event_type_triple_dots.Event_Type_Triple_Dots()

    def Call_Edit_Triple_Dots(self):
        Call_edit_triple_dots = SOEventType(self.driver)
        Call_edit_triple_dots.Edit_Triple_Dots()

    def Call_Event_Types(self):
        Call_event_types = SOEventType(self.driver)
        Call_event_types.Event_Types()

    def Call_Overview(self):
        Call_overview = SOEventType(self.driver)
        Call_overview.Overview()

    def Call_Scheduling_Options(self):
        Call_scheduling_option = SOEventType(self.driver)
        Call_scheduling_option.Scheduling_Options()

    def Call_Booking_Form_And_Redirect(self):
        Call_booking_form = SOEventType(self.driver)
        Call_booking_form.Booking_Form_And_Redirect()

    def Call_Customer_Notificatio(self):
        Call_customer_notification = SOEventType(self.driver)
        Call_customer_notification.Payment_And_Reschedule_Option()

    def Call_Public_Content(self):
        Call_public_content = SOEventType(self.driver)
        Call_public_content.Public_Content()


if __name__ == "__main__":
    driver = Get_chrome_driver().launch_chrome()
    obj = EventTypes(driver)
    obj.Call_login_function123()
    obj.Call_Schedule_Once_Function()
    obj.Call_Event_Type_Triple_Dots()
    obj.Call_Edit_Triple_Dots()
    obj.Call_Event_Types()
    obj.Call_Overview()
    obj.Call_Scheduling_Options()
    obj.Call_Booking_Form_And_Redirect()
    obj.Call_Customer_Notificatio()
    obj.Call_Public_Content()
