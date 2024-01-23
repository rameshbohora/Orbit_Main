from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set the URL you want to open
APP_URL = "https://dashboard.orbit360.cx/"

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
    username_field.send_keys("ramesh.bohara@apexcollege.edu.np")
    password_field.send_keys("ekg@12321")

    # Locate the sign-in button by classname and click it
    signin_button = driver.find_element(By.CLASS_NAME, "primary-btn")
    signin_button.click()
    time.sleep(3)

    driver.find_element(By.XPATH,'//*[@id="wrapper-main"]/div[1]/div/a[6]/span').click() #Communincation Manager(Orbit dashoard menu)
    time.sleep(10)

    driver.find_element(By.XPATH,'/html/body/div[3]/div[1]/div/div/div[3]/a').click() #Taskbird(Dashboard Menu)
    time.sleep(3)

    driver.find_element(By.XPATH,'//*[@id="leftbar"]/div[1]/ul/li[1]/a/p').click() #Task (Taskbird Menu)
    time.sleep(2)

    driver.find_element(By.XPATH,'//*[@id="leftbar"]/div[1]/ul/li[2]/a/p').click() #Project(Taskbird Menu)
    time.sleep(2)

    driver.find_element(By.XPATH,'//*[@id="leftbar"]/div[1]/ul/li[3]/a/p').click() #Task Status(Taskbird Menu)
    time.sleep(2)

    driver.find_element(By.XPATH,'//*[@id="leftbar"]/div[1]/ul/li[4]/a/p').click() #Priorities(Taskbird menu)
    time.sleep(2)

    driver.find_element(By.XPATH,'//*[@id="leftbar"]/div[1]/ul/li[5]/a/span').click() #Set SMS/Email(Taskbird Menu)
    time.sleep(2)

    driver.find_element(By.XPATH,'//*[@id="leftbar"]/div[1]/ul/li[5]/div/a[1]/text()').click() #SMS
    time.sleep(2)

    driver.find_element(By.XPATH,'//*[@id="leftbar"]/div[1]/ul/li[5]/div/a[2]/text()').click() #Email
    time.sleep(2)

    driver.find_element(By.XPATH,'//*[@id="right"]/div/div[4]/a').click() #Broadcast (Dashboard menu)
    time.slee(2)

    driver.find_element(By.XPATH,'//*[@id="leftbar"]/div[1]/ul/li/a/p').click() #Campaign (Broadcast menu)
    time.slee(2)

    driver.find_element(By.XPATH,'//*[@id="right"]/div/div[5]/a').click() #Lead(Dashboard menu)
    time.sleep(2)

    driver.find_element(By.XPATH,'//*[@id="right"]/div/div[6]/a').click() #Customer(Dashboard menu)
    time.sleep(2)






    





finally:
    # Close the browser window
    driver.quit()
