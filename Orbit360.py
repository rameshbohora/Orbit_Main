from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set the URL you want to open
APP_URL = "https://dashboard.orbit360.cx/"

email = input("Enter your email: ")
password = input("Enter your password: ")

# Create a Chrome WebDriver instance
driver = webdriver.Chrome()
driver.maximize_window()

try:
    # Open the URL in the browser
    driver.get(APP_URL)

    # Use WebDriverWait to wait for the username field to be present
    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "email"))
    )

    # Locate the password input field
    password_field = driver.find_element(By.ID, "password")

    # Input username and password
    username_field.send_keys(email)
    password_field.send_keys(password)

    # Locate the sign-in button and click it
    signin_button = driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[4]/button')
    signin_button.click()
    time.sleep(5)

    driver.find_element(By.XPATH,"/html/body/div[3]/div[2]/div[1]/div[2]/div[1]/a/img").click() # i icon
    time.sleep(3)

    # Find and click each introjs button with a 3-second wait after each click
    driver.find_element(By.XPATH, '/html/body/div[8]/div/div[5]/a[3]').click()
    time.sleep(3)

    driver.find_element(By.XPATH, '/html/body/div[8]/div/div[5]/a[3]').click()
    time.sleep(3)

    driver.find_element(By.XPATH, '/html/body/div[8]/div/div[5]/a[3]').click()
    time.sleep(3)

    driver.find_element(By.XPATH, '/html/body/div[8]/div/div[5]/a[3]').click()
    time.sleep(3)

    driver.find_element(By.XPATH, '/html/body/div[8]/div/div[5]/a[1]').click()
    time.sleep(3)

    driver.find_element(By.XPATH,'/html/body/div[3]/div[2]/div[2]/div/div/div[3]/div/div[4]/a').click() # Numbers(Buy Now Button)
    time.sleep(3)

    driver.find_element(By.XPATH,'//html/body/div[3]/div[1]/div/a[1]/span').click() # Get Started dashboard Menu
    time.sleep(3)

    driver.find_element(By.XPATH, '//*[@id="container"]/div/div/div[4]/div/div[4]/a').click() # Livechat(Get Started button)
    time.sleep(3)
     
    driver.find_element(By.XPATH,'/html/body/div[3]/div[1]/div/a[1]/span').click() # Get Started(dashboard menu)
    time.sleep(3)

    driver.find_element(By.XPATH,"/html/body/div[3]/div[2]/div[2]/div/div/div[5]/div/div[4]/a[1]").click() # Channels(Get Connected button)
    time.sleep(3)



    driver.find_element(By.XPATH,"/html/body/div[3]/div[1]/div/a[2]/span").click() # Users(dashboard menu)
    time.sleep(3)

    driver.find_element(By.XPATH,"/html/body/div[3]/div[2]/div[2]/div/div[2]/div[3]/a[2]/div[2]/span").click()
    time.sleep(3)

    # user_container = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div[2]/div/div[3]") #conatainer to scroll
    # driver.execute_script("arguments[0].scrollIntoView(true);", user_container) #scroller

    driver.find_element(By.XPATH,'//*[@id="container"]/div/div[1]/a[2]').click() #Modules
    time.sleep(2)

    driver.find_element(By.XPATH,'//*[@id="modulesList"]/a[1]/div[2]/h3').click() #Module(Broadcast)
    time.sleep(2)

    driver.find_element(By.XPATH,'//*[@id="modulesList"]/a[2]/div[2]/h3').click()#Module(CM)
    time.sleep(2)

    driver.find_element(By.XPATH,'//*[@id="modulesList"]/a[3]/div[2]/h3').click()#Module(Customer)
    time.sleep(2)

    driver.find_element(By.XPATH,'//*[@id="modulesList"]/a[4]/div[2]/h3').click()#Module(Lead)
    time.sleep(2)

    driver.find_element(By.XPATH,'//*[@id="modulesList"]/a[5]/div[2]/h3').click()#Module(Taskbird)
    time.sleep(5)

    driver.find_element(By.XPATH,'//*[@id="container"]/div/div[1]/a[3]').click() # Groups
    time.sleep(2)

    driver.find_element(By.XPATH,'//*[@id="container"]/div/div[2]/a').click() # Create Group
    time.sleep(2)
    
    driver.find_element(By.XPATH,'//*[@id="groupList"]/a/div[2]/h3').click() #Group(groupname)
    time.sleep(2)

    driver.find_element(By.XPATH,'//*[@id="container"]/div/div[1]/a[4]').click() #Roles
    time.sleep(2)

    driver.find_element(By.XPATH,'//*[@id="container"]/div/div[2]/a').click() #Roles(Create)
    time.sleep(2)

    driver.find_element(By.XPATH,'//*[@id="rolesList"]/a').click() #Roles(Admin)
    time.sleep(3)

    driver.find_element(By.XPATH,'//*[@id="wrapper-main"]/div[1]/div/div[1]/span').click()#Insights(dashboard menu)
    time.sleep(3)

    driver.find_element(By.XPATH,'//*[@id="wrapper-main"]/div[1]/div/div[1]/div[3]/a[1]').click() #Insights(Agent Report)
    time.sleep(3)

    driver.find_element(By.XPATH,'//*[@id="wrapper-main"]/div[1]/div/div[1]/div[3]/a[2]').click() #Insights(Login/Log0ut Report)
    time.sleep(3)

    driver.find_element(By.XPATH,'//*[@id="wrapper-main"]/div[1]/div/div[1]/div[3]/a[3]').click() #Insights(CM Summary)
    time.sleep(3)

    driver.find_element(By.XPATH,'//*[@id="wrapper-main"]/div[1]/div/div[1]/div[3]/a[4]').click() #Insights(Chat summary)
    time.sleep(3)

    driver.find_element(By.XPATH,'//*[@id="wrapper-main"]/div[1]/div/div[1]/div[3]/a[5]').click() #Insights(SMS Report)
    time.sleep(3)

    driver.find_element(By.XPATH,'//*[@id="wrapper-main"]/div[1]/div/div[1]/div[3]/a[6]').click() #Insights(Disposition setup)
    time.sleep(3)

    driver.find_element(By.XPATH,'//*[@id="wrapper-main"]/div[1]/div/div[1]/div[3]/a[7]').click() ##Insights(Disposition SUmmary)
    time.sleep(3)

    driver.find_element(By.XPATH,'//*[@id="wrapper-main"]/div[1]/div/a[3]/span').click() #Livechat(Dashboard menu)
    time.sleep(3)

    driver.find_element(By.XPATH,'//*[@id="container"]/div/div[1]/div/a[1]').click() #Livechat(Add widget)
    time.sleep(2)

    driver.find_element(By.XPATH,'//*[@id="container"]/div/div[1]/div/a').click() #Livechat(Go to Widget List)
    time.sleep(2)

    driver.find_element(By.XPATH,'//*[@id="container"]/div/div[1]/div/a[2]').click() #Livechar(Link channel in Widget)
    time.sleep(3)

    driver.find_element(By.XPATH,'//*[@id="wrapper-main"]/div[1]/div/a[4]/span').click() #Channels(Dashboard menu)
    time.sleep(3)

    driver.find_element(By.XPATH,'//*[@id="container"]/div/div/div/div[2]/div[1]/a/div/div/h5').click() #Channels(WhatsApp)
    time.sleep(2)

    driver.find_element(By.XPATH,'//*[@id="wrapper-main"]/div[1]/div/a[4]/span').click() #Channels(Dashboard menu)
    time.sleep(2)

    driver.find_element(By.XPATH,'//*[@id="container"]/div/div/div/div[2]/div[2]/a/div/div/h5').click() #Channels(Messenger)
    time.sleep(2)

    driver.find_element(By.XPATH,'//*[@id="wrapper-main"]/div[1]/div/a[4]/span').click() #Channels(Dashboard menu)
    time.sleep(2)

    driver.find_element(By.XPATH,'//*[@id="container"]/div/div/div/div[2]/div[3]/a/div/div/h5').click()#Channels(Viber)
    time.sleep(2)

    driver.find_element(By.XPATH,'//*[@id="container"]/div/div/div[1]/a').click() #channels(Viber -> Add Channel)
    time.sleep(2)

    driver.find_element(By.XPATH,'//*[@id="container"]/div/div[1]/div/form/div[4]/a').click() #Channels (Viber ->Add Channel ->Back)
    time.sleep(2)

    driver.find_element(By.XPATH,'//*[@id="container"]/div/div/div/div[2]/div[4]/a/div/div/h5').click() #Channels (Email)
    time.sleep(2)

    driver.find_element(By.XPATH,'//*[@id="wrapper-main"]/div[1]/div/a[4]/span').click() #Channels(Dashboard menu)
    time.sleep(2)

    driver.find_element(By.XPATH,'//*[@id="container"]/div/div/div/div[2]/div[5]/a/div/div/h5').click() #Channels (SMS)
    time.sleep(2)

    driver.find_element(By.XPATH,'//*[@id="wrapper-main"]/div[1]/div/a[4]/span').click() #Channels(Dashboard menu)
    time.sleep(2)

    driver.find_element(By.XPATH,'//*[@id="container"]/div/div/div/div[2]/div[6]/div/div/a[1]/h5').click() #Channels(WeChat)
    time.sleep(2)

    driver.find_element(By.XPATH,'//*[@id="wrapper-main"]/div[1]/div/div[2]/span').click() #Numbers(Dashboard Menu)
    time.sleep(2)

    driver.find_element(By.XPATH,'//*[@id="wrapper-main"]/div[1]/div/div[2]/div[3]/a').click()  #Numbers(My Numbers)
    time.sleep(2)

    driver.find_element(By.XPATH,'//*[@id="container"]/div/div/div[1]/a').click() #Numbers(My Numbers ->Buy Number)
    time.sleep(2)

    driver.find_element(By.XPATH,'//*[@id="id_country"]').click() #Numbers(My Numbers -Buy Number ->Select Country)
    time.sleep(2)

    driver.find_element(By.XPATH,'//*[@id="id_country"]/option[5]').click() ##Numbers(My Numbers -Buy Number ->Select Country)
    time.sleep(2)

    driver.find_element(By.XPATH,'//*[@id="container"]/div/div[1]/div[1]/div[1]/a').click() #Numbers(My Numbers -Buy Number ->select Nepal)
    time.sleep(2)

    driver.find_element(By.XPATH,'//*[@id="wrapper-main"]/div[1]/div/a[5]/span').click() #Call(Dashboard menu)
    time.sleep(2)

    # driver.find_element(By.XPATH,'//*[@id="ebxBox"]/div[2]/a').click() # Call(Buy Number)
    # time.sleep(2)
    
    driver.find_element(By.XPATH,'//*[@id="ek_myButton"]').click() #Livehchat button
    time.sleep(2)

    driver.find_element(By.XPATH,'//*[@id="wrapper-main"]/div[2]/div[1]/div[1]/div[2]/a').click() # My Tickets(Navbar menu)
    time.sleep(2)

    driver.find_element(By.XPATH,'//*[@id="container"]/div/div[1]/div/a').click() #My Tickets(Create Ticket)
    time.sleep(2)

    driver.find_element(By.XPATH,'//*[@id="wrapper-main"]/div[2]/div[1]/div[2]/div[3]/a').click() #TopUp(navbar menu)
    time.sleep(2)

    driver.find_element(By.XPATH,'//*[@id="user_info"]').click()#Profile
    time.sleep(2)

    driver.find_element(By.XPATH,'//*[@id="user_info_dropdown"]/div/a[2]').click() #Profile(settings)
    time.sleep(2)

    driver.find_element(By.XPATH,'//*[@id="user_info"]').click()#Profile
    time.sleep(2)

    driver.find_element(By.XPATH,'//*[@id="user_info_dropdown"]/div/a[3]').click() #Profile(your accounts)
    time.sleep(2)

    driver.find_element(By.XPATH,'//*[@id="password_link"]').click() #Profile (My Account ->Password Reset)
    time.sleep(2)

    
    driver.find_element(By.XPATH,'//*[@id="user_info"]').click()#Profile
    time.sleep(2)

    driver.find_element(By.XPATH,'//*[@id="user_info_dropdown"]/div/a[4]').click() #Profile(Billing)
    time.sleep(2)



    driver.find_element(By.XPATH,'//*[@id="wrapper-main"]/div[1]/div/a[6]/span').click() #Orbit360(dashboard menu)
    time.sleep(5)



except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser window
    driver.quit()
