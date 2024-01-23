from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

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

    # Add an explicit wait for the dashboard to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="wrapper-main"]/div[1]/div/a[6]/span'))
    )

    # Directly navigate to the Taskbird page
    driver.get("https://dashboard.orbit360.cx/taskbird")  # Replace with the correct URL if needed

    # Add more interactions here...

except (NoSuchElementException, TimeoutException, Exception) as e:
    print(f"Element not found or not interactable: {e}")

finally:
    # Close the browser window
    driver.quit()
