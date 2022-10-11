from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from xlwt import Workbook
from datetime import date
from selenium.webdriver.common.action_chains import ActionChains
import time
import random

#Login Credentials
username = 'njaurigue@advantechglobal.org'
password = 'noahjaurigue2022$'
query = '(desktop OR "it" OR "information technology" OR administrator OR network OR system OR systems OR user) AND (850 OR pensacola OR navarre OR destin OR niceville OR milton OR eglin OR walton OR "panama city" OR tyndall OR bellview OR brent)'

#Start runtime timer
start = time.time()

#Defining Random Delay
random.seed(None, 2)
def delay():
    return random.randint(3,6)

def bot(username, password, query):
    #Create Driver
    options = Options()
    options.binary_location = '/Applications/Google Chrome.app'
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()

    #Open Sharepoint
    driver.get('https://advantechgsenterprisesinc.sharepoint.com/HR/TR/RESUMES%20%20INTERVIEWS/Forms/AllItems.aspx')

    #Microsoft Login
    driver.find_element(By.NAME, 'loginfmt').send_keys(username)
    driver.find_element(By.ID, 'idSIButton9').click()
    driver.find_element(By.NAME, 'passwd').send_keys(password)
    time.sleep(1)
    driver.find_element(By.ID, 'idSIButton9').click()
    time.sleep(1)
    driver.find_element(By.ID, 'idSIButton9').click()    

    #Search Query
    driver.find_element(By.TAG_NAME, 'INPUT').send_keys(query)
    driver.find_element(By.TAG_NAME, 'INPUT').send_keys(Keys.RETURN)
    time.sleep(5)

    #Go to first file
    driver.find_element(By.CLASS_NAME, 'ms-Link').click()
    i = 0
    while(True):
        print('NEW')
        tabs = driver.window_handles
        time.sleep(3)
        driver.switch_to.window(tabs[1])
        url = driver.current_url
        print(str(i) + ": " + url)
        driver.close()
        driver.switch_to.window(tabs[0])
        driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.ARROW_DOWN)
        print('BEFORE')
        #driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.RETURN)
        driver.switch_to.active_element.send_keys(Keys.RETURN)
        print('AFTER')
        i += 1

        time.sleep(2)



    #Scrolling and Adding Links
    scope = 0
    dupes = []
    while(scope < 10):
        i = 0
        apps = driver.find_elements(By.CLASS_NAME, 'ms-Link')
        print('APPS: ' + str(len(apps)))
        apps[i].click()
        #Get list of tabs
        tabs = driver.window_handles
        driver.switch_to.window(tabs[1])
        url = driver.current_url
        print(str(i) + ": " + url)
        i += 1
        time.sleep(200)
    #driver.find_element(By.CLASS_NAME, 'od-scrollablePane-content-ItemsScopeList').click()

    time.sleep(200)


    start = time.time()
    while(time.time() < start + 30):
        set = driver.find_elements(By.CLASS_NAME, 'ms-Link')
        for i in set:
            dupes.append(i)
        driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.PAGE_DOWN)
        print('URLS: ' + str(len(list(dict.fromkeys(dupes)))))

    print('DUPES: ' + str(len(dupes)))
    #Remove Duplicates
    urls = list(dict.fromkeys(dupes))
    print('URLS: ' + str(len(urls)))

    urls[0].click()
    time.sleep(200)

bot(username, password, query)

#Record and ouput runtime
end = time.time()
print('PROGRAM RUNTIME: ' + str(end - start))

