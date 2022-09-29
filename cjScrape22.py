from ssl import ALERT_DESCRIPTION_BAD_CERTIFICATE_HASH_VALUE
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from xlwt import Workbook
from datetime import date
from selenium.webdriver.common.action_chains import ActionChains
import time
import random

random.seed(None, 2)
def delay():
    return random.randint(3,6)

#USER INPUTS
#Logins: (Ptage92121, Advantech2022$) // (cba92037, g#M8q2qQ)
username = 'Ptage92121'
password = 'Advantech2022$'
query = '(moodle OR blackboard OR canvas OR lms OR "learning management" OR "learning assessment")'

def bot(username, password):
    #Create Driver
    options = Options()
    options.add_argument('--incognito')
    driver = webdriver.Chrome(executable_path=r'C:\Users\Noah Jaurigue\Downloads\chromedriver_win32\chromedriver.exe', chrome_options=options)
    driver.maximize_window()

    #Open Clearance Jobs
    driver.get('https://www.clearancejobs.com/login')
    time.sleep(delay())
    
    #Login
    fields = driver.find_elements(By.CLASS_NAME, 'el-input__inner')
    fields[0].send_keys(username)
    time.sleep(delay())
    fields[1].send_keys(password)
    time.sleep(delay())
    driver.find_element(By.CLASS_NAME, 'btn-submitForm').click()
    time.sleep(delay())

    #Boolean Search Page, w/ Query
    driver.get('https://www.clearancejobs.com/resumes/advanced-search/boolean')
    time.sleep(delay())
    driver.find_element(By.CLASS_NAME, 'cj-textarea__inner').send_keys(query)
    time.sleep(delay())
    driver.find_element(By.CLASS_NAME, 'btn-info').click()
    time.sleep(delay())

    #Change to 50 per page
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div[3]/div/div[2]/div[2]/div[1]/div/span').click()
    time.sleep(delay())
    driver.find_element(By.XPATH, '//*[text()="50 per page"]').click()
    time.sleep(10)

    #Create Workbook
    wb = Workbook()
    row = 0
    s1 = wb.add_sheet('S1')
    s1.write(row, 0, "Name")
    s1.write(row, 1, "Phone Number")
    s1.write(row, 2, "E-Mail")
    s1.write(row, 3, "Title")
    s1.write(row, 4, "Clearance")
    s1.write(row, 5, "YOE")
    s1.write(row, 6, "Relocation?")
    s1.write(row, 7, "Salary")
    s1.write(row, 8, "Highest Degree")
    s1.write(row, 9, "Military Branch")
    s1.write(row, 10,"Ideal Locations")
    s1.write(row, 11,"Last Profile Update")
    wb.save('cjScrape22_' + date.today().strftime("%m_%d_%Y") + '.xls')
    row += 1

    #Call wbPush() for each CJ page
    row = pagePush(driver, wb, s1, row)

#Push applicant data (50 apps) from one CJ page, push to Workbook
def pagePush(driver, wb, s1, row):
    #Retrieve all applicant URLs
    apps = driver.find_elements(By.CLASS_NAME, 'resume-search-candidate-card-desktop__name')
    print('# of Applicants: ' + str(len(apps)))
    pg = 0
    urls = []
    while(pg < len(apps)):
        print(apps[pg].get_attribute('href'))
        urls.append(apps[pg].get_attribute('href'))
        pg += 1

    #Loop through apps
    pg = 0
    while(pg < len(apps)):
        #Open applicant page
        print('READING: ' + str(pg))
        print('URL: ' + urls[pg])
        driver.get(urls[pg])
        time.sleep(delay())

        #Get list of desired info [name, phone, email, title, clearance, YOE, relo, salary, degree, branch, ideal locations, last update]
        name = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div[1]/div[1]/div/div[2]/div[2]/div[2]/div/span[1]').get_attribute('innerText')
        print(name)
        pg += 1
        row += 1
        driver.back()
        time.sleep(delay())  
        
        time.sleep(200)

    return row

bot(username, password)