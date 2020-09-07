from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
driver.get("http://app3.onceplatform.com/")

################# Sign_Up########################

driver.implicitly_wait(5)
driver.get("https://inbox.staticso2.com/")  # will go the Inbox url to copy the sample email id.
driver.find_element(By.XPATH, "//*[@id='div-domain']").click()  # xpath for the email copy.

# driver.get(
#     "https://inviteonce:Sob%40%23123@pythonsaccount.staticso2.com/signin?login_challenge"
#     "=6884eb76891242d7a8088e331e2527ba")   # will go to the Oncehub login screen after authentication pass.

# driver.get(
#     "http://app2.onceplatform.com/"
# )
driver.get("http://app3.onceplatform.com/")
print("Get the URL")
driver.maximize_window()  # It will maximize the size of the window.
print("Maximized successfully")

"""
This function will create a new user successfully.
"""
driver.find_element(By.TAG_NAME, "a")
time.sleep(10)
driver.find_element(By.LINK_TEXT, "Start a free trial").click()
print("Start a free trial button link is clicked")
Name = driver.find_element(By.ID, value="name").send_keys("Shubh")
time.sleep(3)
Email = driver.find_element(By.ID, value="email").send_keys(Keys.CONTROL + "v")
print(Email)
time.sleep(3)
Password = driver.find_element(By.ID, value="password").send_keys("testing@123")
time.sleep(3)
Retype_Password = driver.find_element(By.ID, value="retype-password").send_keys("testing@123")
time.sleep(3)
Sign_Up = driver.find_element(By.ID, value="signUp").click()

# driver.get("https://inbox.staticso2.com/")
# time.sleep(3)
# Enter_Pin = driver.find_element(By.XPATH, value="//input[@id='email-input']").clear()
# time.sleep(3)
#
# driver.find_element(By.XPATH, value="//input[@id='email-input']").send_keys(Keys.CONTROL + "v")
# driver.find_element(By.XPATH, value="//input[@id='email-input']").send_keys(Keys.CONTROL + "c")
#
#
# time.sleep(3)
# get_email = driver.find_element(By.XPATH, value="//div[@id='div-domain']").click()

"""
This funciton will go to the Schedule Once Module.
"""
time.sleep(3)
SO_Get_Started = driver.find_element(By.ID, value="so-get-started").click()
print("Yes we enter to the SO Module")

"""
In this function the avalability will be selected from the avalability Section.
"""
time.sleep(5)

Available_days2 = driver.find_element(By.ID, value="monday").click()
status2 = driver.find_element(By.ID, value="monday").is_selected()
print(status2)
print("The second monday availablility is deselected")

Available_daysA = driver.find_element(By.ID, value="monday").click()
statusA = driver.find_element(By.ID, value="monday").is_selected()
print(statusA)
print("The second monday availablility is selected")

Available_days3 = driver.find_element(By.ID, value="tuesday").click()  # first deselect
status3 = driver.find_element(By.ID, value="tuesday").is_selected()
print(status3)
print("The third tuesday availablility is deselected")

Available_daysB = driver.find_element(By.ID, value="tuesday").click()  # Now select
statusB = driver.find_element(By.ID, value="tuesday").is_selected()
print(statusB)
print("The third tuesday availablility is selected")
#
Available_days4 = driver.find_element(By.ID, value="thursday").click()
# print(status3)
print("The 4th thursday availablility is deselected")

Available_daysC = driver.find_element(By.ID, value="thursday").click()
# print(status)
print("The 4th thursday availablility is selected")

Available_days1 = driver.find_element(By.ID, value="sunday").click()
status1 = driver.find_element(By.ID, value="sunday").is_selected()
print(status1)
print("The first sunday availablility is selected")
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

"""
This function will help to connect to the Exchange Calendar successfully. and then will continue the
process and skip the all other option till the OH module. In OH module it will go to the Profile and
then will do the logout activity.
"""
driver.implicitly_wait(10)
# google calendar
# driver.find_element(By.ID, value="GoogleCalendarConnectBtn").click()
# print("google calendar button has been pressed")
# driver.find_element(By.ID, value="//*[@id='identifierId']").send_keys("mailtest469@gmail.com")
# driver.find_element(By.XPATH, value="//*[@id='identifierNext']/div/button/div[2]").click()

driver.find_element(By.ID, value="ExchangeCalendarConnectBtn").click()
time.sleep(3)
print("Exchange calendar button has been pressed")
outlook_email = driver.find_element(By.XPATH, value="//*[@id='email']").send_keys("amit.singh@devsunil.onmicrosoft.com")
time.sleep(3)
outlook_password = driver.find_element(By.XPATH, value="//*[@id='password']").send_keys("schEdu1e@1234")
time.sleep(3)
outlook_credentials_submit = driver.find_element(By.XPATH,
                                                 value="//*[@id='oui-dialog-1']/div[3]/div[2]/button/span").click()
time.sleep(10)
driver.find_element(By.XPATH, "//*[@id='continue']").click()
time.sleep(10)
driver.find_element(By.XPATH, value="//a[@id='setUpLater']").click()
time.sleep(10)
driver.find_element(By.XPATH, value="//span[contains(text(),'Skip')]").click()
time.sleep(5)
driver.find_element(By.XPATH, value="//*[@id='OrientationTour2']/div[4]/a[1]").click()
time.sleep(3)
driver.find_element(By.XPATH, value="//a[@id='rAccountIcon']").click()
time.sleep(3)
driver.find_element(By.XPATH, value="//span[contains(text(),'Sign out')]").click()

##################### login  #####################################

driver.implicitly_wait(15)
driver.get(
    "http://app3.onceplatform.com/")  # will go to the Oncehub login screen after authentication pass.
print("Get the URL")
driver.maximize_window()  # It will maximize the size of the window.
print("Maximized successfully")
driver.find_element(By.XPATH, value="//input[@id='email']").send_keys("cow-further-65@staticso2.com")
time.sleep(5)
driver.find_element(By.XPATH, value="//input[@id='password']").send_keys("testing@123")
time.sleep(5)
driver.find_element(By.XPATH, value="//button[@id='signIn']").click()
print("signin button has been pressed")
time.sleep(5)

driver.implicitly_wait(40)
Goto_My_Profile = driver.find_element(By.ID, value="rAccountIcon").click()
time.sleep(3)
Click_My_Profile = driver.find_element(By.XPATH, value="//span[contains(text(),'My profile')]").click()
time.sleep(2)
Users = driver.find_element(By.XPATH, value="//span[contains(text(),'Users')]").click()
time.sleep(2)
Click_On_user = driver.find_element(By.XPATH, value="//div[@class='usersName']").click()
time.sleep(2)
Edit_Last_Name = driver.find_element(By.XPATH,
                                     value="//div[@class='list-data']//button[@class='oui-icon-button "
                                           "oui-primary']//oui-icon[@class='oui-icon']").click()
time.sleep(2)

Enter_Last_Name = driver.find_element(By.ID, value="lastNameTxt3").clear()
Enter_Last_Namee = driver.find_element(By.ID, value="lastNameTxt3").send_keys("Thakurrrrrrrrr")
time.sleep(5)
Save_Last_Name = driver.find_element(By.XPATH, value="//span[contains(text(),'Save')]").click()



#################Calendar Connection###############

driver.implicitly_wait(30)
time.sleep(10)
Goto_Calendar_Connection = driver.find_element(By.XPATH,
                                               value="//span[contains(text(),'Calendar connection')]").click()
Disconnect_Calendar = driver.find_element(By.XPATH, value="//a[@id='disconnectAnchor']").click()
time.sleep(5)
print("yes")
Will_Connect_later = driver.find_element(By.XPATH, value="//*[@id='connectToSameCalendar']").click()
time.sleep(2)
print("Yoo")
Disconnect_Anyway = driver.find_element(By.XPATH, value="//span[contains(text(),'Disconnect anyway')]").click()

time.sleep(5)
Exchange_Calendar = driver.find_element(By.XPATH, value="//button[@id='ExchangeCalendarConnectBtn']//span["
                                                        "@class='oui-button-wrapper'][contains(text(),"
                                                        "'Connect')]").click()
print("Exchange calendar button has been pressed")
outlook_email = driver.find_element(By.XPATH, value="//*[@id='email']").send_keys("amit.singh@devsunil.onmicrosoft.com")
time.sleep(5)
outlook_password = driver.find_element(By.XPATH, value="//*[@id='password']").send_keys("schEdu1e@1234")
time.sleep(5)
outlook_credentials_submit = driver.find_element(By.XPATH,
                                                 value="//*[@id='oui-dialog-1']/div[3]/div[2]/button/span").click()
time.sleep(5)
default_office_reminder = driver.find_element(By.XPATH, value="//oui-select[@placeholder='Duration']//div["
                                                              "@class='oui-select-value']").click()
time.sleep(3)
Selected_real_path = driver.find_element(By.XPATH, value="//span[contains(text(),'30 minutes')]").click()
print("working till here")

##################### Email Notification #################

driver.implicitly_wait(30)
time.sleep(10)
Goto_Email_Notification = driver.find_element(By.XPATH,
                                              value="//span[contains(text(),'Email notifications')]").click()
time.sleep(3)
email_sent_from = driver.find_element(By.XPATH, value="//div[@class='form-inline']//input["
                                                      "@class='oui-input-element oui-input oui-primary "
                                                      "cdk-text-field-autofill-monitored ng-untouched "
                                                      "ng-pristine ng-valid']").send_keys("vanii")
time.sleep(3)
Discard_Changes = driver.find_element(By.XPATH, value="//span[contains(text(),'Discard')]").click()
time.sleep(3)


################## SMS Notification ######################

driver.implicitly_wait(30)
SMS_Notification = driver.find_element(By.XPATH, value="//span[contains(text(),'SMS notifications')]").click()
time.sleep(3)
SMS_Notification_Activate = driver.find_element(By.XPATH, value="//span[@class='oui-slider round']").click()
time.sleep(3)
Discard_Change = driver.find_element(By.XPATH, value="//span[contains(text(),'Discard')]").click()
time.sleep(3)


##################### Date and Time #################

driver.implicitly_wait(30)
time.sleep(10)
Date_And_Time = driver.find_element(By.XPATH, value="//span[contains(text(),'Date and time')]").click()
print("Click on DAte and Time")
time.sleep(3)
Select_Country = driver.find_element(By.XPATH, value="//label[contains(text(), 'Default time "
                                                     "zone')]//following-sibling::div[@class='form-control "
                                                     "ng-star-inserted']")
time.sleep(3)
# selected_country = driver.find_element(By.XPATH, value="//*[@id='oui-option-10203']/span").click()
# time.sleep(3)
Save_It = driver.find_element(By.XPATH, value="//span[contains(text(),'Save')]").click()
time.sleep(3)

################# Password #####################

driver.implicitly_wait(30)
Password_Click = driver.find_element(By.XPATH, value="//li[@class='sl-sidenav-link ng-star-inserted']//span["
                                                     "@class='sl-sidenav-link-text'][contains(text(),"
                                                     "'Password')]").click()
time.sleep(3)
Current_Password_Txt_Field = driver.find_element(By.XPATH, value="//input[@id='current-password']").send_keys(
    "testing@123")
time.sleep(2)
New_pass_txt_field = driver.find_element(By.XPATH, value="//input[@id='new-password']").send_keys("test@123")
time.sleep(2)
Confirm_Pass_txt_field = driver.find_element(By.XPATH, value="//input[@id='re-type-password']").send_keys("test@123")
time.sleep(2)
Discard = driver.find_element(By.XPATH, value="//span[contains(text(),'Discard')]").click()

############## Authentication #####################

driver.implicitly_wait(30)
time.sleep(5)
Authentication_Button_Click = driver.find_element(By.XPATH, value="//span[contains(text(),'Authentication')]").click()
time.sleep(2)
Enable_Two_way_Authentication = driver.find_element(By.XPATH, value="//span[@class='oui-slider round']").click()
time.sleep(2)
Enter_Current_Password_Authentication = driver.find_element(By.XPATH,
                                                            value="//input[@id='current-password']").send_keys(
    "testing@123")
time.sleep(2)
Submit = driver.find_element(By.XPATH, value="//span[contains(text(),'Submit')]").click()
time.sleep(2)
Enter_Mobile_Number = driver.find_element(By.XPATH, value="//input[@placeholder='Include area code or any "
                                                          "other prefix']").send_keys("8628077343")
Now_Discard = driver.find_element(By.XPATH, value="//span[contains(text(),'Discard')]").click()

################## ScheduleOnce #########################3

driver.implicitly_wait(30)
time.sleep(5)
Click_Schedule_Once = driver.find_element(By.XPATH, value="//span[contains(text(),'ScheduleOnce')]").click()
time.sleep(2)
Payment_Integration_Select = driver.find_element(By.XPATH, value="//oui-checkbox[@id='pay-setup']//div["
                                                                 "@class='oui-checkbox-background']//*["
                                                                 "local-name()='svg']").click()
time.sleep(2)
Discardd = driver.find_element(By.XPATH, value="//span[contains(text(),'Discard')]").click()

################### OH Billing ##################3

driver.find_element(By.XPATH, value="//span[contains(text(),'Billing')]").click()

############## OH Billing - Product ###########

driver.find_element(By.XPATH, value="//span[contains(text(),'Products')]").click()
driver.find_element(By.XPATH, value="//span[contains(text(),'Purchase now')]").click()

