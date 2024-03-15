import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyperclip

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

    wait_and_click('/html/body/div[3]/div[1]/div/a[3]/span')  # livechat
    wait_and_click('/html/body/div[3]/div[2]/div[2]/div/div[1]/div/a[1]')  # Add widget
    time.sleep(5)
    wait_and_click('/html/body/div[3]/div[2]/div[2]/div/div[2]/div[2]/div/form/div[1]/input')  # widget name input field

    wait_and_click('/html/body/div[3]/div[2]/div[2]/div/div[2]/div[2]/div/form/div[2]/button')  # create button
    wait_and_click('/html/body/div[3]/div[2]/div[2]/div/div[2]/div[2]/div/form/div[3]/div/div/div[3]/button[2]')  # proceed button
    wait_and_click('/html/body/div[3]/div[2]/div[2]/div[1]/div[2]/div[2]/div/div/button/i')
    wait_and_click('/html/body/div[3]/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div/button')  # copies link to the clipboard

    # Open a new tab
    driver.execute_script("window.open('', '_blank');")
    # Switch to the new tab
    driver.switch_to.window(driver.window_handles[1])
 
    # Retrieve the link from the clipboard using pyperclip
    link = pyperclip.paste()

    # Locate the input field and paste the link
    input_field = driver.find_element(By.XPATH, '//*[@id="your_input_field_xpath"]')  
    input_field.click()
    input_field.send_keys(link)

    input_field.submit()

finally:
    time.sleep(7)
    driver.quit()
