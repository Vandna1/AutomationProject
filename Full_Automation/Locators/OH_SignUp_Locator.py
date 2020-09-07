import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class SignUpLocator:
    def __init__(self, driver):
        self.driver = driver

    def Call_Get_URL_Inbox(self):
        self.driver.implicitly_wait(5)
        self.driver.get("https://inbox.staticso2.com/")  # will go the Inbox url to copy the sample email id.
        self.driver.find_element(By.XPATH, "//*[@id='div-domain']").click()
        # self.driver.get(
        #     "https://inviteonce:Sob%40%23123@pythonsaccount.staticso2.com/signin?login_challenge"
        #     "=6884eb76891242d7a8088e331e2527ba")   # will go to the Oncehub login screen after authentication pass.

        # self.driver.get(
        #     "http://app2.onceplatform.com/"
        # )
    def Call_Get_URL_Server(self):
        self.driver.implicitly_wait(5)
        time.sleep(5)
        self.driver.get("http://app3.onceplatform.com/")
        print("Get the URL")
        self.driver.maximize_window()   # It will maximize the size of the window.
        print("Maximized successfully")

    def Call_SignUp_function(self):
        self.driver.find_element(By.TAG_NAME, "a")
        time.sleep(10)
        self.driver.find_element(By.LINK_TEXT, "Start a free trial").click()
        print("Start a free trial button link is clicked")
        self.driver.find_element(By.ID, value="name").send_keys("Vanu Thakur")
        time.sleep(3)
        self.driver.find_element(By.ID, value="email").send_keys(Keys.CONTROL + "v")
        time.sleep(3)
        self.driver.find_element(By.ID, value="password").send_keys("testing@123")
        time.sleep(3)
        self.driver.find_element(By.ID, value="retype-password").send_keys("testing@123")
        time.sleep(3)
        self.driver.find_element(By.ID, value="signUp").click()

    def call_SO_Get_Started(self):
        self.driver.implicitly_wait(5)
        time.sleep(5)
        self.driver.find_element(By.ID, value="so-get-started").click()
        print("Yes we enter to the SO Module")

    def Call_Set_Availability(self):
        self.driver.implicitly_wait(10)
        time.sleep(5)
        self.driver.find_element(By.ID, value="monday").click()
        self.driver.find_element(By.ID, value="monday").is_selected()
        print("The second monday availablility is deselected")

        self.driver.find_element(By.ID, value="monday").click()
        self.driver.find_element(By.ID, value="monday").is_selected()
        print("The second monday availablility is selected")

        self.driver.find_element(By.ID, value="tuesday").click()  # first deselect
        self.driver.find_element(By.ID, value="tuesday").is_selected()
        print("The third tuesday availablility is deselected")
        self.driver.find_element(By.ID, value="tuesday").click()  # Now select
        self.driver.find_element(By.ID, value="tuesday").is_selected()
        print("The third tuesday availablility is selected")
        self.driver.find_element(By.ID, value="thursday").click()
        print("The 4th thursday availablility is deselected")
        self.driver.find_element(By.ID, value="thursday").click()
        print("The 4th thursday availablility is selected")
        self.driver.find_element(By.ID, value="sunday").click()
        self.driver.find_element(By.ID, value="sunday").is_selected()
        print("The first sunday availablility is selected")
        # self.driver.find_element(By.ID, value="saturday").click()
        # print("The 5th saturday availablility is selected")
        #
        # self.driver.find_element(By.ID, value="availability-start").click()
        # self.driver.find_element(By.ID, value="oui-option-1").click()
        # print("The 11 time has been selected")
        # self.driver.find_element(By.ID, value="oui-option-42").click()
        # print("The 12 time has been selected")

        time.sleep(3)
        self.driver.find_element(By.XPATH, value="//*[@id='changetz']").click()
        print("I have clicked on the Change time button")
        time.sleep(3)
        self.driver.find_element(By.ID, value="selectedCountry").click()
        print("Going to select the country")
        time.sleep(3)
        self.driver.find_element(By.XPATH, value="//*[@id='oui-option-216']/span").click()
        print("selected country")
        time.sleep(3)
        self.driver.find_element(By.ID, value="saveTimeZone").click()
        print("last")

        self.driver.find_element(By.ID, value="continue").click()
        print("continue button has been clicked")

    def Call_Calendar_Connect(self):
        self.driver.implicitly_wait(20)
        time.sleep(10)
        # google calendar
        # driver.find_element(By.ID, value="GoogleCalendarConnectBtn").click()
        # print("google calendar button has been pressed")
        # driver.find_element(By.ID, value="//*[@id='identifierId']").send_keys("mailtest469@gmail.com")
        # driver.find_element(By.XPATH, value="//*[@id='identifierNext']/div/button/div[2]").click()
        self.driver.find_element(By.XPATH, value="//*[@id='MainDataDiv']/div/div/oh-onboarding/div/oh-onboarding"
                                                 "-calendar-connection/oh-calendar-connection/div/div/div/button").click()
        time.sleep(3)
        self.driver.find_element(By.ID, value="ExchangeCalendarConnectBtn").click()
        time.sleep(3)
        print("Exchange calendar button has been pressed")
        self.driver.find_element(By.XPATH, value="//*[@id='email']").send_keys("amit.singh@devsunil.onmicrosoft.com")
        time.sleep(3)
        self.driver.find_element(By.XPATH, value="//*[@id='password']").send_keys("schEdu1e@1234")
        time.sleep(3)
        self.driver.find_element(By.XPATH, value="//*[@id='oui-dialog-1']/div[3]/div[2]/button/span").click()
        time.sleep(10)
        self.driver.find_element(By.XPATH, "//*[@id='continue']").click()
        time.sleep(10)
        self.driver.find_element(By.XPATH, value="//a[@id='setUpLater']").click()
        time.sleep(10)
        self.driver.find_element(By.XPATH, value="//span[contains(text(),'Skip')]").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, value="//*[@id='OrientationTour2']/div[4]/a[1]").click()
        time.sleep(3)

    def Logout(self):
        self.driver.find_element(By.XPATH, value="//a[@id='rAccountIcon']").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, value="//span[contains(text(),'Sign out')]").click()

