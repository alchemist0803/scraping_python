import os
import time
from dotenv import load_dotenv
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import random
import string
import csv
import json

options = Options()

options.add_argument("--ignore-certificate-errors")
options.add_argument("--disable-web-security")
options.add_argument("--disable-content-safety-policy")
options.add_argument("--disable-features=CrossSiteDocumentBlockingIfIsolating")
options.add_argument('disable-infobars')
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("prefs", {"download.prompt_for_download": False})
# options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-javascript")

service = Service(ChromeDriverManager().install())
for i in range(1, 100):

    driver = webdriver.Chrome(options=options, service=service)

    target_url = "https://www.doordash.com"

    driver.get(target_url)

    signUpButton = driver.find_element(By.CLASS_NAME, "jkSREy")
    signUpButton.click()
    iframe_element = driver.find_element(By.CSS_SELECTOR, "iframe")
    driver.switch_to.frame(iframe_element)

    characters = string.ascii_letters + string.digits

    time.sleep(5)

    first_name = "John"
    last_name = "Doe"
    email = ''.join(random.choice(characters) for _ in range(5))+"@gmail.com"
    phone = random.randint(3214310000, 3219999999)
    # phone = random.randint(10000000000, 99999999999)
    password = "Abcdefg123!@#"

    print("===>first_name", first_name)
    print("===>last_name", last_name)
    print("===>email", email)
    print("===>phone", phone)
    print("===>password", password)

    first_name_input = driver.find_element(By.ID, "FieldWrapper-0")
    last_name_input = driver.find_element(By.ID, "FieldWrapper-1")
    email_input = driver.find_element(By.ID, "FieldWrapper-2")
    phone_input = driver.find_element(By.ID, "FieldWrapper-4")
    password_input = driver.find_element(By.ID, "FieldWrapper-5")
    submit_button = driver.find_element(By.ID, "sign-up-submit-button")

    first_name_input.click()
    first_name_input.clear()
    first_name_input.send_keys(first_name)

    last_name_input.click()
    last_name_input.clear()
    last_name_input.send_keys(last_name)

    email_input.click()
    email_input.clear()
    email_input.send_keys(email)

    phone_input.click()
    phone_input.clear()
    phone_input.send_keys(phone)

    password_input.click()
    password_input.clear()
    password_input.send_keys(password)

    submit_button.click()

    time.sleep(10)

    new_array = [first_name, last_name, email, phone, password]

    # File path
    csv_file_path = "data.csv"

    # Read the existing data from the CSV file
    existing_data = []
    with open(csv_file_path, 'r', newline='') as csv_file:
        reader = csv.reader(csv_file)
        existing_data = list(reader)

    # Append the new array to the existing data
    existing_data.append(new_array)

    # Write the updated data back to the CSV file
    with open(csv_file_path, 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        
        # Write the new array as a row
        writer.writerow(new_array)


    print(f"JSON data saved to CSV file: {csv_file_path}")

    driver.close()
    driver.quit()