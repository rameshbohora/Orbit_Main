import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from faker import Faker
import random
import string

def driver_setup():
    # Create a Chrome WebDriver instance
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def generate_email(fake):
    return fake.email()

def generate_name(fake):
    return fake.name()

def generate_username(fake):
    return fake.user_name()

def generate_phone_number():
    # Generate a random phone number with minimum 3 digits and maximum 10 digits
    return ''.join(random.choices(string.digits, k=random.randint(3, 10)))


def generate_password(length=12):
    # Generate a random password with alphanumeric characters and symbols
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))


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
def wait_and_click(xpath):
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, xpath))).click()

def login(driver, email, password):
    driver.get(APP_URL)
    wait_and_click('/html/body/div/div[2]/form/div[4]/button')
    driver.find_element(By.ID, "email").send_keys(email)
    driver.find_element(By.ID, "password").send_keys(password)
    wait_and_click('/html/body/div/div[2]/form/div[4]/button') 

def introjs(driver):
    wait_and_click('/html/body/div[3]/div[2]/div[1]/div[2]/div[1]/a/img')
    wait_and_click('/html/body/div[7]/div/div[5]/a[3]')
    wait_and_click('/html/body/div[7]/div/div[5]/a[3]')
    wait_and_click('/html/body/div[7]/div/div[5]/a[3]')
    wait_and_click('/html/body/div[7]/div/div[5]/a[3]') 
    wait_and_click('/html/body/div[7]/div/div[5]/a[1]') 

def topup(driver, companyname, billingname, address, state, postalcode, city, cardnumber, cvn):
    wait_and_click('//*[@id="wrapper-main"]/div[2]/div[1]/div[2]/div[3]/a')
    wait_and_click('//*[@id="proceed-btn"]')
    driver.find_element(By.ID,"id_company_name").send_keys(companyname)
    driver.find_element(By.ID,"id_billing_name").send_keys(billingname)
    driver.find_element(By.ID,"id_address").send_keys(address)
    driver.find_element(By.ID,"id_state").send_keys(state)
    driver.find_element(By.ID,"id_postal_code").send_keys(postalcode)
    driver.find_element(By.ID,"id_city").send_keys(city)
    wait_and_click('//*[@id="id_country"]/option[152]')
    wait_and_click('//*[@id="checkoutbtn"]')
    wait_and_click('//*[@id="proceedbtn"]')
    wait_and_click('//*[@id="nextbtn"]')
    driver.find_element(By.ID,"card_number").send_keys(cardnumber)
    wait_and_click('//*[@id="card_expiry_month"]/option[13]')
    wait_and_click('//*[@id="card_expiry_year"]/option[2]')
    driver.find_element(By.ID,"card_cvn").send_keys(cvn)
    wait_and_click('//*[@id="payment_details_lower"]/input[2]')
    wait_and_click('//*[@id="receipt_post_buttons"]/div[2]/a')

def user(driver):
    wait_and_click('//*[@id="wrapper-main"]/div[1]/div/a[2]/span')



def add_user(driver, usermail, username, name, phone, new_user_password, password_confirmation):

    wait_and_click('//*[@id="createusermodal"]')
    wait_and_click('//*[@id="confirmuser"]')
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="id_email"]'))).send_keys(usermail)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="id_username"]'))).send_keys(username)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="id_name"]'))).send_keys(name)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="id_ph_no"]'))).send_keys(phone)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="id_password1"]'))).send_keys(new_user_password)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="id_password2"]'))).send_keys(password_confirmation)


    wait_and_click('//*[@id="createUserButton"]') #create button
    wait_and_click('//*[@id="confirmCreateUser"]') #proceed button
    

def configure_modules(driver):
    wait_and_click('//*[@id="container"]/div/div[1]/a[2]')

    #Broadcast
    wait_and_click('//*[@id="modulesList"]/a[1]/div[2]/h3')
    wait_and_click('//*[@id="formbody"]/form/div[1]/div[1]/label[2]')
    wait_and_click('//*[@id="formbody"]/form/div[2]/button')
    wait_and_click('/html/body/div[5]/div/div[6]/button[1]')

    #CM
    wait_and_click('//*[@id="modulesList"]/a[2]/div[2]/h3')
    wait_and_click('//*[@id="formbody"]/form/div[1]/div[1]/label[2]')
    wait_and_click('//*[@id="formbody"]/form/div[2]/button')
    wait_and_click('/html/body/div[5]/div/div[6]/button[1]')

    #Customer
    wait_and_click('//*[@id="modulesList"]/a[3]/div[2]/h3')
    wait_and_click('//*[@id="formbody"]/form/div[1]/div[1]/label[2]')
    wait_and_click('//*[@id="formbody"]/form/div[2]/button')
    wait_and_click('/html/body/div[5]/div/div[6]/button[1]')

    #Lead
    wait_and_click('//*[@id="modulesList"]/a[4]/div[2]/h3')
    wait_and_click('//*[@id="formbody"]/form/div[1]/div[1]/label[2]')
    wait_and_click('//*[@id="formbody"]/form/div[2]/button')
    wait_and_click('/html/body/div[5]/div/div[6]/button[1]')

    #Taskbird
    wait_and_click('//*[@id="modulesList"]/a[5]/div[2]/h3')
    wait_and_click('//*[@id="formbody"]/form/div[1]/div[1]/label[2]')
    wait_and_click('//*[@id="formbody"]/form/div[2]/button')
    wait_and_click('/html/body/div[5]/div/div[6]/button[1]')

def create_group(driver, groupname):
    wait_and_click('//*[@id="container"]/div/div[1]/a[3]')  # Groups

    #Create Group
    wait_and_click('//*[@id="container"]/div/div[2]/a')
    WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="id_name"]'))).send_keys(groupname)
    wait_and_click('//*[@id="id_supervisor"]/option[2]')
    wait_and_click('//*[@id="create_group_form"]/div[3]/div[1]/label[2]')
    wait_and_click('//*[@id="create_group_form"]/div[4]/button')
    wait_and_click('/html/body/div[5]/div/div[6]/button[1]') 
    
    

    

def setup_roles(driver, rolename):
    wait_and_click('//*[@id="container"]/div/div[1]/a[4]')  # Roles

    #Create Role
    wait_and_click('//*[@id="container"]/div/div[2]/a')
    WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="id_name"]'))).send_keys(rolename)
    wait_and_click(By.XPATH,'//*[@id="select_allid_assigned_users"]')
    wait_and_click('//*[@id="create_group_form"]/div[3]/div[1]/label[2]')
    wait_and_click('//*[@id="create_group_form"]/div[4]/button')
    wait_and_click('/html/body/div[5]/div/div[6]/button[1]') 


def insights(driver):
    wait_and_click('//*[@id="wrapper-main"]/div[1]/div/div[1]/span')


def livechat(driver):
    wait_and_click('//*[@id="wrapper-main"]/div[1]/div/a[3]/span')

def channels(driver):
    wait_and_click('//*[@id="wrapper-main"]/div[1]/div/a[4]/span')

def numbers(driver):
    wait_and_click('//*[@id="wrapper-main"]/div[1]/div/div[2]/span')

def call(driver):
    wait_and_click('//*[@id="wrapper-main"]/div[1]/div/a[5]/span')

def livechat_button(driver):
    wait_and_click('//*[@id="ek_myButton"]')

def tickets(driver):
    wait_and_click('//*[@id="wrapper-main"]/div[2]/div[1]/div[1]/div[2]/a')

if __name__=='__main__':

    try:
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        #Card Details
        cardnumber = input("Enter card number:")
        cvn = input("enter cvn number:")
        driver = webdriver.Chrome()
        driver.maximize_window()
        # Set the URL you want to open
        APP_URL = "https://dashboard.orbit360.cx/"
        fake = Faker()


        # User Addition 
        usermail = generate_email(fake)
        username = generate_username(fake)
        name = generate_name(fake)
        phone = generate_phone_number()
        new_user_password = generate_password()
        password_confirmation = new_user_password

        #Create Group
        groupname = fake.name()

        #Create Role
        rolename = fake.name()

        #Checkout Details
        companyname = fake.company()
        billingname = fake.name()
        address = fake.address()
        state = fake.state()
        postalcode = fake.postcode()
        city = fake.city()



        # Create a Chrome WebDriver instance
        

        login(driver=driver,email=email,password=password)
        introjs(driver)
        topup(driver=driver,companyname=companyname, billingname=billingname, address=address, state=state, postalcode=postalcode,city=city,cardnumber=cardnumber, cvn=cvn)
        user(driver)
        add_user(driver=driver, usermail=usermail, username=username, name=name, phone=phone, new_user_password=new_user_password, password_confirmation=password_confirmation)
        configure_modules(driver)
        create_group(driver=driver,groupname=groupname)
        setup_roles(rolename)
        insights(driver)
        livechat(driver)
        channels(driver)
        numbers(driver)
        call(driver)
        livechat_button(driver)
        tickets(driver)

    except Exception as e:
        print(f"An error occurred: {e}")


    finally:
        time.sleep(10)
        # Close the browser window
        driver.quit()
