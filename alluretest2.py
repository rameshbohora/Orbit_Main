import allure
import pytest
import subprocess
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from faker import Faker
import random
import string


# Set the URL you want to open
APP_URL = "https://dashboard.orbit360.cx/"

# Initialize Faker
fake = Faker()

# Set up fixtures
@pytest.fixture(scope="module")
def driver_setup():
    # Create a Chrome WebDriver instance
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

#reusable function for waiting and clicking
def wait_and_click(driver, xpath):
    try:
        element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        element.click()
    except StaleElementReferenceException:
        # If element is stale, wait for it to become stale and find it again
        WebDriverWait(driver, 10).until(EC.staleness_of(element))
        element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        element.click()

def generate_email():
    return fake.email()

def generate_name():
    return fake.name()

def generate_username():
    return fake.user_name()

def generate_phone_number():
    # Generate a random phone number with minimum 3 digits and maximum 10 digits
    return ''.join(random.choices(string.digits, k=random.randint(3, 10)))


def generate_password(length=12):
    # Generate a random password with alphanumeric characters and symbols
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

# User Addition 
usermail = generate_email()
username = generate_username()
name = generate_name()
phone = generate_phone_number()
new_user_password = generate_password()
password_confirmation = new_user_password

#Create Group
groupname = fake.company()

#Create Role
rolename = fake.job() + "Role"

#Checkout Details
companyname = fake.company()
billingname = fake.name()
address = fake.address()
state = fake.state()
postalcode = fake.postcode()
city = fake.city()

#Card Details (provide test data directly)
cardnumber = "1234567890123456"
cvn = "123"

def login(driver, email, password):
    driver.get(APP_URL)
    wait_and_click(driver, '/html/body/div/div[2]/form/div[4]/button')
    driver.find_element(By.ID, "email").send_keys(email)
    driver.find_element(By.ID, "password").send_keys(password)
    wait_and_click(driver, '/html/body/div/div[2]/form/div[4]/button') 

def introjs(driver):
    wait_and_click(driver, '/html/body/div[3]/div[2]/div[1]/div[2]/div[1]/a/img')
    wait_and_click(driver, '/html/body/div[8]/div/div[5]/a[3]')
    wait_and_click(driver, '/html/body/div[8]/div/div[5]/a[3]')
    wait_and_click(driver, '/html/body/div[8]/div/div[5]/a[3]')
    wait_and_click(driver, '/html/body/div[8]/div/div[5]/a[3]')
    wait_and_click(driver, '/html/body/div[8]/div/div[5]/a[1]')

def topup(driver, companyname, billingname, address, state, postalcode, city, cardnumber, cvn):
    wait_and_click(driver, '//*[@id="wrapper-main"]/div[2]/div[1]/div[2]/div[3]/a')
    wait_and_click(driver, '//*[@id="proceed-btn"]')
    driver.find_element(By.ID,"id_company_name").send_keys(companyname)
    driver.find_element(By.ID,"id_billing_name").send_keys(billingname)
    driver.find_element(By.ID,"id_address").send_keys(address)
    driver.find_element(By.ID,"id_state").send_keys(state)
    driver.find_element(By.ID,"id_postal_code").send_keys(postalcode)
    driver.find_element(By.ID,"id_city").send_keys(city)
    wait_and_click(driver, '//*[@id="id_country"]/option[152]')
    wait_and_click(driver, '//*[@id="checkoutbtn"]')
    wait_and_click(driver, '//*[@id="proceedbtn"]')
    wait_and_click(driver, '//*[@id="nextbtn"]')
    driver.find_element(By.ID,"card_number").send_keys(cardnumber)
    wait_and_click(driver, '//*[@id="card_expiry_month"]/option[13]')
    wait_and_click(driver, '//*[@id="card_expiry_year"]/option[2]')
    driver.find_element(By.ID,"card_cvn").send_keys(cvn)
    wait_and_click(driver, '//*[@id="payment_details_lower"]/input[2]')
    wait_and_click(driver, '//*[@id="receipt_post_buttons"]/div[2]/a')

def user(driver):
    wait_and_click(driver, '//*[@id="wrapper-main"]/div[1]/div/a[2]/span')

def add_user(driver, usermail, username, name, phone, new_user_password, password_confirmation):
    wait_and_click(driver, '//*[@id="createusermodal"]')
    wait_and_click(driver, '//*[@id="confirmuser"]')
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="id_email"]'))).send_keys(usermail)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="id_username"]'))).send_keys(username)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="id_name"]'))).send_keys(name)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="id_ph_no"]'))).send_keys(phone)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="id_password1"]'))).send_keys(new_user_password)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="id_password2"]'))).send_keys(password_confirmation)
    wait_and_click(driver, '//*[@id="createUserButton"]') #create button
    wait_and_click(driver, '//*[@id="confirmCreateUser"]') #proceed button

def configure_modules(driver):
    wait_and_click(driver, '//*[@id="container"]/div/div[1]/a[2]')
    # Configure modules here...

def create_group(driver, groupname):
    wait_and_click(driver, '//*[@id="container"]/div/div[1]/a[3]')  # Groups
    # Create group here...

def setup_roles(driver, rolename):
    wait_and_click(driver, '//*[@id="container"]/div/div[1]/a[4]')  # Roles
    # Setup roles here...

def insights(driver):
    wait_and_click(driver, '//*[@id="wrapper-main"]/div[1]/div/div[1]/span')

def livechat(driver):
    wait_and_click(driver, '//*[@id="wrapper-main"]/div[1]/div/a[3]/span')

def channels(driver):
    wait_and_click(driver, '//*[@id="wrapper-main"]/div[1]/div/a[4]/span')

def numbers(driver):
    wait_and_click(driver, '//*[@id="wrapper-main"]/div[1]/div/div[2]/span')

def call(driver):
    wait_and_click(driver, '//*[@id="wrapper-main"]/div[1]/div/a[5]/span')

def livechat_button(driver):
    wait_and_click(driver, '//*[@id="ek_myButton"]')

def tickets(driver):
    wait_and_click(driver, '//*[@id="wrapper-main"]/div[2]/div[1]/div[1]/div[2]/a')

@allure.feature("Test Feature")
@allure.story("Test Story")
@allure.title("Test Example")
def test_example(driver_setup):
    with allure.step("Initializing test data"):
        email = generate_email()
        password = generate_password()
        companyname = fake.company()
        billingname = fake.name()
        address = fake.address()
        state = fake.state()
        postalcode = fake.postcode()
        city = fake.city()

    driver = driver_setup

    with allure.step("Executing test steps"):
        try:
            login(driver, email, password)
            introjs(driver)
            topup(driver, companyname, billingname, address, state, postalcode, city, cardnumber, cvn)
            user(driver)
            add_user(driver, usermail, username, name, phone, new_user_password, password_confirmation)
            configure_modules(driver)
            create_group(driver, groupname)
            setup_roles(driver, rolename)
            insights(driver)
            livechat(driver)
            channels(driver)
            numbers(driver)
            call(driver)
            livechat_button(driver)
            tickets(driver)
        except Exception as e:
            # Attach exception information to Allure report
            allure.attach(str(e), name="Exception", attachment_type=allure.attachment_type.TEXT)
            raise e

if __name__ == "__main__":
    # Run tests and generate Allure report
    pytest.main(['-v', '--alluredir', 'allure-results'])
    # Generate Allure report
    allure_cmd = 'allure generate --clean allure-results -o allure-report'
    subprocess.call(allure_cmd, shell=True)
