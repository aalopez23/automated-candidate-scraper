from shareplum import Site
from shareplum import Office365
from shareplum.site import Version
from xlwt import Workbook
from datetime import date

import time
import random

#Login Credentials
username = 'njaurigue@advantechglobal.org'
password = 'noahjaurigue2022$'
query = '(desktop OR "it" OR "information technology" OR administrator OR network OR system OR systems OR user) AND (850 OR pensacola OR navarre OR destin OR niceville OR milton OR eglin OR walton OR "panama city" OR tyndall OR bellview OR brent)'

#Start runtime timer
start = time.time()

<<<<<<< Updated upstream
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

    #Scrolling and Adding Links
    dupes = []
    apps = driver.find_elements(By.CLASS_NAME, 'ms-Link')
    apps[100].click()
    #driver.find_element(By.CLASS_NAME, 'od-scrollablePane-content-ItemsScopeList').click()

    time.sleep(200)
=======
>>>>>>> Stashed changes

auth = Office365('https://advantechgsenterprisesinc.sharepoint.com', username = username, password = password).GetCookies()
site = Site('https://advantechgsenterprisesinc.sharepoint.com/HR/TR/RESUMES%20%20INTERVIEWS/Forms/AllItems.aspx', version = Version.v365, authcookie=auth)

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


#Record and ouput runtime
end = time.time()
print('PROGRAM RUNTIME: ' + str(end - start))

