from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()


class Login:
    def login(self):
        driver.implicitly_wait(5)
        driver.get("https://inbox.staticso2.com/")  # will go the Inbox url to copy the sample email id.
        driver.find_element(By.XPATH, "//*[@id='div-domain']").click()  # xpath for the email copy.

        driver.get(
            "https://inviteonce:Sob%40%23123@pythonsaccount.staticso2.com/signin?login_challenge"
            "=6884eb76891242d7a8088e331e2527ba")   # will go to the Oncehub login screen after authentication pass.
        print("Get the URL")
        driver.maximize_window()   # It will maximize the size of the window.
        print("Maximized successfully")

    def SignUp(self):
        driver.find_element(By.TAG_NAME, "a")
        time.sleep(10)
        driver.find_element(By.LINK_TEXT, "Start a free trial").click()
        print("Start a free trial button link is clicked")
        Name = driver.find_element(By.ID, value="name").send_keys("Shubh")
        time.sleep(3)
        Email = driver.find_element(By.ID, value="email").send_keys(Keys.CONTROL + "v")
        time.sleep(3)
        Password = driver.find_element(By.ID, value="password").send_keys("testing@123")
        time.sleep(3)
        Retype_Password = driver.find_element(By.ID, value="retype-password").send_keys("testing@123")
        time.sleep(3)
        Sign_Up = driver.find_element(By.ID, value="signUp").click()

    def ScheduleOnce(self):
        time.sleep(3)
        SO_Get_Started = driver.find_element(By.ID, value="so-get-started").click()
        print("Yes we enter to the SO Module")

    def Set_Availability(self):
        time.sleep(5)

        # Available_days1 = driver.find_element(By.ID, value="sunday").click()
        # status1 = driver.find_element(By.ID, value="sunday").is_selected()
        # print(status1)
        # print("The first sunday availablility is selected")

        Available_days2 = driver.find_element(By.ID, value="monday").click()
        status2 = driver.find_element(By.ID, value="monday").is_selected()
        print(status2)
        print("The second monday availablility is selected")

        Available_daysA = driver.find_element(By.ID, value="monday").click()
        statusA = driver.find_element(By.ID, value="monday").is_selected()
        print(statusA)
        print("The second monday availablility is selected")

        # Available_days3 = driver.find_element(By.ID, value="tuesday").click()
        # status3 = driver.find_element(By.ID, value="tuesday").is_selected()
        # print(status3)
        # print("The third tuesday availablility is selected")
        #
        # Available_days4 = driver.find_element(By.ID, value="thursday").click()
        # print(status3)
        # print("The 4th thursday availablility is selected")
        #
        # Available_days5 = driver.find_element(By.ID, value="saturday").click()
        # print(status3)
        # print("The 5th saturday availablility is selected")
        #
        # Avalaibility_Start = driver.find_element(By.ID, value="availability-start").click()
        # Available_select_from = driver.find_element(By.ID, value="oui-option-1").click()
        # print("The 11 time has been selected")
        # Available_select_To = driver.find_element(By.ID, value="oui-option-42").click()
        # print("The 12 time has been selected")

        time.sleep(3)
        Time_Zone_Change = driver.find_element(By.XPATH, value="//*[@id='changetz']").click()
        print("I have clicked on the Change time button")
        time.sleep(3)
        Select_Your_Country = driver.find_element(By.ID, value="selectedCountry").click()
        print("Going to select the country")
        time.sleep(3)
        Choosen_country = driver.find_element(By.XPATH, value="//*[@id='oui-option-216']/span").click()
        print("selected country")
        time.sleep(3)
        Save_Time_Zone = driver.find_element(By.ID, value="saveTimeZone").click()
        print("last")

        Continue_Button = driver.find_element(By.ID, value="continue").click()
        print("continue button has been clicked")

    def Calendar(self):
        driver.implicitly_wait(10)
        # driver.find_element(By.ID, value="GoogleCalendarConnectBtn").click()
        # print("google calendar button has been pressed")
        # driver.find_element(By.ID, value="//*[@id='identifierId']").send_keys("mailtest469@gmail.com")
        # driver.find_element(By.XPATH, value="//*[@id='identifierNext']/div/button/div[2]").click()
        driver.find_element(By.ID, value="ExchangeCalendarConnectBtn").click()
        print("Exchange calendar button has been pressed")
        outlook_email = driver.find_element(By.XPATH, value="//*[@id='email']").send_keys("amit.singh@devsunil.onmicrosoft.com")
        outlook_password = driver.find_element(By.XPATH, value="//*[@id='password']").send_keys("schEdu1e@1234")
        submit = driver.find_element(By.XPATH, value="//*[@id='oui-dialog-1']/div[3]/div[2]/button/span").click()
        time.sleep(10)
        driver.find_element(By.XPATH, "//*[@id='continue']").click()

obj = Login()
obj.login()
obj.SignUp()
obj.ScheduleOnce()
obj.Set_Availability()
obj.Calendar()
