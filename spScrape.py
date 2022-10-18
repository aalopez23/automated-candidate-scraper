from re import L
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
from playsound import playsound

#Login Credentials
username = 'stran@advantechglobal.org'
password = 'steventran2022$'
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
    actions = ActionChains(driver)
    driver.maximize_window()

    #Open Sharepoint
    driver.get('https://advantechgsenterprisesinc.sharepoint.com/HR/TR/RESUMES%20%20INTERVIEWS/Forms/AllItems.aspx')
    time.sleep(1)

    #Microsoft Login
    driver.find_element(By.NAME, 'loginfmt').send_keys(username)
    time.sleep(1)
    driver.find_element(By.ID, 'idSIButton9').click()
    time.sleep(1)
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
    urls = []
    #Selecting the list and the not the specific element
    # Don't ask why it works but it works
    driver.find_element(By.CLASS_NAME, "root-125").click()
    print("------------" + str(len(driver.find_elements(By.CLASS_NAME, "root-125"))) + "------------")
    actions.send_keys(Keys.DOWN)
    actions.send_keys(Keys.DOWN)
    actions.send_keys(Keys.UP)
    actions.send_keys(Keys.RETURN)
    actions.perform()
    
    i = 0
    while(True):
        tabs = driver.window_handles
        time.sleep(3)
        
        if len(tabs) >= 2:
            #Base Case (There is a New Tab)
            driver.switch_to.window(tabs[1])
            url = driver.current_url
            urls.append(url)
            print(str(i + 1) + ": " + url)
            driver.close()
            driver.switch_to.window(tabs[0])
            time.sleep(1)

        else:
            #No New Tab
            url = driver.current_url
            urls.append(url)
            print(str(i + 1) + ": " + url)
            actions.send_keys(Keys.ESCAPE)
            actions.perform()
            time.sleep(1)

        #Checks if the last url two urls are the same, reintialize the pointer
        if (len(urls) > 1) and (urls[-1] == urls[-2]):
            print('---------------HIT MAX---------------')
            playsound('mixkit-positive-notification-951.mp3')
            driver.find_element(By.CLASS_NAME, "root-125").click()
            actions.send_keys(Keys.DOWN)
            actions.send_keys(Keys.DOWN)
            actions.send_keys(Keys.UP)
            actions.send_keys(Keys.RETURN)
            actions.perform()

        actions.send_keys(Keys.DOWN)
        print('DOWN')
        actions.send_keys(Keys.RETURN)
        print('RETURN')
        actions.perform()
        i += 1
        
        



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
        l = driver.find_elements(By.CLASS_NAME, 'ms-Link')
        for i in l:
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

