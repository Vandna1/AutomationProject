from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time
driver = webdriver.Chrome()

class Login:
    def login(self):

        # username = "inviteonce"
        # password = "Sob@#123"
        driver.implicitly_wait(10)
        # driver.get("https://inbox.staticso2.com/")
        # get_email = driver.find_element(By.ID, value="email-input").
        driver.get("https://inviteonce:Sob%40%23123@pythonsaccount.staticso2.com/signin?login_challenge=6884eb76891242d7a8088e331e2527ba")
        # driver.get("https://inviteonce:Sob%40%23123@pythonsaccount.staticso2.com/")
        # driver.get("http://pythonshub.staticso2.com/")
        # driver.get("https://pythonsaccount.staticso2.com/signin?login_challenge=f03ffd00db0643008c692b59e3e4d84a")
        print("Get the URL")
        driver.maximize_window()
        print("Maximized successfully")

        # alert = driver.switch_to_alert()
        # print("Alerts has been called here:")
        # alert.SetAuthenticationCredentials(username,password)
        # alert.accept()

    def SignUp(self):
        driver.find_element(By.TAG_NAME, "a")
        time.sleep(10)
        driver.find_element(By.LINK_TEXT, "Start a free trial").click()
        print("Start a free trial button link is clicked")
        Name = driver.find_element(By.ID, value="name").send_keys("Shubh")
        time.sleep(3)
        Email = driver.find_element(By.ID, value="email").send_keys("opportunity-composition-85@staticso2.com")
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
        Available_days1 = driver.find_element(By.ID, value="sunday").click()
        status1 = driver.find_element(By.ID, value="sunday").is_selected()
        print(status1)
        print("The first sunday availablility is selected")
        Available_days2 = driver.find_element(By.ID, value="monday").click()
        status2 = driver.find_element(By.ID, value="monday").is_selected()
        print(status2)
        Available_days3 = driver.find_element(By.ID, value="tuesday").click()
        status3 = driver.find_element(By.ID, value="tuesday").is_selected()
        print(status3)
        Available_days4 = driver.find_element(By.ID, value="thursday").click()
        Available_days5 = driver.find_element(By.ID, value="saturday").click()

        Avalaibility_Start = driver.find_element(By.ID, value="availability-start").click()
        Available_select_from = driver.find_element(By.ID, value="oui-option-23").click()
        Available_select_To = driver.find_element(By.ID, value="oui-option-47").click()

        Time_Zone_Change = driver.find_element(By.ID, value="changetz").click()
        Select_Your_Country = driver.find_element(By.ID, value="selectedCountry").click()
        Choosen_country = driver.find_element(By.ID, value="oui-option-417").click()
        # Select_time_Zone =
        Save_Time_Zone = driver.find_element(By.ID, value="saveTimeZone").click()
        print("last")


obj = Login()
obj.login()
obj.SignUp()
obj.ScheduleOnce()
obj.Set_Availability()
