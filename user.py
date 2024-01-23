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

# User Addition 
usermail = input("Enter user email: ")
username = input("Enter username: ")
name = input("Enter name: ")
phone = input("Enter phone number: ")
new_user_password = input("Enter password: ")
password_confirmation = input("Enter confirmation password: ")

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
    wait_and_click('/html/body/div[3]/div[1]/div/a[2]/span')
    wait_and_click('/html/body/div[3]/div[2]/div[2]/div/div[2]/a')
    wait_and_click('/html/body/div[3]/div[2]/div[3]/div/div/div[3]/button[2]')

    # Fill out the new user form
    wait_and_click('/html/body/div[3]/div[2]/div[2]/div/div[3]/div[2]/form/div[1]/input')

    driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div[2]/div/div[3]/div[2]/form/div[1]/input').send_keys(usermail)
    driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div[2]/div/div[3]/div[2]/form/div[2]/input').send_keys(username)
    driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div[2]/div/div[3]/div[2]/form/div[3]/input').send_keys(name)
    driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div[2]/div/div[3]/div[2]/form/div[4]/input').send_keys(phone)
    driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div[2]/div/div[3]/div[2]/form/div[5]/input').send_keys(new_user_password)
    driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div[2]/div/div[3]/div[2]/form/div[6]/input').send_keys(password_confirmation)

    wait_and_click('/html/body/div[3]/div[2]/div[2]/div/div[3]/div[2]/form/div[7]/button') #create button
    wait_and_click('/html/body/div[3]/div[2]/div[2]/div/div[3]/div[2]/form/div[8]/div/div/div[3]/button[2]') #proceed button

finally:
    time.sleep(10)
    # Close the browser window
    driver.quit()
