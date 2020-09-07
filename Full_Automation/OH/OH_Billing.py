from Full_Automation.Locators.OH_Billing_Locators import BillingLocator
from Full_Automation.OH.User_Profile import Logi
from Full_Automation.OH.Webdriver_Get import Get_chrome_driver
import time


class Billing:
    driver = None

    def __init__(self, driver):
        self.driver = driver

    def login_function_cal(self):
        chk = Logi(self.driver)
        chk.URL_file()
        chk.Llogin()
        chk.My_Profile()

    def Biling_Check(self):
        billing_check = BillingLocator(self.driver)
        billing_check.Click_On_Biiling_Butn()

    def Product(self):
        product_click = BillingLocator(self.driver)
        product_click.Click_On_Product()

    def Payment_Method(self):
        payment_method_click = BillingLocator(self.driver)
        payment_method_click.Click_On_Payment_Method()

    def Notification(self):
        notification_btn_click = BillingLocator(self.driver)
        notification_btn_click.Click_On_Notification()

    def Transaction(self):
        transaction_btn_click = BillingLocator(self.driver)
        transaction_btn_click.Click_On_Transcation()


if __name__ == "__main__":
    driver = Get_chrome_driver().launch_chrome()
    abj = Billing(driver)
    abj.login_function_cal()
    abj.Biling_Check()
    abj.Product()
    abj.Payment_Method()
    abj.Notification()
    abj.Transaction()
