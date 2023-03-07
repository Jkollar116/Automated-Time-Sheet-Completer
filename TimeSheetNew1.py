# Import necessary libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import msvcrt


# Define username, password,
userName = (input("Enter your email: "))
password = ""
print("Enter your password:", end='', flush=True)
while True:
    ch = msvcrt.getch()
    if ch == b'\r':
        break
    password += ch.decode('utf-8')
    print('*', end='', flush=True)


# Set Chrome options to disable infobars and start in fullscreen
options = Options()
options.add_argument("--start-maximized")
options.add_experimental_option('detach', True)
chrome_driver = webdriver.Chrome()

# Set up the Chrome service with the path to the driver executable
service = ChromeService(executable_path="C:\\PATH\\TO\\CHROME\\DRIVER\\HERE")

# Create a Chrome driver instance using the service and options
driver = webdriver.Chrome(service=service, options=options)

# Define school and URL
school = "F"
url = "https://idm.suny.edu/security/login/loginForm.do?redirectUrl=https%3A%2F%2Fsuny.edu%3A443%2Ftime%2Fflow%2Fhome-flow"

# Open the URL in the Chrome driver
driver.get(url)


def insert_times(xPath, time):
    time_slot = driver.find_element(By.XPATH, xPath)
    time_slot.send_keys(time)
    time_slot.click()

def click_button(xPath):
    button = driver.find_element(By.XPATH, xPath)
    button.click()
# Select the school from the dropdown list
select_school = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div/form/fieldset/div[1]/div/div/select")
select_school.send_keys(school)
select_school.click()

# Submit the selected school
click_button("/html/body/div[2]/div/div/div/div/form/fieldset/div[6]/button")
time.sleep(3)
# Enter the username using the ActionChains method
actions = ActionChains(driver)
actions.send_keys(userName)
actions.perform()

# Submit the username
click_button("/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div[1]/div[3]/div/div/div/div[4]/div/div/div/div[2]/input")
time.sleep(2)


# Enter the password using the ActionChains method
actions = ActionChains(driver)
actions.send_keys(password)
actions.perform()

# Submit the password
click_button("/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[4]/div[2]/div/div/div/div/input")

# Clicks the "Stay signed in" button
click_button("/html/body/div/form/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[3]/div[2]/div/div/div[2]/input")

# Clicks the "Time Attendance" button
click_button("/html/body/div[1]/div[3]/form/input")

# Clicks the "Role" button
click_button("/html/body/div[1]/div[3]/form/div[3]/table[2]/tbody/tr[2]/td[1]/input")
time.sleep(2)
# Clicks the "Select Week" dropdown
click_button("/html/body/div[1]/div[3]/form/div[5]/select")

# Find the dropdown element on the webpage using its ID
dropdown_element = driver.find_element(By.ID,'accrualPeriodDropDown')

# Create a Select object to interact with the dropdown
dropdown = Select(dropdown_element)

# Select the first option in the dropdown
dropdown.select_by_index(1)

#Enters the time in for each day of the week into its timeslot slot
time.sleep(2)
#friday

day_num = "3"
for i in range (1, 3):

    #Friday
    insert_times("/html/body/div[1]/div[3]/form/div[6]/div[5]/table/tbody/tr[" + day_num + "]/td[3]/table/tbody/tr/td[1]/input[2]", "11:00a")
    insert_times("/html/body/div[1]/div[3]/form/div[6]/div[5]/table/tbody/tr[" + day_num + "]/td[3]/table/tbody/tr/td[2]/input", "01:30p")
    insert_times("/html/body/div[1]/div[3]/form/div[6]/div[5]/table/tbody/tr[" + day_num + "]/td[3]/table/tbody/tr/td[3]/input", "02:00p")
    insert_times("/html/body/div[1]/div[3]/form/div[6]/div[5]/table/tbody/tr[" + day_num + "]/td[3]/table/tbody/tr/td[4]/input", "07:00p")
    day_num_int = int(day_num)
    day_num_int += 3
    day_num = str(day_num_int)

    #Monday
    insert_times("/html/body/div[1]/div[3]/form/div[6]/div[5]/table/tbody/tr[" + day_num + "]/td[3]/table/tbody/tr/td[1]/input[2]", "05:45p")
    insert_times("/html/body/div[1]/div[3]/form/div[6]/div[5]/table/tbody/tr[" + day_num + "]/td[3]/table/tbody/tr/td[2]/input", "10:00p")
    day_num_int = int(day_num)
    day_num_int += 1
    day_num = str(day_num_int)
    #Tuesday
    insert_times("/html/body/div[1]/div[3]/form/div[6]/div[5]/table/tbody/tr[" + day_num + "]/td[3]/table/tbody/tr/td[1]/input[2]", "12:15p")
    insert_times("/html/body/div[1]/div[3]/form/div[6]/div[5]/table/tbody/tr[" + day_num + "]/td[3]/table/tbody/tr/td[2]/input", "01:30p")
    insert_times("/html/body/div[1]/div[3]/form/div[6]/div[5]/table/tbody/tr[" + day_num + "]/td[3]/table/tbody/tr/td[3]/input", "03:00p")
    insert_times("/html/body/div[1]/div[3]/form/div[6]/div[5]/table/tbody/tr[" + day_num + "]/td[3]/table/tbody/tr/td[4]/input", "04:25p")
    day_num_int = int(day_num)
    day_num_int += 1
    day_num = str(day_num_int)
    #Wednesday
    insert_times("/html/body/div[1]/div[3]/form/div[6]/div[5]/table/tbody/tr[" + day_num + "]/td[3]/table/tbody/tr/td[1]/input[2]", "04:30p")
    insert_times("/html/body/div[1]/div[3]/form/div[6]/div[5]/table/tbody/tr[" + day_num + "]/td[3]/table/tbody/tr/td[2]/input", "10:00p")

    day_num ="11"








