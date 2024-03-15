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
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, xpath))).click()

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
    wait_and_click("/html/body/div[3]/div[2]/div[1]/div[2]/div[1]/a/img")
    wait_and_click('/html/body/div[8]/div/div[5]/a[3]')
    wait_and_click('/html/body/div[8]/div/div[5]/a[3]')
    wait_and_click('/html/body/div[8]/div/div[5]/a[3]')
    wait_and_click('/html/body/div[8]/div/div[5]/a[3]')
    wait_and_click('/html/body/div[8]/div/div[5]/a[1]')
    wait_and_click('/html/body/div[3]/div[2]/div[2]/div/div/div[3]/div/div[4]/a')
    wait_and_click('//html/body/div[3]/div[1]/div/a[1]/span')
    wait_and_click('//*[@id="container"]/div/div/div[4]/div/div[4]/a')
    wait_and_click('/html/body/div[3]/div[1]/div/a[1]/span')
    wait_and_click('/html/body/div[3]/div[2]/div[2]/div/div/div[5]/div/div[4]/a[1]') 
    wait_and_click('/html/body/div[3]/div[1]/div/a[2]/span')
    wait_and_click('/html/body/div[3]/div[2]/div[2]/div/div[2]/div[3]/a[2]/div[2]/span')
    wait_and_click('//*[@id="container"]/div/div[1]/a[2]') 
    wait_and_click('//*[@id="modulesList"]/a[1]/div[2]/h3')
    wait_and_click('//*[@id="modulesList"]/a[2]/div[2]/h3') 
    wait_and_click('//*[@id="modulesList"]/a[3]/div[2]/h3') 
    wait_and_click('//*[@id="modulesList"]/a[4]/div[2]/h3') 
    wait_and_click('//*[@id="modulesList"]/a[5]/div[2]/h3')
    wait_and_click('//*[@id="container"]/div/div[1]/a[3]')
    wait_and_click('//*[@id="container"]/div/div[2]/a')
    wait_and_click('//*[@id="groupList"]/a/div[2]/h3')
    wait_and_click('//*[@id="container"]/div/div[1]/a[4]')
    wait_and_click('//*[@id="container"]/div/div[2]/a')
    wait_and_click('//*[@id="rolesList"]/a')
    wait_and_click('//*[@id="wrapper-main"]/div[1]/div/div[1]/span')
    wait_and_click('//*[@id="wrapper-main"]/div[1]/div/div[1]/div[3]/a[1]')
    wait_and_click('//*[@id="wrapper-main"]/div[1]/div/div[1]/div[3]/a[2]')
    wait_and_click('//*[@id="wrapper-main"]/div[1]/div/div[1]/div[3]/a[3]')
    wait_and_click('//*[@id="wrapper-main"]/div[1]/div/div[1]/div[3]/a[4]')
    wait_and_click('//*[@id="wrapper-main"]/div[1]/div/div[1]/div[3]/a[5]')
    wait_and_click('//*[@id="wrapper-main"]/div[1]/div/div[1]/div[3]/a[6]')
    wait_and_click('//*[@id="wrapper-main"]/div[1]/div/div[1]/div[3]/a[7]')
    wait_and_click('//*[@id="wrapper-main"]/div[1]/div/a[3]/span')
    wait_and_click('//*[@id="container"]/div/div[1]/div/a[1]')
    wait_and_click('//*[@id="container"]/div/div[1]/div/a')
    wait_and_click('//*[@id="container"]/div/div[1]/div/a[2]')
    wait_and_click('//*[@id="wrapper-main"]/div[1]/div/a[4]/span')
    wait_and_click('//*[@id="container"]/div/div/div/div[2]/div[1]/a/div/div/h5')
    wait_and_click('//*[@id="wrapper-main"]/div[1]/div/a[4]/span')
    wait_and_click('//*[@id="container"]/div/div/div/div[2]/div[2]/a/div/div/h5')
    wait_and_click('//*[@id="wrapper-main"]/div[1]/div/a[4]/span')
    wait_and_click('//*[@id="container"]/div/div/div/div[2]/div[3]/a/div/div/h5')
    wait_and_click('//*[@id="container"]/div/div/div[1]/a')
    wait_and_click('//*[@id="container"]/div/div[1]/div/form/div[4]/a')
    wait_and_click('//*[@id="container"]/div/div/div/div[2]/div[4]/a/div/div/h5')
    wait_and_click('//*[@id="wrapper-main"]/div[1]/div/a[4]/span')
    wait_and_click('//*[@id="container"]/div/div/div/div[2]/div[5]/a/div/div/h5')
    wait_and_click('//*[@id="wrapper-main"]/div[1]/div/a[4]/span')
    wait_and_click('//*[@id="container"]/div/div/div/div[2]/div[6]/div/div/a[1]/h5')
    wait_and_click('//*[@id="wrapper-main"]/div[1]/div/div[2]/span')
    wait_and_click('//*[@id="wrapper-main"]/div[1]/div/div[2]/div[3]/a')
    wait_and_click('//*[@id="container"]/div/div/div[1]/a')
    wait_and_click('//*[@id="id_country"]')
    wait_and_click('//*[@id="id_country"]/option[5]')
    wait_and_click('//*[@id="container"]/div/div[1]/div[1]/div[1]/a')
    wait_and_click('//*[@id="wrapper-main"]/div[1]/div/a[5]/span')
    wait_and_click('/html/body/button')
    wait_and_click('//*[@id="wrapper-main"]/div[2]/div[1]/div[1]/div[2]/a')
    wait_and_click('//*[@id="container"]/div/div[1]/div/a')
    wait_and_click('//*[@id="wrapper-main"]/div[2]/div[1]/div[2]/div[3]/a')
    wait_and_click('//*[@id="user_info"]')
    wait_and_click('//*[@id="user_info_dropdown"]/div/a[2]')
    wait_and_click('//*[@id="user_info"]')
    wait_and_click('//*[@id="user_info_dropdown"]/div/a[3]')
    wait_and_click('//*[@id="password_link"]')
    wait_and_click('//*[@id="user_info"]')
    wait_and_click('//*[@id="user_info_dropdown"]/div/a[4]')
    wait_and_click('//*[@id="wrapper-main"]/div[1]/div/a[6]/span')

finally:
    # Close the browser window
    driver.quit()
