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

    # Navigate to the desired menu item that opens a new window
    driver.find_element(By.XPATH, '//*[@id="wrapper-main"]/div[1]/div/a[6]/span').click()  # Communication Manager (Orbit dashboard menu)

    # Wait for the new window to be available in the window handles
    new_window_handle = [handle for handle in driver.window_handles if handle != driver.current_window_handle][0]
    driver.switch_to.window(new_window_handle)

    # Perform actions in the new window
    element = WebDriverWait(driver, 50).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="right"]/div/div[3]/a'))
    )
    element.click()

    # Wait for the new window to be ready (you can adjust the condition based on the page behavior)
    WebDriverWait(driver, 30).until(EC.title_contains("Expected Title"))

    # Continue with additional actions in the new window
    element_in_new_window = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="leftbar"]/div[1]/ul/li[1]/a'))
    )
    element_in_new_window.click()

    # Additional actions in the new window

    time.sleep(10)

    # Continue with the rest of your code in the new window

finally:
    # Close the browser window
    driver.quit()
