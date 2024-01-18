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
    username_field.send_keys("rameshbohora88@gmail.com")
    password_field.send_keys("ekg@12321")

    # Locate the sign-in button by classname and click it
    signin_button = driver.find_element(By.CLASS_NAME, "primary-btn")
    signin_button.click()
    time.sleep(5)

    driver.find_element(By.XPATH,"/html/body/div[3]/div[2]/div[1]/div[2]/div[1]/a/img").click() # i icon
    time.sleep(3)

    # Find and click each introjs button with a 3-second wait after each click
    introjs_buttons = driver.find_elements(By.CLASS_NAME, "introjs-button.introjs-nextbutton")
    for button in introjs_buttons:
        button.click()
        time.sleep(3)

    driver.find_element(By.CLASS_NAME, "introjs-button.introjs-skipbutton.introjs-donebutton").click()
    time.sleep(3)

    # Buttons with a 3-second wait after each click
    buttons_to_click = [
        "get-started-btn",  # Numbers (Buy Now Button)
        "nav-icon",  # Get Started dashboard Menu
        '//*[@id="container"]/div/div/div[4]/div/div[4]/a',  # Livechat (Get Started button)
        'nav-icon',  # Get Started (dashboard menu)
        '/html/body/div[3]/div[2]/div[2]/div/div/div[5]/div/div[4]/a[1]',  # Channels (Get Connected button)
        '/html/body/div[3]/div[1]/div/a[2]/span',  # Users (dashboard menu)
        '/html/body/div[3]/div[2]/div[2]/div/div[2]/div[3]/a[2]/div[2]/span',  # Some other button
        '//*[@id="container"]/div/div[1]/a[2]',  # Modules
        '//*[@id="modulesList"]/a[1]/div[2]/h3',  # Module (Broadcast)
        '//*[@id="modulesList"]/a[2]/div[2]/h3',  # Module (CM)
        '//*[@id="modulesList"]/a[3]/div[2]/h3',  # Module (Customer)
        '//*[@id="modulesList"]/a[4]/div[2]/h3',  # Module (Lead)
        '//*[@id="modulesList"]/a[5]/div[2]/h3',  # Module (Taskbird)
        '//*[@id="container"]/div/div[1]/a[3]',  # Groups
        '//*[@id="container"]/div/div[2]/a',  # Create Group
        '//*[@id="groupList"]/a/div[2]/h3',  # Group (groupname)
        '//*[@id="container"]/div/div[1]/a[4]',  # Roles
        '//*[@id="container"]/div/div[2]/a',  # Roles
        '//*[@id="rolesList"]/a[2]/div[2]/h3'  # Some other button
    ]

    for button_xpath in buttons_to_click:
        driver.find_element(By.XPATH if '/' in button_xpath else By.CLASS_NAME, button_xpath).click()
        time.sleep(3)

finally:
    # Close the browser window
    driver.quit()
