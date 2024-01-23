
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set the URL you want to open
APP_URL = "https://dashboard.orbit360.cx/"

# Get user input for email and password
email = input("Enter your email: ")
password = input("Enter your password: ")



# Create a Chrome WebDriver instance
driver = webdriver.Chrome()
driver.maximize_window()

# Define a reusable function for waiting and clicking
def wait_and_click(xpath):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath))).click()

try:
    # Open the URL in the browser
    driver.get(APP_URL)

    # Use WebDriverWait to wait for the username field to be present
    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "email"))
    )
  
    password_field = driver.find_element(By.ID, "password")
  
    username_field.send_keys(email)
    password_field.send_keys(password)
 
    signin_button = driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[4]/button')
    signin_button.click()

    # Wait and click for the subsequent actions
    wait_and_click('/html/body/div[3]/div[1]/div/a[2]/span') #users
    wait_and_click('/html/body/div[3]/div[2]/div[2]/div/div[1]/a[2]') #Modules

    #Modules ->Broadcast
    # wait_and_click('/html/body/div[3]/div[2]/div[2]/div/div[2]/div[2]/a[1]/div[2]/h3') #broadcast
    # wait_and_click('/html/body/div[3]/div[2]/div[2]/div/div[3]/div[2]/form/div[1]/div[1]/label[2]')#select
    # wait_and_click('/html/body/div[3]/div[2]/div[2]/div/div[3]/div[2]/form/div[2]/button') #save changes
    # wait_and_click('/html/body/div[5]/div/div[6]/button[1]') #confirmation modal

    #Groups
    # wait_and_click('/html/body/div[3]/div[2]/div[2]/div/div[1]/a[3]') #Groups
    # wait_and_click('/html/body/div[3]/div[2]/div[2]/div/div[2]/a') #create group
    # time.sleep(10)
    # wait_and_click('/html/body/div[3]/div[2]/div[2]/div/div[3]/div[2]/form/div[4]/button') #save changes
    # wait_and_click('/html/body/div[5]/div/div[6]/button[1]') #confirmation modal
   

   #Modules -Roles
    wait_and_click('/html/body/div[3]/div[2]/div[2]/div/div[1]/a[4]') #roles
    wait_and_click('/html/body/div[3]/div[2]/div[2]/div/div[2]/a') #create role
    time.sleep(10)
    wait_and_click('/html/body/div[3]/div[2]/div[2]/div/div[3]/div[2]/form/div[4]/button') #Save changes
    wait_and_click('/html/body/div[5]/div/div[6]/button[1]') #confirmation modal




finally:
    time.sleep(10)
    # Close the browser window
    driver.quit()
